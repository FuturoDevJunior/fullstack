from pymongo import MongoClient
from bson import ObjectId
from models import Product, Category, Order

client = MongoClient("mongodb://mongo:27017/")
db = client["store"]

def create_item(collection, item):
    result = db[collection].insert_one(item.dict(exclude={"id"}))
    return str(result.inserted_id)

def get_items(collection):
    return [{**item, "id": str(item["_id"])} for item in db[collection].find()]

def get_item(collection, id):
    item = db[collection].find_one({"_id": ObjectId(id)})
    return {**item, "id": str(item["_id"])} if item else None

def update_item(collection, id, item):
    db[collection].update_one({"_id": ObjectId(id)}, {"$set": item.dict(exclude={"id"})})
    return get_item(collection, id)

def delete_item(collection, id):
    db[collection].delete_one({"_id": ObjectId(id)})

def get_dashboard(category_id=None, product_id=None, period=None):
    pipeline = [{"$group": {"_id": None, "total_orders": {"$sum": 1}, "avg_total": {"$avg": "$total"}, "total_revenue": {"$sum": "$total"}}}]
    if category_id or product_id:
        match = {}
        if category_id:
            match["category_ids"] = category_id
        if product_id:
            match["product_ids"] = product_id
        pipeline.insert(0, {"$match": match})
    result = list(db.orders.aggregate(pipeline))
    return result[0] if result else {"total_orders": 0, "avg_total": 0, "total_revenue": 0}