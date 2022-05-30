from asyncore import poll
import threading
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

events = []
metro_loop = None
executor = None

__poll_interval = 0.001

def add(func, interval):
    event = {
        "func":func,
        "interval": interval,
        "prev_time": time.time(),
    }

    events.append(event)

def update():
    for event in events:
        now = time.time()
        diff = now - event["prev_time"]
        
        if event["interval"] < diff:                        
            executor.submit(event["func"])
            event["prev_time"] = now

def update_loop():    
    global __poll_interval
    while True:    
        try:      
            update()
            time.sleep(__poll_interval)
        except Exception:
            break

def start(use_process=False, num_processes=None, reset_timer=True, poll_interval=0.0):  
    global executor, __poll_interval
    if use_process:
        executor = ProcessPoolExecutor(max_workers=num_processes)
    else:
        executor = ThreadPoolExecutor(max_workers=num_processes)
    
    if reset_timer:
        now = time.time()
        for event in events:
            event["prev_time"] = now

    if 0.0 < poll_interval:
        __poll_interval = poll_interval
    
    global metro_loop
    metro_loop = threading.Thread(target=update_loop)

    metro_loop.start()


def terminate():
    executor.shutdown()
    metro_loop.join()    