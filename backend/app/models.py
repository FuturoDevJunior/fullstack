from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Category(BaseModel):
    id: Optional[str] = None
    name: str

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    price: float
    category_ids: List[str]
    image_url: Optional[str] = None

class Order(BaseModel):
    id: Optional[str] = None
    date: datetime
    product_ids: List[str]
    total: float