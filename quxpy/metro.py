import threading
import time

events = []
jobs = []
thread = None
use_thread = False

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
                if use_thread:
                    job = threading.Thread(target=event["func"])
                    job.start()
                    jobs.append(job)
                else:
                    event["func"]()
                event["prev_time"] = now

def start(use_thread_for_each_event=False):    
    now = time.time()
    use_thread = use_thread_for_each_event
    for event in events:
        event["prev_time"] = now
    thread = threading.Thread(target=update)
    thread.start()



def terminate():
    if use_thread:
        for job in jobs:            
            job.join()
    
    thread.join()    
