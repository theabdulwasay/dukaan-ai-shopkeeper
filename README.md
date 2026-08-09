<div align="center">

# 🏪 Dukaan AI

### **Smart Shop Management · Powered by AI**

**A lightweight, self-hosted shop management system built for small businesses.**

Inventory · POS Billing · Sales Analytics · Reports · AI Assistant

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge\&logo=flask\&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-File--Based-003B57?style=for-the-badge\&logo=sqlite\&logoColor=white)](https://www.sqlite.org/)
[![Claude](https://img.shields.io/badge/AI-Claude-D97757?style=for-the-badge)](https://www.anthropic.com/)
[![License](https://img.shields.io/badge/License-MIT-8A8A8A?style=for-the-badge)](LICENSE)

<br/>

**Run your shop. Track your stock. Understand your sales. Let AI help.**

</div>

---

## 🌟 Overview

**Dukaan AI** is a self-hosted shop management application designed for small businesses such as:

* 🛒 Grocery stores
* 🏪 General stores
* 📚 Stationery shops
* 👕 Retail shops
* 📦 Small inventory-based businesses

It combines everyday shop operations with an **AI-powered assistant** that can understand your actual inventory and sales data.

Unlike a generic chatbot, Dukaan AI can answer questions using your **live shop database**.

> 💡 **Example:**
> Ask *"What products are low in stock?"* or *"How much did I sell today?"* and the assistant can respond using your actual shop data.

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🏠 Smart Dashboard

* Today's revenue
* Total sales
* Low-stock alerts
* Recent transactions
* Quick business overview

</td>
<td width="50%">

### 📦 Inventory Management

* Add products
* Edit product details
* Delete products
* Track stock quantity
* Manage prices & costs
* Organize products by category

</td>
</tr>

<tr>
<td width="50%">

### 🧾 POS Billing

* Create shopping carts
* Add multiple products
* Automatic stock deduction
* Calculate totals
* Complete checkout
* Generate printable receipts

</td>
<td width="50%">

### 📊 Reports & Analytics

* 1-day reports
* 7-day reports
* 30-day reports
* Daily revenue charts
* Sales statistics
* Top-selling products

</td>
</tr>

<tr>
<td width="50%">

### 🤖 AI Assistant

* Ask questions about your shop
* Analyze live inventory
* Analyze sales
* Generate product descriptions
* Draft customer replies

</td>
<td width="50%">

### 🌍 Multi-Language Friendly

Supports:

* 🇬🇧 English
* 🇵🇰 Roman Urdu
* اردو

</td>
</tr>
</table>

---

# 🤖 AI Assistant

The **Dukaan AI Assistant** has three specialized modes.

### 🔎 1. Ask About My Shop

Ask questions about your actual business data.

**Examples:**

```text
What's low in stock?

How much did I sell today?

Which products are selling the most?

What was my revenue this week?

Which products need restocking?
```

The assistant uses information from the application's database instead of guessing.

> 🔐 **Data-first principle:**
> If the required information does not exist in the database, the assistant should say that it does not have enough data rather than inventing numbers.

---

### ✍️ 2. Write Product Description

Turn basic product information into polished marketing content.

**Input:**

```text
Product: Premium Green Tea
Category: Beverages
Details: 250g, organic, imported
```

**AI can generate:**

* Shelf descriptions
* Product listings
* Social media captions
* Short promotional copy

---

### 💬 3. Reply to a Customer

Paste a customer's message and get a natural response.

**Example:**

```text
Customer:
"Do you have this product available?"
```

The assistant can generate a professional response that can be copied and sent directly.

---

# 🧠 How It Works

```text
                 ┌──────────────────────┐
                 │      Shopkeeper      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │     Dukaan AI UI     │
                 │  HTML · CSS · JS     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Flask Backend     │
                 │   REST / Web Routes  │
                 └───────┬───────┬──────┘
                         │       │
                ┌────────▼─┐   ┌─▼────────────┐
                │  SQLite  │   │ AI Assistant │
                │ Database │   │  Anthropic   │
                └──────────┘   └──────────────┘
```

### Core flow

```text
Shopkeeper
    ↓
Dashboard / Inventory / Billing
    ↓
Flask Backend
    ↓
SQLite Database
    ↓
Reports & Business Data
    ↓
AI Assistant
    ↓
Useful Shop-Specific Responses
```

---

# 🛠️ Tech Stack

| Layer            | Technology                |
| ---------------- | ------------------------- |
| 🐍 Backend       | Python 3.10+              |
| 🌐 Web Framework | Flask 3.0                 |
| 🗄️ ORM          | Flask-SQLAlchemy          |
| 💾 Database      | SQLite                    |
| 🎨 Frontend      | HTML5 · CSS3 · JavaScript |
| 🤖 AI            | Anthropic API             |
| 🧠 AI SDK        | `anthropic` Python SDK    |
| 📊 Charts        | JavaScript-based charts   |
| 🔐 Configuration | Environment Variables     |

### Why SQLite?

Dukaan AI is designed for small shops, so it avoids unnecessary infrastructure.

There is:

* ❌ No database server
* ❌ No complex deployment
* ❌ No separate database administration

Instead:

```text
instance/shop.db
```

contains the application's local database.

---

# 🚀 Getting Started

## 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/dukaan-ai.git
cd dukaan-ai
```

---

## 2️⃣ Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure the AI API

Copy the environment template:

```bash
cp .env.example .env
```

Then configure:

```env
ANTHROPIC_API_KEY=your-actual-key-here
```

Get your API key from the **Anthropic Console**:

https://console.anthropic.com

> ℹ️ The complete shop management system works without an AI API key. Only the **AI Assistant** functionality requires the key.

---

## 5️⃣ Optional `.env` support

If your application does not automatically load `.env`, install:

```bash
pip install python-dotenv
```

Then add:

```python
from dotenv import load_dotenv

load_dotenv()
```

to your application startup.

---

## 6️⃣ Seed sample data

Optional sample products and sales can be created using:

```bash
python seed.py
```

---

## 7️⃣ Start the application

```bash
python app.py
```

Then open:

```text
http://localhost:5000
```

🎉 **Dukaan AI is ready!**

The SQLite database will automatically be created at:

```text
instance/shop.db
```

---

# 📁 Project Structure

```text
dukaan-ai/
│
├── app.py
├── config.py
├── extensions.py
├── models.py
├── seed.py
├── requirements.txt
├── .env.example
├── README.md
│
├── routes/
│   ├── dashboard.py
│   ├── inventory.py
│   ├── billing.py
│   ├── reports.py
│   └── chat.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── billing.html
│   ├── receipt.html
│   ├── reports.html
│   ├── chat.html
│   │
│   └── inventory/
│       ├── list.html
│       └── form.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── billing.js
│       └── chat.js
│
└── instance/
    └── shop.db
```

---

# 🗃️ Database Models

Dukaan AI uses a simple relational structure:

```text
┌──────────────┐
│   Product    │
├──────────────┤
│ id           │
│ name         │
│ category     │
│ price        │
│ cost         │
│ stock        │
└──────┬───────┘
       │
       │
       ▼
┌──────────────┐
│   SaleItem   │
├──────────────┤
│ id           │
│ sale_id      │
│ product_id   │
│ quantity     │
│ price        │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     Sale     │
├──────────────┤
│ id           │
│ total        │
│ date         │
└──────────────┘
```

The application can also maintain customer information through the `Customer` model.

---

# 📊 Business Workflow

```text
        ADD PRODUCTS
             │
             ▼
      ┌─────────────┐
      │  INVENTORY  │
      └──────┬──────┘
             │
             ▼
       CREATE BILL
             │
             ▼
        CHECKOUT
             │
       ┌─────┴─────┐
       ▼           ▼
   Sale Saved   Stock Updated
       │
       ▼
     REPORTS
       │
       ▼
   BUSINESS INSIGHTS
       │
       ▼
    🤖 AI ASSISTANT
```

---

# 🔐 Security Notes

Dukaan AI is designed primarily for **local or private deployment**.

### Current limitations

* No user authentication
* No role-based access control
* Designed for a single shop
* SQLite is intended for lightweight usage

⚠️ **Do not expose the application directly to the public internet without adding authentication, authorization, HTTPS, secure secret management, and other production security controls.**

---

# 🧩 AI Safety & Data Principles

The AI Assistant is designed around the shop's existing data.

### ✅ It can

* Read relevant shop information
* Summarize inventory
* Analyze sales information
* Generate descriptions
* Draft customer messages

### ❌ It should not

* Invent stock quantities
* Fabricate sales numbers
* Make up product prices
* Pretend database information exists when it does not

This makes the assistant more useful for **real shop operations**.

---

# 🎯 Use Cases

### 🛒 Grocery Store

Track:

```text
Milk
Bread
Sugar
Rice
Cooking Oil
Tea
Biscuits
```

### 📚 Stationery Shop

Manage:

```text
Pens
Notebooks
Markers
Files
Registers
Printing Supplies
```

### 🏪 General Store

Use the complete system for:

```text
Inventory
Billing
Sales
Reports
Customer communication
AI assistance
```

---

# 🗺️ Roadmap

Potential future improvements:

* [ ] 🔐 User authentication
* [ ] 👥 Multiple shop employees
* [ ] 🏬 Multi-branch support
* [ ] 📱 Responsive mobile UI
* [ ] 📈 Advanced analytics
* [ ] 📦 Supplier management
* [ ] 🔔 Automatic low-stock notifications
* [ ] 🧾 PDF invoices
* [ ] 💳 Payment tracking
* [ ] ☁️ Cloud deployment
* [ ] 📤 Excel / CSV export
* [ ] 🌐 Urdu-first interface
* [ ] 📱 WhatsApp customer integration
* [ ] 🧠 AI sales forecasting

---

# 🤝 Contributing

Contributions are welcome!

```bash
# Fork the repository

# Create a feature branch
git checkout -b feature/amazing-feature

# Commit your changes
git commit -m "Add amazing feature"

# Push your branch
git push origin feature/amazing-feature
```

Then open a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

<div align="center">

## 🏪 Dukaan AI

### **Simple software. Smarter shops.**

Built for shopkeepers who would rather **run their business than fight their software.**

<br/>

**Inventory · Billing · Reports · AI**

<br/>

⭐ **If you find this project useful, consider giving it a star!**

</div>
