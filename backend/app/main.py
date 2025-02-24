from fastapi import FastAPI, HTTPException, UploadFile, File
from models import Product, Category, Order
from crud import create_item, get_items, get_item, update_item, delete_item, get_dashboard
from s3_utils import upload_to_s3

app = FastAPI()

@app.post("/products/", response_model=Product)
async def create_product(product: Product, image: UploadFile = File(...)):
    product.image_url = upload_to_s3(image.file)
    product_id = create_item("products", product)
    return {**product.dict(), "id": product_id}

@app.get("/products/")
async def list_products():
    return get_items("products")

@app.put("/products/{id}")
async def update_product(id: str, product: Product):
    if not get_item("products", id):
        raise HTTPException(404, "Product not found")
    return update_item("products", id, product)

@app.delete("/products/{id}")
async def delete_product(id: str):
    if not get_item("products", id):
        raise HTTPException(404, "Product not found")
    delete_item("products", id)
    return {"message": "Product deleted"}