import threading

events = {}
threads = []

def add(event_name, func):
    global events
    events[event_name] = func


def bang(event_name, *args):
    global events, jobs
    thread = threading.Thread(target=events[event_name],args=args)
    threads.append(thread)
    thread.start()


def close():
    for thread in threads:
        thread.join()
    print("All threads cleared.")
