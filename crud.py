from sqlalchemy.orm import Session
import models
import schemas


# Create Product
def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# Get All Products
def get_products(db: Session):
    return db.query(models.Product).all()


# Get Product By ID
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(
        models.Product.id == product_id
    ).first()


# Get Products By Category
def get_by_category(db: Session, category_name: str):
    return db.query(models.Product).filter(
        models.Product.category == category_name
    ).all()


# Update Product
def update_product(db: Session, product_id: int, product: schemas.ProductCreate):
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    db_product.category = product.category
    db_product.brand = product.brand
    db_product.product_name = product.product_name
    db_product.price = product.price
    db_product.stock = product.stock

    db.commit()
    db.refresh(db_product)
    return db_product


# Delete Product
def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if not db_product:
        return None

    db.delete(db_product)
    db.commit()
    return db_product
