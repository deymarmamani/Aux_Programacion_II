class Televisor:
    def __init__(self, marcar: str, resolucion: int, tipo: str):
        self.__marcar = marcar
        self.__resolucion = resolucion
        self.__tipo = tipo

    def __str__(self):
        return f"Marca: {self.__marcar}, Resolución: {self.__resolucion} pulgadas, Tipo: {self.__tipo}"
tv1 = Televisor("LG", 55, "OLED")
print(tv1)