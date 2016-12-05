class carta:
    def __init__(self, nombre, mazo):
        self.nombre = nombre

    def verCarta(self):
        return self.nombre

class mano:
     def __init__(self):
        self.cartas = [] #Array de objeto carta
    def verMano(self):
        return self.cartas
    def agregarCarta(self, carta):
        self.cartas.append(carta)
        return True
    def usarCarta(self, carta)
        return self.cartas.pop(self.cartas.index(carta))

class mazo:
    def __init__(self, cartas):
        self.cartas = cartas #Array de objeto carta
        self.descarte = []

    def cantidadMazo(self): #Cantidad de Cartas que quedan
        return self.cartas.len

    def cantidadDescarte(self): #CAntidad de Cartas en pila de descarte
        return self.descarte.len

    def shuffle(self): #Revolver las Cartas
        random.shuffle(self.cartas)
        return True

    def draw(self): #Robar Cartas
        return self.cartas.pop(0)

    def discard(self, carta): #Botar carta
        self.descarte.append(carta)
        return True

    def verDescarte(self): #Ver pila de descarte
        return self.descarte
