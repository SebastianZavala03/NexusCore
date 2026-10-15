from producto import Producto
from categoria import Categoria
from venta import Venta
from excepcion import (
    StockInsuficienteError,
    ProductoExistenteError,
    ProductoNoExistenteError
)
from fabrica_producto import ProductoFactory


def buscar_producto(lista, id_producto):
    codigo_buscar = id_producto.strip().lower()
    for prod in lista:
        if prod.id_producto == codigo_buscar:
            return prod
    return None


def ejecutar_sistema():
    inventario_general = []

    categorias = []
    cat1 = Categoria("cat-01", "perifericos")
    cat2 = Categoria("cat-02", "equipos")
    cat3 = Categoria("cat-03", "software")

    categorias.append(cat1)
    categorias.append(cat2)
    categorias.append(cat3)

    ventas_del_dia = []
    contador_ventas = 1

    while True:
        print("\n=======================================")
        print("Sistema NexusCore")
        print("=======================================")
        print("1.  - registrar producto")
        print("2.  - asignar categoria")
        print("3.  - consultar codigo")
        print("4.  - registrar venta")
        print("5.  - ingresar mercaderia")
        print("6.  - modificar producto")
        print("7.  - bajo stock")
        print("8.  - en promocion")
        print("9.  - catalogo por categoria")
        print("10. - desvincular categoria")
        print("11. - eliminar producto")
        print("12. - ventas del dia")
        print("13. - valor total inventario")
        print("14. - salir del sistema")

        opcion = input("seleccione una opcion del menu: ").strip()

        if opcion == "1":
            print("\n--- registrar producto ---")
            codigo = input("codigo: ").strip().lower()

            if any(prod.id_producto == codigo for prod in inventario_general):
                print("error: ya existe un producto con ese codigo.")
                continue

            nombre = input("nombre: ").strip().lower()

            try:
                precio = float(input("precio (s/.): "))
                stock = int(input("stock inicial: "))
                descuento = float(input("descuento (%): "))
            except ValueError:
                print("error: ingrese numeros validos.")
                continue

            caracteristicas = input("caracteristicas: ").strip().lower()

            print("tipo: 1. equipo | 2. software | 3. accesorio")
            tipo = input("seleccione tipo: ").strip()

            dato_extra = None
            if tipo == "1":
                dato_extra = input("sistema operativo: ").strip().lower()
            elif tipo == "2":
                try:
                    dato_extra = int(input("meses de licencia: "))
                except ValueError:
                    dato_extra = 12
            elif tipo == "3":
                dato_extra = input("compatibilidad: ").strip().lower()

            try:
                nuevo_producto = ProductoFactory.crear_producto(
                    tipo, codigo, nombre, stock, precio, caracteristicas, descuento, dato_extra
                )
                inventario_general.append(nuevo_producto)
                print("producto registrado con exito.")
            except (StockInsuficienteError, ValueError) as error:
                print(f"error al registrar: {error}")

        elif opcion == "2":
            print("\n--- asignar categoria ---")
            if not inventario_general:
                print("el inventario esta vacio.")
                continue

            print("productos disponibles:")
            for prod in inventario_general:
                print(f"- {prod.id_producto} | {prod.nombre}")

            cod = input("codigo del producto: ").strip().lower()
            prod_encontrado = buscar_producto(inventario_general, cod)

            if not prod_encontrado:
                print("error: no existe ningun producto con ese codigo.")
                continue

            print("\ncategorias disponibles:")
            for cat in categorias:
                print(f"- [{cat.id_categoria}] {cat.nombre}")

            entrada_cat = input("ingrese el codigo o nombre de la categoria: ").strip().lower()

            cat_encontrada = None
            for cat in categorias:
                if cat.id_categoria == entrada_cat or cat.nombre == entrada_cat:
                    cat_encontrada = cat
                    break

            if cat_encontrada:
                try:
                    cat_encontrada.registrar_producto(prod_encontrado)
                except ProductoExistenteError as error:
                    print(f"error: {error}")
            else:
                print("categoria no encontrada.")

        elif opcion == "3":
            print("\n--- consultar producto ---")
            cod = input("codigo a buscar: ").strip().lower()
            prod = buscar_producto(inventario_general, cod)

            if not prod:
                print("error: no existe ningun producto con ese codigo.")
            else:
                print(f"detalle: {prod.obtener_info()}")
                print(f"caracteristicas: {prod.caracteristicas}")
                print(f"descuento: {prod.descuento}%")

        elif opcion == "4":
            print("\n--- registrar venta ---")
            cod = input("codigo del producto: ").strip().lower()
            prod = buscar_producto(inventario_general, cod)

            if not prod:
                print("error: no existe ningun producto con ese codigo.")
                continue

            try:
                cantidad = int(input(f"cantidad a vender (stock actual: {prod.stock}): "))
            except ValueError:
                print("error: ingrese un numero entero.")
                continue

            id_venta = f"v-{contador_ventas:03d}"
            nueva_venta = Venta(id_venta)

            try:
                nueva_venta.agregar_detalle(prod, cantidad)
                ventas_del_dia.append(nueva_venta)
                contador_ventas += 1
                print(f"venta realizada. total: s/. {nueva_venta.total:.2f}")
                print(f"stock restante de {prod.nombre}: {prod.stock}")
            except StockInsuficienteError as error:
                print(f"error en la venta: {error}")

        elif opcion == "5":
            print("\n--- ingresar mercaderia ---")
            cod = input("codigo del producto: ").strip().lower()
            prod = buscar_producto(inventario_general, cod)

            if not prod:
                print("error: no existe ningun producto con ese codigo.")
                continue

            try:
                ingreso = int(input("cantidad a ingresar: "))
                if ingreso <= 0:
                    raise StockInsuficienteError("la cantidad a ingresar debe ser mayor a 0.")
                prod.stock += ingreso
                print(f"nuevo stock de {prod.nombre}: {prod.stock}")
            except ValueError:
                print("error: ingrese un numero valido.")
            except StockInsuficienteError as error:
                print(f"error: {error}")

        elif opcion == "6":
            print("\n--- modificar producto ---")
            cod = input("codigo del producto: ").strip().lower()
            prod = buscar_producto(inventario_general, cod)

            if not prod:
                print("error: no existe ningun producto con ese codigo.")
                continue

            nuevo_nombre = input("nuevo nombre (enter para no cambiar): ").strip().lower()
            if nuevo_nombre != "":
                prod.nombre = nuevo_nombre

            nuevo_precio = input("nuevo precio (enter para no cambiar): ").strip()
            if nuevo_precio != "":
                try:
                    val_p = float(nuevo_precio)
                    if val_p <= 0:
                        raise StockInsuficienteError("el precio debe ser mayor a 0.")
                    prod.precio = val_p
                except ValueError:
                    print("precio no valido, se mantuvo el anterior.")
                except StockInsuficienteError as error:
                    print(f"error: {error}")

            print("producto actualizado con exito.")

        elif opcion == "7":
            print("\n--- bajo stock (3 o menos) ---")
            hay_datos = False
            for prod in inventario_general:
                if prod.stock <= 3:
                    print(f"- {prod.id_producto} | {prod.nombre} | stock: {prod.stock}")
                    hay_datos = True
            if not hay_datos:
                print("no hay productos con bajo stock.")

        elif opcion == "8":
            print("\n--- en promocion ---")
            hay_datos = False
            for prod in inventario_general:
                if prod.descuento > 0:
                    descuento_soles = prod.precio * (prod.descuento / 100)
                    oferta = prod.precio - descuento_soles
                    print(f"- {prod.id_producto} | {prod.nombre} | precio oferta: s/. {oferta:.2f} (-{prod.descuento}%)")
                    hay_datos = True
            if not hay_datos:
                print("no hay productos en promocion.")

        elif opcion == "9":
            print("\n--- catalogo por categoria ---")
            for cat in categorias:
                print(f"- [{cat.id_categoria}] {cat.nombre}")

            entrada_cat = input("ingrese el codigo o nombre de la categoria: ").strip().lower()

            cat_seleccionada = None
            for cat in categorias:
                if cat.id_categoria == entrada_cat or cat.nombre == entrada_cat:
                    cat_seleccionada = cat
                    break

            if cat_seleccionada:
                print(f"\ncategoria: {cat_seleccionada.nombre}")
                if not cat_seleccionada.productos:
                    print("sin productos asignados todavia.")
                else:
                    for prod in cat_seleccionada.productos:
                        print(f"- {prod.id_producto} | {prod.nombre} | s/. {prod.precio:.2f} | stock: {prod.stock}")
            else:
                print("categoria no encontrada.")

        elif opcion == "10":
            print("\n--- desvincular de categoria ---")
            cod = input("codigo del producto: ").strip().lower()
            desvinculado = False
            for cat in categorias:
                try:
                    cat.eliminar_producto(cod)
                    desvinculado = True
                    break
                except ProductoNoExistenteError:
                    continue

            if not desvinculado:
                print("el producto no estaba en ninguna categoria.")

        elif opcion == "11":
            print("\n--- eliminar producto ---")
            cod = input("codigo del producto a eliminar: ").strip().lower()
            prod = buscar_producto(inventario_general, cod)

            if not prod:
                print("error: no existe ningun producto con ese codigo.")
                continue

            confirmar = input(f"¿eliminar '{prod.nombre}'? (s/n): ").strip().lower()
            if confirmar == "s":
                inventario_general.remove(prod)
                for cat in categorias:
                    try:
                        cat.eliminar_producto(prod.id_producto)
                    except ProductoNoExistenteError:
                        pass
                print("producto eliminado con exito.")

        elif opcion == "12":
            print("\n--- ventas del dia ---")
            if not ventas_del_dia:
                print("no hay ventas registradas.")
            else:
                total_dia = 0.0
                for v in ventas_del_dia:
                    total_dia += v.total
                print(f"total recaudado: s/. {total_dia:.2f}")
                for v in ventas_del_dia:
                    print(f"venta: {v.numero_venta} | total: s/. {v.total:.2f}")

        elif opcion == "13":
            print("\n--- valor total inventario ---")
            total_unidades = 0
            valor_total = 0.0
            for prod in inventario_general:
                total_unidades += prod.stock
                valor_total += prod.stock * prod.precio
            print(f"valor en mercaderia: s/. {valor_total:,.2f}")
            print(f"total unidades: {total_unidades}")
            print(f"total productos: {len(inventario_general)}")

        elif opcion == "14":
            break




ejecutar_sistema()
