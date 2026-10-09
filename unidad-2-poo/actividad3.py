class Alumno:
    def __init__ (self, nombre, curso, nota ):
        self.nombre=nombre
        self.curso=curso
        self.nota=int(nota)

    def mostrar_datos(self):
        print(f"Nombre:{self.nombre}")
        print(f"Curso:{self.curso}")
        print(f"Nota:{self.nota}")

    def esta_aprobado(self):
        if self.nota>6:
            print("Aprobado")
        else:
            print("Desaprobado")

alumno1=Alumno("Karen", "7mo", "10")
alumno1.mostrar_datos()
alumno1.esta_aprobado()
