from clases.contacto import Agenda

def main():
    agenda = Agenda()

    
    agenda.agregar_contacto("Rocio Gonzalez", "984523210", "romundo@gmail.com")
    agenda.agregar_contacto("Dominga Mattheos", "955887798", "doma@gmail.com")
    agenda.agregar_contacto("Phillip Parra", "956988963", "phillp@gmail.com")

    while True:
        print(" MENÚ AGENDA ")
        print("1 Ver todos los contactos")
        print("2 Agregar nuevo contacto")
        print("3 Buscar contacto por nombre")
        print("4 Eliminar contacto")
        print("5 Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agenda.mostrar_contactos()

        elif opcion == "2":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            agenda.agregar_contacto(nombre, telefono, correo)

        elif opcion == "3":
            nombre = input(" Ingrese nombre contacto: ")
            contacto = agenda.buscar_contacto(nombre)
            if contacto:
                print(f"Contacto encontrado: {contacto.nombre}, {contacto.telefono} , {contacto.correo}")
            else:
                print(f" No se encontró el contacto '{nombre}'.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre a eliminar: ")
            agenda.eliminar_contacto(nombre)

        elif opcion == "5":
            print(" Salisteo de la agenda.")
            break

        else:
            print("Opción no válida, Reintente.")
if __name__ == "__main__":
    main()
