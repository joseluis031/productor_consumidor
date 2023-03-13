#ejercicio productor y consumidor
import threading
import time
import random
from queue import Queue
import sys
import os
import signal

#definimos la clase productor
class Productor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self)
        self.cola = cola

    def run(self):
        for i in range(10):
            numero = random.randint(1, 10)
            self.cola.put(numero)
            print ("Productor: %s ha producido el numero %s" % (self.getName(), numero))
            time.sleep(1)
        print ("Productor: %s termina" % self.getName())

#definimos la clase consumidor
class Consumidor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self)
        self.cola = cola

    def run(self):
        for i in range(10):
            numero = self.cola.get()
            print ("Consumidor: %s ha consumido el numero %s" % (self.getName(), numero))
            time.sleep(1)
        print ("Consumidor: %s termina" % self.getName())

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

if __name__ == "__main__":
    main()