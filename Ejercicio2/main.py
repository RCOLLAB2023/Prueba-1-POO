from clases.curso import Curso

def main():
        nombre_curso = input("Nombre del curso a crear: ").strip()
        curso = curso(nombre_curso)

        curso.inscribir_alumno("Rocio Gonzalez")
        curso.inscribir_alumno("Phillip Parra")
        curso.inscribir_alumno("Dominga Mattheos")

while True:
        print("\n=== MENÚ CURSO ===")
        print("1. Inscribir alumno")
        print("2. Eliminar alumno")
        print("3. Listar alumnos")
        print("4. Consultar estado del curso")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            nombre = input("Nombre del alumno a inscribir: ")
            Curso.inscribir_alumno(nombre)
        elif opcion == "2":
            nombre = input("Nombre del alumno a eliminar: ")
            Curso.eliminar_alumno(nombre)
        elif opcion == "3":
            Curso.listar_alumnos()
        elif opcion == "4":
            Curso.mostrar_estado()
        elif opcion == "5":
            print("Saliendo.")
            break
        else:
            print(" Opción inválida, intenta nuevamente.")

if __name__ == "__main__":
    main()
          


