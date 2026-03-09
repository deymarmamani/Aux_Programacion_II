#Dada la clase aula se tiene los siguientes atributos, nombre de aula, piso en el que se encuentra, y una matriz de estudiantes y sus notas
#a) Sobrecargar un método para:
#i) Mostrar todos los datos del aula.
#ii) Mostrar a los estudiantes con un mensaje de “APROBADO”, “REPROBADO”, con respecto a la nota obtenida.
class Aula:
    def __init__(self, nombre_de_aula, piso, estudiantes):
        self.nombre = nombre_de_aula
        self.piso = piso
        self.estudiantes = estudiantes

    def mostrar_datos(self):
        print(f"Aula: {self.nombre}")
        print(f"Piso: {self.piso}")
        print("Estudiantes y sus notas:")
        for estudiante, nota in self.estudiantes.items():
            print(f"{estudiante}: {nota}")

    def mostrar_aprobados_reprobados(self):
        print("Estudiantes con su estado de aprobación:")
        for estudiante, nota in self.estudiantes.items():
            estado = "APROBADO" if nota >= 60 else "REPROBADO"
            print(f"{estudiante}: {estado}")

estudiantes = {"Deymar": 85, "Daniel": 55, "Mijail": 70, "Israel": 45}
aula = Aula("Aula 101", 1, estudiantes)
aula.mostrar_datos()
aula.mostrar_aprobados_reprobados()
