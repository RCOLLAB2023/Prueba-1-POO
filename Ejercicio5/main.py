from clases.pelicula import Pelicula,Catalogo

def main():
    catalogo = Catalogo()

    
    catalogo.agregar_pelicula(Pelicula("El Conjuro", "Terror", 2013))
    catalogo.agregar_pelicula(Pelicula("Mujer Bonita", "Romance", 1990))
    catalogo.agregar_pelicula(Pelicula("Los ilusionistas 2", "thriller", 2013))
    catalogo.agregar_pelicula(Pelicula("Mision Imposible 2", "Ciencia Ficcion", 2000))

    while True:
        print(" MENÚ CATÁLOGO PELICULAS")
        print("1 Ver catálogo completo")
        print("2 Buscar película por título")
        print("3 Filtrar películas por género")
        print("4 Agregar nueva película")
        print("5 Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            catalogo.mostrar_catalogo()

        elif opcion == "2":
            titulo = input("Ingrese el título de la película a buscar: ")
            catalogo.buscar_por_titulo(titulo)

        elif opcion == "3":
            genero = input("Ingrese el género a filtrar: ")
            catalogo.filtrar_por_genero(genero)

        elif opcion == "4":
            titulo = input("Título: ")
            genero = input("Género: ")
            try:
                anio = int(input("Año de lanzamiento: "))
                catalogo.agregar_pelicula(Pelicula(titulo, genero, anio))
                print(f"'{titulo}' agregada correctamente al catálogo.")
            except ValueError:
                print(" Año inválido. Intente nuevamente.")

        elif opcion == "5":
            print(" Saliste del Catalogo")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()