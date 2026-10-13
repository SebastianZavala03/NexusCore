from producto import Producto

class Categoria:
    def __init__(self, id_categoria: str, nombre: str):
        self.id_categoria = id_categoria
        self.nombre = nombre
        self.productos: list[Producto] = []
