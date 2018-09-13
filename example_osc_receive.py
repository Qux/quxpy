from quxpy import osc_receiver
import time

def foo(*args):
    time.sleep(2)
    print(args)

def bar(*args):
    print(args)

receiver = osc_receiver.OscReceiver(50001)
receiver.add("/bar", bar)
receiver.add("/foo", foo)

receiver.start()
