#ejercicio productor y consumidor
import threading    #importo libreria threading
import time         #importo libreria time
import random       #importo libreria random
from queue import Queue #importo libreria queue

#definimos la clase productor
class Productor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self) #inicializo el hilo
        self.cola = cola #creo cola de numeros

    def run(self):
        for i in range(10): #genero 10 numeros aleatorios
            numero =(random.randint(1, 10))
            self.cola.put(numero)   #agrego numero a la cola
            print ("Productor: ha producido el numero {}" .format(numero))
            time.sleep(1)   #duermo el proceso por 1 segundo
        print ("Productor ha terminado de producir")

#definimos la clase consumidor
class Consumidor(threading.Thread):
    def __init__(self, cola):
        threading.Thread.__init__(self) #inicializo el hilo
        self.cola = cola    

    def run(self):
        for i in range(10): #bucle para consumir 10 numeros
            numero = self.cola.get()    #obtengo numero de la cola
            print ("Consumidor: ha consumido el numero {}" .format(numero))
            time.sleep(1)   #duermo el proceso por 1 segundo
        print ("Consumidor ha terminado de consumir")

#definimos la clase main
def main():
    cola = Queue()  #creo cola
    productor = Productor(cola) #creo productor
    consumidor = Consumidor(cola)   #creo consumidor
    productor.start()   #inicio productor
    consumidor.start()  #inicio consumidor
    productor.join()    #espero a que termine el productor
    consumidor.join()   #espero a que termine el consumidor
    
    print ("Programa terminado")    #imprimo mensaje de finalizacion de programa