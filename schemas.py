from pydantic import BaseModel
class ProductCreate(BaseModel):
    category: str
    brand: str
    product_name: str
    price: float
    stock: int


class ProductResponse(ProductCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
