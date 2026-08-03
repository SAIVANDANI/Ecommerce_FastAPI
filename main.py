from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-Commerce Product API",
    description="CRUD Operations for E-Commerce Products - Clothes, Beverages, Electronic Devices, Accessories, Beauty & Personal Care",
    version="1.0"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def welcome():
    return {"message": "Welcome to E-Commerce Product Management API"}


# Create Product
@app.post("/products", response_model=schemas.ProductResponse)
def create(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)


# Get All Products
@app.get("/products", response_model=list[schemas.ProductResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_products(db)


# Get Product By ID
@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def read_one(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Update Product
@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated = crud.update_product(db, product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


# Delete Product
@app.delete("/products/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}


# Get Products By Category
@app.get("/category/{category_name}", response_model=list[schemas.ProductResponse])
def category_products(category_name: str, db: Session = Depends(get_db)):
    product_list = crud.get_by_category(db, category_name)
    if not product_list:
        raise HTTPException(status_code=404, detail="No products found in this category")
    return product_list
