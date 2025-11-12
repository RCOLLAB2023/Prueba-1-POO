class Usuario:
    def __init__(self, nombre_usuario, clave):
        self.nombre_usuario = nombre_usuario
        self.clave = clave


class SistemaAutenticacion:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, nombre_usuario, clave):
        if self.buscar_usuario(nombre_usuario):
            print(f" El usuario '{nombre_usuario}' ya está registrado.")
        else:
            nuevo_usuario = Usuario(nombre_usuario, clave)
            self.usuarios.append(nuevo_usuario)
            print(f" Usuario '{nombre_usuario}' registrado exitosamente.")

    def buscar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre_usuario == nombre_usuario:
                return usuario
        return None

    def iniciar_sesion(self, nombre_usuario, clave):
        usuario = self.buscar_usuario(nombre_usuario)
        if usuario:
            if usuario.clave == clave:
                print(f"Acceso permitido. Bienvenido, {nombre_usuario}")
            else:
                print(f"Clave incorrecta para '{nombre_usuario}'.")
        else:
            print(f"El usuario '{nombre_usuario}' no existe.")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for usuario in self.usuarios:
                print(f" - {usuario.nombre_usuario}")
            print()