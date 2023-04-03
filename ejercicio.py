#ejercicio productor y consumidor
import threading
import time
import random
from queue import Queue


#definimos la clase productor
class Productor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self)
        self.cola = cola

    def run(self):
        for i in range(10):
            numero =(random.randint(1, 10)) #este es L[0]

            self.cola.put(numero)
            print ("Productor: ha producido el numero {}" .format(numero))
            time.sleep(1)
        print ("Productor ha terminado de producir")

#definimos la clase consumidor
class Consumidor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self)
        self.cola = cola

    def run(self):
        for i in range(10):
            numero = self.cola.get()
            print ("Consumidor: ha consumido el numero {}" .format(numero))
            time.sleep(1)
        print ("Consumidor ha terminado de consumir")

#definimos la clase main
def main():
    cola = Queue()
    productor = Productor(cola)
    consumidor = Consumidor(cola)
    productor.start()
    consumidor.start()
    productor.join()
    consumidor.join()
    
    print ("Programa terminado")