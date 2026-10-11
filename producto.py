class Producto:
    def __init__(self, id_producto: str, nombre: str, stock: int, precio: float, caracteristicas: str, descuento: float):
        self.id_producto = id_producto.strip().lower()
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
        self.caracteristicas = caracteristicas
        self.descuento = descuento

    def obtener_info(self):
        return f"[{self.id_producto}] {self.nombre} | Stock: {self.stock} | Precio: S/. {self.precio:.2f}"

    def __str__(self):
        return f"[{self.id_producto}] {self.nombre}"
