from producto import Producto

class Categoria:
    def __init__(self, id_categoria: str, nombre: str):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.productos: list[Producto] = []

    def registrar_producto(self, producto_nuevo: Producto):
        for producto_guardado in self.productos:
            if producto_guardado.id_producto == producto_nuevo.id_producto:
                print("el producto ya esta en la categoria.")
                return False
        self.productos.append(producto_nuevo)
        print(f"Producto '{producto_nuevo.nombre}' asignado a la categoria '{self.nombre}'.")
        return True

    def eliminar_producto(self, id_a_eliminar: str):
        codigo_buscar = id_a_eliminar.strip().lower()
        for producto_guardado in self.productos:
            if producto_guardado.id_producto == codigo_buscar:
                self.productos.remove(producto_guardado)
                print(f"Producto '{producto_guardado.nombre}' desvinculado de la categoria '{self.nombre}'.")
                return True
        return False
