from pythonosc import dispatcher, osc_server
import event

class OscReceiver:
    def __init__(self, port):
        self.dispatcher = dispatcher.Dispatcher()
        self.server = osc_server.ForkingOSCUDPServer(("127.0.0.1", port), self.dispatcher)

    def add(self, adr, func):
        event.add(adr, func)
        self.dispatcher.map(adr, event.bang)

    def start(self):
        self.server.serve_forever()
