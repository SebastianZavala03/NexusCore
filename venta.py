from producto import Producto
from excepcion import StockInsuficienteError

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
        if cantidad <= 0:
            raise StockInsuficienteError(f"La cantidad a vender de {producto.nombre} debe ser mayor a 0.")
        if producto.stock < cantidad:
            raise StockInsuficienteError(f"Stock insuficiente para {producto.nombre}. Stock actual: {producto.stock}")
        producto.stock -= cantidad
        nuevo_detalle = DetalleVenta(producto, cantidad)
        self.detalles.append(nuevo_detalle)
        self.total += nuevo_detalle.subtotal
        return True
