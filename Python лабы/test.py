from multiprocessing import Process, Event
import time

# Создаем событие 
event = Event() 

def worker():
    print("Рабочий в ожидании...")
    # Блокируем поток до срабатывания события
    event.wait()  
    print("Начал работу!")

def trigger():
    print("Запускаю сигнал")
    time.sleep(5)
    # Устанавливаем событие
    event.set()
    print("Сигнал запущен")
    
if __name__ == "__main__":
    
    # Запускаем процессы    
    trigger_process = Process(target=trigger)
    worker_process = Process(target=worker)
    
    trigger_process.start()
    worker_process.start()
    
    # Ждем завершения процессов  
    trigger_process.join()
    worker_process.join()
    event.set()