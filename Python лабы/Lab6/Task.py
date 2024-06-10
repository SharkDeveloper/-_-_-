from time import sleep
from multiprocessing import Process, Event

evt = Event()

def worker():
    print("Worker: (Отдыхает)...")
    print(evt.is_set())
    evt.wait()
    print("Опять работа!")

def director():
    sleep(5)
    print("Director: Перекур закончился, пора работать!")
    evt.set()
    print(evt.is_set())
    

if __name__=="__main__":
    wrkr = Process(target=worker)
    drctr = Process(target=director)

    wrkr.start()  
    drctr.start() 

    wrkr.join() 
    drctr.join()    



    
    
    
