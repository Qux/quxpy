# coding=utf-8
#
# python-osc ( https://pypi.org/project/python-osc/ ) is required.
#



from pythonosc import osc_message_builder, udp_client
from . list_util import flatter

class OscSender:
    def __init__(self, host, port):
        self.client = udp_client.SimpleUDPClient(host, port)

    def send(self, address, *args):
        msg = osc_message_builder.OscMessageBuilder(address=address)

        args = flatter(args)

        for arg in args:
            msg.add_arg(arg)

        msg = msg.build()

        self.client.send(msg)
