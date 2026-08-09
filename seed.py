"""Optional: populate the database with a few sample products so the app
isn't empty on first run.

Usage:
    python seed.py
"""
import os
import random
from math import ceil

from app import create_app
from extensions import db
from models import Product


def generate_product(i, categories, units):
    name = f"Sample Product {i:06d}"
    category = random.choice(categories)
    price = round(random.uniform(20, 2000), 2)
    cost_price = round(price * random.uniform(0.6, 0.95), 2)
    stock_qty = random.randint(0, 500)
    low_stock_threshold = random.randint(1, 20)
    unit = random.choice(units)
    return {
        "name": name,
        "category": category,
        "price": price,
        "cost_price": cost_price,
        "stock_qty": stock_qty,
        "low_stock_threshold": low_stock_threshold,
        "unit": unit,
    }


TARGET = int(os.environ.get("SEED_COUNT", "100000"))
BATCH_SIZE = int(os.environ.get("SEED_BATCH", "5000"))

categories = ["Grocery", "Household", "Stationery", "Beverages", "Snacks", "Personal Care"]
units = ["pcs", "pack", "bottle", "bag"]


app = create_app()
with app.app_context():
    # ensure tables exist
    db.create_all()

    existing = Product.query.count()
    if existing >= TARGET:
        print(f"Existing products ({existing}) >= target ({TARGET}) — skipping seed.")
    else:
        to_create = TARGET - existing
        print(f"Seeding {to_create} products in batches of {BATCH_SIZE} (target {TARGET}).")
        batches = ceil(to_create / BATCH_SIZE)
        created = 0
        next_idx = existing + 1
        for b in range(batches):
            this_batch = min(BATCH_SIZE, to_create - created)
            mappings = [generate_product(next_idx + j, categories, units) for j in range(this_batch)]
            db.session.bulk_insert_mappings(Product, mappings)
            db.session.commit()
            created += this_batch
            next_idx += this_batch
            print(f"Inserted {created}/{to_create} records...")

        print(f"Seeding complete: inserted {created} new products (total now {Product.query.count()}).")


if __name__ == "__main__":
    # allow running directly as: python seed.py or set SEED_COUNT env var
    pass
