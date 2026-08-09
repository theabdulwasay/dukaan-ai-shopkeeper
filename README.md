<div align="center">

# 🏪 Dukaan AI

**A self-hosted shop management app for small shopkeepers.**
Inventory · Billing · Reports · AI Assistant — all in one lightweight web app.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-file--based-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Claude](https://img.shields.io/badge/AI-Claude-D97757?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-8A8A8A?style=flat-square)

</div>

---

## ✨ What it does

Dukaan AI gives a small shop — grocery, general store, stationery, anything —
a simple dashboard to run day-to-day operations, plus an AI assistant that
actually knows your live inventory and sales, not just generic advice.

| | |
|---|---|
| 🏠 **Dashboard** | Today's revenue, sales count, low-stock alerts, recent sales at a glance |
| 📦 **Inventory** | Add, edit, and remove products — track stock, price, cost, and category |
| 🧾 **Billing (POS)** | Build a cart, checkout, auto-decrement stock, print a receipt |
| 📊 **Reports** | Revenue & sales over 1 / 7 / 30 days, daily bar chart, top products |
| 🤖 **AI Assistant** | Ask about your shop, write product descriptions, draft customer replies |

**Languages:** English · Roman Urdu · اردو (Urdu script)

---

## 🧠 The AI Assistant, in detail

The assistant has three modes, switchable right in the chat:

- **Ask about my shop** — answers using your *actual* database (e.g. *"what's low in stock?"*, *"how much did I sell today?"*). It never invents numbers — if the data doesn't have the answer, it says so.
- **Write product description** — turns a product name + a few details into a ready-to-use shelf tag or social post.
- **Reply to a customer** — paste in a customer's message, get a natural reply you can send as-is.

---

## 🛠️ Tech stack

- **Backend:** Python 3.10+, Flask, Flask-SQLAlchemy
- **Database:** SQLite (a single file — no server to install or manage)
- **Frontend:** Plain HTML / CSS / JS — no build step, no framework
- **AI:** Anthropic API via the `anthropic` Python SDK

---

## 🚀 Getting started

### 1. Install dependencies

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Add your API key

```bash
cp .env.example .env
```

Open `.env` and set:

```env
ANTHROPIC_API_KEY=your-actual-key-here
```

Get a key from the [Anthropic Console](https://console.anthropic.com).
> Everything except the **AI Assistant** page works fine with no key at all.

<details>
<summary>Optional: auto-load <code>.env</code> with python-dotenv</summary>

`app.py` reads environment variables via `os.environ`, so `.env` isn't
loaded automatically. Either export it manually before running:

```bash
export $(cat .env | xargs)
```

or add these two lines to the top of `app.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

</details>

### 3. (Optional) seed sample data

```bash
python seed.py
```

### 4. Run it

```bash
python app.py
```

Then open **http://localhost:5000** 🎉

> The SQLite file is created automatically at `instance/shop.db` on first run.

---

## 📁 Project structure

```
shopkeeper_ai/
├── app.py                    # app factory + entry point
├── config.py                 # configuration (reads .env)
├── extensions.py             # Flask-SQLAlchemy instance
├── models.py                 # Product, Customer, Sale, SaleItem
├── seed.py                   # optional sample data
├── requirements.txt
├── .env.example
│
├── routes/
│   ├── dashboard.py
│   ├── inventory.py
│   ├── billing.py
│   ├── reports.py
│   └── chat.py                # AI assistant endpoint
│
├── templates/                 # Jinja2 HTML templates
│   ├── base.html
│   ├── dashboard.html
│   ├── billing.html
│   ├── receipt.html
│   ├── reports.html
│   ├── chat.html
│   └── inventory/
│       ├── list.html
│       └── form.html
│
└── static/
    ├── css/style.css
    └── js/
        ├── billing.js
        └── chat.js
```

---

## 📝 Notes

- Built for a **single shop**, run locally or on your own server. There's
  no login/authentication — add one before exposing it on the public internet.
- The AI assistant only ever sees the data already in your database; it
  never fabricates stock numbers or prices.
- To change the AI model, edit the `model=` line in `routes/chat.py`.

---

<div align="center">
<sub>Built for shopkeepers who'd rather run their shop than fight software. 🛍️</sub>
</div>
