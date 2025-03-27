from time import sleep
from threading import *
class Hellow(Thread):
    def run(self):
        for i in range(5):
            print('Hellow',end=' ')
            sleep(2)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Hi')
            sleep(2)

t1=Hellow()
t2=Hi()
t1.start()
sleep(0.5)
t2.start()

t1.join()
t2.join()
print('Bye')