from clases.biblioteca import Biblioteca
from clases.libro import Libro 

def main():
    biblioteca = Biblioteca()

    libro1 = Libro("El Alquimista","Paulo Coelho",55)
    libro2 = Libro("Lo que el viento se llevo","Margaret Mitchell",20)
    libro3 = Libro("Papelucho Historiador","Marcela Paz",15)
    libro4 = Libro("Don Quijote de la Mancha","Miguel de Cervantes",66)

    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    biblioteca.mostrar_catalogo()

    print("---Solicitar Prestamos e Ingreso Devoluciones---")
    biblioteca.prestar_libro("Don Quijote")
    biblioteca.prestar_libro("Papelucho Historiador")

    biblioteca.mostrar_catalogo()

if __name__== "__main__":
    main()