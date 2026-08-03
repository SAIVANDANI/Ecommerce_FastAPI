
from database import SessionLocal, engine, Base
import models

Base.metadata.create_all(bind=engine)

db = SessionLocal()

products = [
    # Clothes
    {"category": "Clothes", "brand": "Levis", "product_name": "Slim Fit Denim Jeans", "price": 2499.00, "stock": 40},
    {"category": "Clothes", "brand": "H&M", "product_name": "Cotton Crew Neck T-Shirt", "price": 599.00, "stock": 80},
    {"category": "Clothes", "brand": "Zara", "product_name": "Formal Slim Fit Shirt", "price": 1799.00, "stock": 35},
    {"category": "Clothes", "brand": "Puma", "product_name": "Zip-Up Hooded Jacket", "price": 2999.00, "stock": 25},
    {"category": "Clothes", "brand": "Allen Solly", "product_name": "Pleated Formal Trousers", "price": 1499.00, "stock": 30},

    # Beverages
    {"category": "Beverages", "brand": "Coca-Cola", "product_name": "Coca-Cola Classic 1.25L", "price": 90.00, "stock": 150},
    {"category": "Beverages", "brand": "Tropicana", "product_name": "Mixed Fruit Juice 1L", "price": 120.00, "stock": 100},
    {"category": "Beverages", "brand": "Nescafe", "product_name": "Instant Coffee 200g Jar", "price": 449.00, "stock": 60},
    {"category": "Beverages", "brand": "Bisleri", "product_name": "Packaged Drinking Water 1L", "price": 20.00, "stock": 300},
    {"category": "Beverages", "brand": "Red Bull", "product_name": "Energy Drink 250ml Can", "price": 125.00, "stock": 90},

    # Electronic Devices
    {"category": "Electronic Devices", "brand": "Samsung", "product_name": "Galaxy M14 Smartphone", "price": 12999.00, "stock": 20},
    {"category": "Electronic Devices", "brand": "Boat", "product_name": "Rockerz 450 Bluetooth Headphones", "price": 1499.00, "stock": 55},
    {"category": "Electronic Devices", "brand": "HP", "product_name": "Pavilion 15 Laptop", "price": 54999.00, "stock": 12},
    {"category": "Electronic Devices", "brand": "Mi", "product_name": "Smart Band 8 Fitness Tracker", "price": 2999.00, "stock": 45},
    {"category": "Electronic Devices", "brand": "Sony", "product_name": "Bluetooth Party Speaker", "price": 6999.00, "stock": 18},

    # Accessories
    {"category": "Accessories", "brand": "Fastrack", "product_name": "Analog Wrist Watch", "price": 1699.00, "stock": 40},
    {"category": "Accessories", "brand": "Titan", "product_name": "Leather Wallet for Men", "price": 899.00, "stock": 60},
    {"category": "Accessories", "brand": "Ray-Ban", "product_name": "UV Protection Sunglasses", "price": 3999.00, "stock": 22},
    {"category": "Accessories", "brand": "American Tourister", "product_name": "Laptop Backpack 30L", "price": 2199.00, "stock": 35},
    {"category": "Accessories", "brand": "Daniel Wellington", "product_name": "Stainless Steel Bracelet", "price": 2599.00, "stock": 28},

    # Beauty & Personal Care
    {"category": "Beauty & Personal Care", "brand": "Nivea", "product_name": "Soft Moisturizing Cream 100ml", "price": 299.00, "stock": 70},
    {"category": "Beauty & Personal Care", "brand": "Maybelline", "product_name": "Matte Liquid Lipstick", "price": 649.00, "stock": 50},
    {"category": "Beauty & Personal Care", "brand": "Dove", "product_name": "Nourishing Shampoo 340ml", "price": 399.00, "stock": 65},
    {"category": "Beauty & Personal Care", "brand": "Gillette", "product_name": "Mach3 Razor with Cartridges", "price": 599.00, "stock": 55},
    {"category": "Beauty & Personal Care", "brand": "Lakme", "product_name": "Sunscreen Lotion SPF 50", "price": 449.00, "stock": 48},
]

for item in products:
    db.add(models.Product(**item))

db.commit()
db.close()

print(f"Seeded {len(products)} products across 5 categories successfully.")
