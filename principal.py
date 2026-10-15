from producto import Producto
from categoria import Categoria
from venta import Venta
from excepcion import StockInsuficienteError, ProductoExistenteError, ProductoNoExistenteError
from fabrica_producto import ProductoFactory

def buscar_producto(lista, id_producto):
    codigo_buscar = id_producto.strip().lower()
    for prod in lista:
        if prod.id_producto == codigo_buscar:
            return prod
    return None

def ejecutar_sistema():
    inventario_general = []
    categorias = [Categoria("cat-01", "perifericos"), Categoria("cat-02", "equipos"), Categoria("cat-03", "software")]
    ventas_del_dia = []
    contador_ventas = 1

    while True:
        print("\n=== Sistema NexusCore (Menu Base) ===")
        print("1. registrar producto")
        print("2. asignar categoria")
        print("3. consultar codigo")
        print("4. registrar venta")
        print("14. salir")
        opcion = input("opcion: ").strip()

        if opcion == "1":
            codigo = input("codigo: ").strip().lower()
            if any(p.id_producto == codigo for p in inventario_general):
                print("error: codigo ya existe.")
                continue
            nombre = input("nombre: ").strip().lower()
            try:
                precio = float(input("precio: "))
                stock = int(input("stock: "))
                descuento = float(input("descuento: "))
                caracteristicas = input("caracteristicas: ").strip().lower()
                tipo = input("tipo (1.equipo, 2.software, 3.accesorio): ").strip()
                dato_extra = input("dato especifico: ").strip()
                prod = ProductoFactory.crear_producto(tipo, codigo, nombre, stock, precio, caracteristicas, descuento, dato_extra)
                inventario_general.append(prod)
                print("registrado con exito.")
            except Exception as e:
                print(f"error: {e}")
        elif opcion == "14":
            break

ejecutar_sistema()
