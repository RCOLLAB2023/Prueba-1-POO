class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.alumnos = []

    def inscribir_alumno(self, nombre):
        if nombre not in self.alumnos:
            self.alumnos.append(nombre)
            print(f" Alumno '{nombre}' inscrito en {self.nombre}.")
        else:
            print(f" El alumno '{nombre}' ya está inscrito.")

    def eliminar_alumno(self, nombre):
        if nombre in self.alumnos:
            self.alumnos.remove(nombre)
            print(f" Alumno '{nombre}' eliminado.")
        else:
            print(f" No se encontró el alumno '{nombre}' en el curso.")

    def listar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos inscritos.")
        else:
            print(f"Alumnos inscritos en {self.nombre}:")
            for a in self.alumnos:
                print(f"- {a}")

    def mostrar_estado(self):
        print(f" Curso: {self.nombre}")
        print(f"Total de alumnos: {len(self.alumnos)}")
