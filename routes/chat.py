import os
from datetime import date

from flask import Blueprint, current_app, jsonify, render_template, request

from extensions import db
from models import Product, Sale

chat_bp = Blueprint("chat", __name__, url_prefix="/assistant")


def build_shop_context():
    """Summarize the current shop data so the AI answers with real facts,
    not guesses."""
    products = Product.query.order_by(Product.name).all()
    low_stock = [p for p in products if p.is_low_stock]

    today = date.today()
    todays_sales = Sale.query.filter(db.func.date(Sale.created_at) == today).all()
    revenue_today = sum(s.total_amount for s in todays_sales)

    lines = ["Current shop inventory:"]
    if products:
        for p in products[:300]:
            flag = "LOW STOCK" if p.is_low_stock else "ok"
            lines.append(
                f"- {p.name} | category: {p.category or 'n/a'} | "
                f"stock: {p.stock_qty} {p.unit} | price: Rs.{p.price} | {flag}"
            )
    else:
        lines.append("(no products in inventory yet)")

    lines.append("")
    lines.append(f"Today's sales so far: {len(todays_sales)} sale(s), revenue: Rs.{revenue_today:.2f}")
    if low_stock:
        lines.append(f"Low stock items ({len(low_stock)}): " + ", ".join(p.name for p in low_stock))
    else:
        lines.append("No low stock items right now.")

    return "\n".join(lines)


@chat_bp.route("/")
def index():
    return render_template("chat.html")


@chat_bp.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    mode = data.get("mode", "qa")  # qa | description | reply
    language = data.get("language", "English")

    if not question:
        return jsonify({"error": "Please type a question or some details first."}), 400

    api_key = current_app.config.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return jsonify({
            "error": "ANTHROPIC_API_KEY is not set. Add it to your .env file (see .env.example) and restart the server."
        }), 500

    try:
        import anthropic
    except ImportError:
        return jsonify({"error": 'The "anthropic" package is not installed. Run: pip install -r requirements.txt'}), 500

    client = anthropic.Anthropic(api_key=api_key)

    if mode == "description":
        system = (
            "You are a copywriting assistant for a small local shopkeeper. Write a short, "
            f"appealing product description (2-4 lines) for a shelf tag, WhatsApp status, or "
            f"social media post, in {language}. No markdown, no asterisks, no headers — plain text only."
        )
        user_message = question
    elif mode == "reply":
        system = (
            "You are a customer-service assistant for a small local shopkeeper. Write a short, "
            f"natural reply (1-3 lines) to the customer's message below, in {language}, ready to "
            "send as-is on WhatsApp or SMS. No markdown, no asterisks."
        )
        user_message = question
    else:  # qa — answer using real shop data
        system = (
            "You are a helpful assistant for a small local shopkeeper. Answer the shopkeeper's "
            "question about their inventory, stock, or sales using ONLY the shop data given below. "
            f"Reply in {language}, in short, plain, practical language, no markdown. If the data "
            "doesn't contain the answer, say so honestly instead of guessing.\n\n" + build_shop_context()
        )
        user_message = question

    try:
        response = client.messages.create(
            model="claude-sonnet-5",
            max_tokens=600,
            system=system,
            messages=[{"role": "user", "content": user_message}],
        )
        answer = "".join(
            block.text for block in response.content if getattr(block, "type", "") == "text"
        ).strip()
        return jsonify({"answer": answer or "(no response)"})
    except Exception as exc:  # noqa: BLE001 - surface any API error to the UI
        return jsonify({"error": f"AI request failed: {exc}"}), 500
