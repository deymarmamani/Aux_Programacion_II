# Ejercicio 4. Realiza la abstracción de un Bus.
# a) Al bus desean subir X cantidad de pasajeros, actualiza los datos del bus.
# b) Crea un método para cobrar pasaje a los pasajeros. (Costo del pasaje: bs. 1.50)
# c) Muestra cuántos asientos quedan disponibles.
# d) Crea una instancia del bus y utiliza los métodos de los incisos anteriores.

class Bus:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pasajeros = 0
        self.recaudacion = 0.0

    def subir_pasajeros(self, cantidad):
        if self.pasajeros + cantidad <= self.capacidad:
            self.pasajeros += cantidad
            print(f"{cantidad} pasajeros han subido al bus.")
        else:
            print("No hay suficiente espacio para todos los pasajeros.")
    def cobrar_pasaje(self):
        costo_pasaje = 1.50
        total_cobrado = self.pasajeros * costo_pasaje
        self.recaudacion += total_cobrado
        print(f"Se ha cobrado un total de Bs. {total_cobrado:.2f} por los pasajes.")
    def asientos_disponibles(self):
        disponibles = self.capacidad - self.pasajeros
        print(f"Quedan {disponibles} asientos disponibles.")


bus = Bus(capacidad=50)
bus.subir_pasajeros(25)
bus.cobrar_pasaje()
bus.asientos_disponibles()
