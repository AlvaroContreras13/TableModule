# example_domain_logic.py
from domain_logic import Product

product = Product(1, "Laptop", 999.99)

print(f"Product ID: {product.product_id}, Name: {product.name}, Price: {product.price}")
