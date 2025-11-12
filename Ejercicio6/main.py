from clases.usuario import SistemaAutenticacion

def main():
    sistema = SistemaAutenticacion()

    
    sistema.registrar_usuario("Rocio", "1234")
    sistema.registrar_usuario("Seller1", "C.25.fr")
    sistema.registrar_usuario("user", "0100")

    
    sistema.registrar_usuario("Seller1", "xyz2")  # ya existe

    sistema.iniciar_sesion("Rocio", "1234")       
    sistema.iniciar_sesion("Rocio", "7777")       
    sistema.iniciar_sesion("usuaria2", "5324")   

   
    sistema.mostrar_usuarios()

    while True:
        print(" MENU DE ACCESO ")
        print("1 Registrar nuevo usuario")
        print("2 Iniciar sesión")
        print("3 Ver usuarios registrados")
        print("4 Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre de usuario: ")
            clave = input("Ingrese clave: ")
            sistema.registrar_usuario(nombre, clave)

        elif opcion == "2":
            nombre = input("Ingrese nombre de usuario: ")
            clave = input("Ingrese clave: ")
            sistema.iniciar_sesion(nombre, clave)

        elif opcion == "3":
            sistema.mostrar_usuarios()

        elif opcion == "4":
            print(" Saliste del sistema.")
            break

        else:
            print(" Opción no válida, intente nuevamente.")


if __name__ == "__main__":
    main()