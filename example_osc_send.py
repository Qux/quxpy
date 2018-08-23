from quxpy.osc_sender import OscSender
import random, time

sender = OscSender("127.0.0.1", 50000)

# simple way
sender.send("/foo", 0.1, 0.2)

# any nested params are available
params=[1, [2, 3] , ( [(4,5),6.2] ,7,8, "bar") ]
sender.send("/foo", params)
