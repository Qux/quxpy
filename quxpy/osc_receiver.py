from pythonosc import dispatcher, osc_server
from . import thread_event as event

class OscReceiver:
    def __init__(self, port):
        self.dispatcher = dispatcher.Dispatcher()
        self.server = osc_server.ThreadingOSCUDPServer(("0.0.0.0", port), self.dispatcher)

    def add(self, adr, func):
        event.add(adr, func)
        self.dispatcher.map(adr, event.bang)

    def start(self):
        self.server.serve_forever()

    def terminate(self):
        self.server.shutdown()


receiver = None

def setup(port):
    global receiver
    receiver = OscReceiver(port)

def start():
    global receiver
    receiver.start()

def add(adr, func):
    global receiver
    receiver.add(adr, func)

def terminate():
    global receiver
    receiver.terminate()
    event.close()
