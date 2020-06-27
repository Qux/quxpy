import threading
import time

events = []
thread = None

def add(func, interval):
    event = {
        "func":func,
        "interval": interval,
        "prev_time": 0
    }

    events.append(event)


def update():    
    while True:        
        for event in events:
            now = time.time()
            diff = now - event["prev_time"]
            
            if event["interval"] < diff:
                event["func"]()
                event["prev_time"] = now

def start():    
    thread = threading.Thread(target=update)
    thread.start()

def terminate():
    thread.terminate()
    thread.join()    
