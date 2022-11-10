from Node import *

class Connection(object):
    def __init__(self, in_node, out_node, s_power):
        self._in_node = in_node #string
        self._out_node = out_node #string
        self._sig_power = s_power #float
        self._latency = 0 #float
        self._snr = 0 #float
        self._rb = 0

    @property
    def bit_rate(self):
        return self._rb

    @bit_rate.setter
    def bit_rate(self, value):
        self._rb = value

    @property
    def in_node(self):
        return self._in_node

    @property
    def out_node(self):
        return self._out_node

    @property
    def signal_power(self):
        return self._sig_power

    @property
    def latency(self):
        return self._latency

    @latency.setter
    def latency(self, value):
        self._latency = value

    @property
    def snr(self):
        return self._snr

    @snr.setter
    def snr(self, value):
        self._snr = value
