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
    
anime1 = Anime("Naruto", "Shonen", 5)

anime1.agregarEpisodeos("Episodio 1: El inicio de la aventura")
anime1.agregarEpisodeos("Episodio 2: El examen de los ninjas")
anime1.agregarEpisodeos("Episodio 3: El encuentro con el equipo")
anime1.agregarEpisodeos("Episodio 4: La batalla contra Zabuza")
anime1.agregarEpisodeos("Episodio 5: El despertar del poder")
print(anime1.mostrar_episodios())