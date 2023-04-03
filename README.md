# productor_consumidor
El link de este repositorio es el siguiente: [GitHub](https://github.com/joseluis031/productor_consumidor.git)
## Explicacion del ejercicio

Este ejercicio consiste en la creacion de dos hilos, y que mientras uno de ellos
ejecute una accion, el otro va a estar ejecutando otra accion, la cual
depende del hilo anterior y la realizara de manera concurrente

## Codigo utilizado para la tarea
```
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
```
### Explicacion del codigo
He utilizado las librerias threading, time, random, y queue

Primero he creado la clase Productor, utilizando un bucle mediante el cual el productor ira creando productos; y he añadido los elementos a una cola a la que accedera la siguiente clase creada a traves del metodo .get()

Despues he creado la clase Consumidor, utilizando un bucle mediante el cual el consumidor ira consumiento productos, los cuales obtiene de la cola ya generada anteriormente 
--utilizo time.sleep para que el programa se pause un segundo cada vez que se genera o se consume un producto.

Por ultimo ejecutamos en paralelo las clases con el metodo .start y .join






### Ejecucion del codigo
```
Productor: ha producido el numero 3
Consumidor: ha consumido el numero 3
Productor: ha producido el numero 2
Consumidor: ha consumido el numero 2
Productor: ha producido el numero 7
Consumidor: ha consumido el numero 7
Productor: ha producido el numero 4
Consumidor: ha consumido el numero 4
Productor: ha producido el numero 2
Consumidor: ha consumido el numero 2
Productor: ha producido el numero 1
Consumidor: ha consumido el numero 1
Productor: ha producido el numero 4
Consumidor: ha consumido el numero 4
Productor: ha producido el numero 3
Consumidor: ha consumido el numero 3
Productor: ha producido el numero 3
Consumidor: ha consumido el numero 3
Productor: ha producido el numero 5
Consumidor: ha consumido el numero 5
Productor ha terminado de producir
Consumidor ha terminado de consumir
Programa terminado
```
