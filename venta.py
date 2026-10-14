from producto import Producto

class DetalleVenta:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad
        descuento_soles = producto.precio * (producto.descuento / 100)
        precio_final = producto.precio - descuento_soles
        self.subtotal = precio_final * cantidad

class Venta:
    def __init__(self, numero_venta: str):
        self.numero_venta = numero_venta
        self.detalles: list[DetalleVenta] = []
        self.total = 0.0

    def agregar_detalle(self, producto: Producto, cantidad: int):
        if cantidad <= 0 or producto.stock < cantidad:
            return False
        producto.stock -= cantidad
        nuevo_detalle = DetalleVenta(producto, cantidad)
        self.detalles.append(nuevo_detalle)
        self.total += nuevo_detalle.subtotal
        return True
