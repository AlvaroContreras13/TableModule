from product_table_module import ProductTableModule

# Crear una instancia de ProductTableModule
product_module = ProductTableModule()

# Mostrar todos los productos
print("Lista de productos:")
products = product_module.get_all_products()
for product in products:
    print(f"{product['id']}: {product['name']} - ${product['price']}")

# Agregar un nuevo producto
print("\nAgregando un nuevo producto...")
product_module.add_product("Teclado", 50)

# Mostrar todos los productos después de agregar el nuevo producto
print("\nLista de productos después de agregar uno nuevo:")
products = product_module.get_all_products()
for product in products:
    print(f"{product['id']}: {product['name']} - ${product['price']}")

# Eliminar un producto
print("\nEliminando un producto...")
product_module.delete_product(1)

# Mostrar todos los productos después de eliminar uno
print("\nLista de productos después de eliminar uno:")
products = product_module.get_all_products()
for product in products:
    print(f"{product['id']}: {product['name']} - ${product['price']}")
