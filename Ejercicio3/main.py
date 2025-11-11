from clases.pedido import Pedido

def main():
    pedido = Pedido()

    pedido.agregar_item("Teclado", 25000, 2)
    pedido.agregar_item("Mouse", 3500, 1)
    pedido.agregar_item("Audifonos", 12000, 3)

    while True:
        print(" MENÚ PEDIDO ")
        print("1. Agregar ítem")
        print("2. Ver detalle del pedido")
        print("3. Ver total a pagar")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            nombre = input("Nombre del ítem: ").strip()
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                pedido.agregar_item(nombre, precio, cantidad)
            except ValueError:
                print(" Error: debes ingresar valores numéricos válidos.")

        elif opcion == "2":
            pedido.mostrar_items()

        elif opcion == "3":
            pedido.mostrar_items()
            pedido.mostrar_total()

        elif opcion == "4":
            print("Saliendo del sistema de pedidos.")
            break

        else:
            print(" Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()