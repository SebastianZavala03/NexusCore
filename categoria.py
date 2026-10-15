from producto import Producto
from excepcion import ProductoExistenteError, ProductoNoExistenteError

class Categoria:
    def __init__(self, id_categoria: str, nombre: str):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.productos: list[Producto] = []

    def registrar_producto(self, producto_nuevo: Producto):
        for producto_guardado in self.productos:
            if producto_guardado.id_producto == producto_nuevo.id_producto:
                raise ProductoExistenteError(f"El producto '{producto_nuevo.nombre}' ya pertenece a la categoria '{self.nombre}'.")
        self.productos.append(producto_nuevo)
        print(f"Producto '{producto_nuevo.nombre}' asignado a la categoria '{self.nombre}'.")

    def eliminar_producto(self, id_a_eliminar: str):
        codigo_buscar = id_a_eliminar.strip().lower()
        for producto_guardado in self.productos:
            if producto_guardado.id_producto == codigo_buscar:
                self.productos.remove(producto_guardado)
                print(f"Producto '{producto_guardado.nombre}' desvinculado de la categoria '{self.nombre}'.")
                return True
        raise ProductoNoExistenteError(f"No se encontro el producto con codigo '{id_a_eliminar}' en '{self.nombre}'.")
