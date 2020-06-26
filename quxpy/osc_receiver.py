from pythonosc import dispatcher, osc_server
from . import event

class OscReceiver:
    def __init__(self, port):
        self.dispatcher = dispatcher.Dispatcher()
        self.server = osc_server.ForkingOSCUDPServer(("127.0.0.1", port), self.dispatcher)

    def add(self, adr, func):
        event.add(adr, func)
        self.dispatcher.map(adr, event.bang)

    def start(self):
        self.server.serve_forever()

    def terminate(self):
        self.server.shutdown()


osc_receiver = None

def setup(port):
    global osc_receiver
    osc_receiver = OscReceiver(port)

def start():
    global osc_receiver
    osc_receiver.start()

def add(adr, func):
    global osc_receiver
    osc_receiver.add(adr, func)

def terminate():
    global osc_receiver
    osc_receiver.terminate()