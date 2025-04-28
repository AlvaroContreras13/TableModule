from db_config import get_db_connection

class ProductTableModule:
    def __init__(self):
        self.connection = get_db_connection()

    def get_all_products(self):
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()

    def add_product(self, name, price):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (name, price))
        self.connection.commit()

    def delete_product(self, product_id):
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
