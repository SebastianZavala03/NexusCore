from excepcion import StockInsuficienteError

class Producto:
    def __init__(self, id_producto: str, nombre: str, stock: int, precio: float, caracteristicas: str, descuento: float):
        if stock < 0:
            raise StockInsuficienteError(f"El stock de {nombre} no puede ser menor a 0.")
        if precio <= 0:
            raise StockInsuficienteError(f"El precio de {nombre} debe ser mayor a 0.")
        if descuento < 0 or descuento > 100:
            raise StockInsuficienteError(f"El descuento de {nombre} debe estar entre 0 y 100.")

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


class Equipo(Producto):
    def __init__(self, id_producto: str, nombre: str, stock: int, precio: float, caracteristicas: str, descuento: float, sistema_operativo: str):
        super().__init__(id_producto, nombre, stock, precio, caracteristicas, descuento)
        self.sistema_operativo = sistema_operativo

    def obtener_info(self):
        return f"[{self.id_producto}] {self.nombre} | Stock: {self.stock} | Precio: S/. {self.precio:.2f} | SO: {self.sistema_operativo}"


class Software(Producto):
    def __init__(self, id_producto: str, nombre: str, stock: int, precio: float, caracteristicas: str, descuento: float, meses_licencia: int):
        super().__init__(id_producto, nombre, stock, precio, caracteristicas, descuento)
        if meses_licencia <= 0:
            raise StockInsuficienteError(f"La licencia para {nombre} debe ser mayor a 0 meses.")
        self.meses_licencia = meses_licencia

    def obtener_info(self):
        return f"[{self.id_producto}] {self.nombre} | Stock: {self.stock} | Precio: S/. {self.precio:.2f} | Licencia: {self.meses_licencia} meses"


class Accesorio(Producto):
    def __init__(self, id_producto: str, nombre: str, stock: int, precio: float, caracteristicas: str, descuento: float, compatibilidad: str):
        super().__init__(id_producto, nombre, stock, precio, caracteristicas, descuento)
        self.compatibilidad = compatibilidad

    def obtener_info(self):
        return f"[{self.id_producto}] {self.nombre} | Stock: {self.stock} | Precio: S/. {self.precio:.2f} | Compatible con: {self.compatibilidad}"
