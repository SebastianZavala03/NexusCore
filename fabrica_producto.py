from producto import Producto, Equipo, Software, Accesorio

class ProductoFactory:

    @classmethod
    def crear_producto(cls, tipo, codigo, nombre, stock, precio, caracteristicas, descuento, dato_extra=None):
        if tipo == "1":
            return Equipo(codigo, nombre, stock, precio, caracteristicas, descuento, dato_extra)
        elif tipo == "2":
            return Software(codigo, nombre, stock, precio, caracteristicas, descuento, dato_extra)
        elif tipo == "3":
            return Accesorio(codigo, nombre, stock, precio, caracteristicas, descuento, dato_extra)
        else:
            raise ValueError(f"Tipo de producto '{tipo}' no valido. Opciones: 1 (Equipo), 2 (Software), 3 (Accesorio).")