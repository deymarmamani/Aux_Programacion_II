class Anime():
    def __init__(self, nombre: str, genero: str, nroEpisodios: int, episodios: list = []):
        self.nombre = nombre
        self.genero = genero
        self.__nroEpisodios = nroEpisodios
        self.__episodios = []
    def agregarEpisodeos(self, titulo):
        if len(self.__episodios) < self.__nroEpisodios:
            self.__episodios.append(titulo)
    def mostrar_episodios(self):
        return self.__episodios
    
anime1 = Anime("one piece", "Shonen", 1045)

anime1.agregarEpisodeos("Episodio 1: El inicio de la gran guerra pirata")
anime1.agregarEpisodeos("Episodio 2: El encuentro con el sombrero de paja")
anime1.agregarEpisodeos("Episodio 3: La búsqueda del tesoro legendario")
anime1.agregarEpisodeos("Episodio 4: La batalla contra los marines")
anime1.agregarEpisodeos("Episodio 5: El despertar del poder del rey de los piratas")
anime1.agregarEpisodeos("Episodio 6: La alianza con los nakamas")
anime1.agregarEpisodeos("Episodio 7: La lucha contra los shichibukai")
anime1.agregarEpisodeos("Episodio 8: La guerra en el archipiélago Sabaody")
anime1.agregarEpisodeos("Episodio 9: El enfrentamiento con los yonko")
anime1.agregarEpisodeos("Episodio 10: La búsqueda del One Piece")
#### No tiene final one piece, por lo tanto no se puede agregar más episodios :^]
print(anime1.mostrar_episodios())