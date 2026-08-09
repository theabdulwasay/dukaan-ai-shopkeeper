# Dukaan AI — Shopkeeper's Assistant

A complete, self-hosted web app for small shopkeepers: inventory management,
billing/POS with printable receipts, sales reports, and an AI assistant
(powered by Claude) that can answer plain-language questions about your
stock and sales, write product descriptions, and draft replies to
customers.

## Features

- **Dashboard** — today's revenue, sales count, low-stock alerts, recent sales.
- **Inventory** — add, edit, delete products; track stock, price, cost, category.
- **Billing (POS)** — build a cart, checkout, auto-decrement stock, print a receipt.
- **Reports** — revenue/sales over 1/7/30 days, daily bar chart, top products, low stock list.
- **AI Assistant** — three modes:
  - *Ask about my shop* — answers using your live inventory & sales data (e.g. "what's low in stock?").
  - *Write product description* — turns basic details into a shelf-tag/social-post description.
  - *Reply to a customer* — drafts a ready-to-send reply to a customer's message.
  - Supports English, Roman Urdu, and Urdu script.

## Tech stack

- Python 3.10+, Flask, Flask-SQLAlchemy, SQLite (file-based, no server needed)
- Vanilla HTML/CSS/JS (no build step, no frontend framework)
- Anthropic API (`anthropic` Python SDK) for the AI assistant

## Setup

1. **Install dependencies** (a virtual environment is recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure your API key**:
   ```bash
   cp .env.example .env
   ```
   Then open `.env` and set:
   ```
   ANTHROPIC_API_KEY=your-actual-key-here
   ```
   You can get a key from the Anthropic Console (https://console.anthropic.com).
   Everything except the AI Assistant page works fine without a key.

3. **(Optional) load python-dotenv automatically** — `app.py` reads
   environment variables via `os.environ`. If you want `.env` to load
   automatically, either `export $(cat .env | xargs)` before running, or
   add these two lines to the top of `app.py`:
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

4. **(Optional) seed sample data**:
   ```bash
   python seed.py
   ```

5. **Run the app**:
   ```bash
   python app.py
   ```
   Then open http://localhost:5000 in your browser.

The SQLite database file is created automatically at
`instance/shop.db` the first time you run the app.

## Project structure

```
shopkeeper_ai/
├── app.py                 # app factory + entry point
├── config.py               # configuration (reads .env)
├── extensions.py           # Flask-SQLAlchemy instance
├── models.py                # Product, Customer, Sale, SaleItem
├── seed.py                  # optional sample data
├── requirements.txt
├── .env.example
├── routes/
│   ├── dashboard.py
│   ├── inventory.py
│   ├── billing.py
│   ├── reports.py
│   └── chat.py             # AI assistant endpoint
├── templates/               # Jinja2 HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── billing.html
│   ├── receipt.html
│   ├── reports.html
│   ├── chat.html
│   └── inventory/
│       ├── list.html
│       └── form.html
└── static/
    ├── css/style.css
    └── js/{billing,chat}.js
```

## Notes

- This app is designed for a single shop, run locally or deployed on your
  own server. It has no authentication/login — add one before exposing it
  on the public internet.
- The AI assistant only sees the inventory/sales data already in your
  database. It never invents stock numbers or prices.
- To change the AI model, edit the `model=` line in `routes/chat.py`.
