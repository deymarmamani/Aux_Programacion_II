class Instrumento:
    def __init__(self, nombre: str, material: str, tipo: str):
        self.nombre = nombre
        self.__material = material
        self.__tipo = tipo
    def __str__(self):
        return f"Instrumento: {self.nombre}, Material: {self.__material}, Tipo: {self.__tipo}"
    def get_material(self):
        return self.__material
    def get_tipo(self):
        return self.__tipo
    def set_material(self, material: str):
        self.__material = material
    def set_tipo(self, tipo: str):
        if tipo in ["cuerdad", "aire"]:
            self.__tipo = tipo
inst1 = Instrumento("flauta", "Madera", "aire")

print(inst1)

print(inst1.get_material())

inst1.set_tipo("aire")
print(inst1)