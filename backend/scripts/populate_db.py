import pymongo
from datetime import datetime
import os

# Usa 'mongo' no Docker e 'localhost' localmente
mongo_host = os.getenv("MONGO_HOST", "mongo" if os.getenv("DOCKER_ENV") else "localhost")
client = pymongo.MongoClient(f"mongodb://{mongo_host}:27017/")
db = client["store"]

db.products.drop()
db.categories.drop()
db.orders.drop()

categories = [{"name": "Eletrônicos"}, {"name": "Roupas"}]
category_ids = [str(db.categories.insert_one(cat).inserted_id) for cat in categories]

products = [
    {"name": "Celular", "description": "Smartphone", "price": 999.99, "category_ids": [category_ids[0]], "image_url": "http://fake.com/celular.jpg"},
    {"name": "Camiseta", "description": "Camiseta algodão", "price": 29.99, "category_ids": [category_ids[1]], "image_url": "http://fake.com/camiseta.jpg"}
]
product_ids = [str(db.products.insert_one(prod).inserted_id) for prod in products]

orders = [
    {"date": datetime.now(), "product_ids": [product_ids[0]], "total": 999.99},
    {"date": datetime.now(), "product_ids": [product_ids[1]], "total": 29.99}
]
[db.orders.insert_one(order) for order in orders]

print("Banco populado com sucesso!")