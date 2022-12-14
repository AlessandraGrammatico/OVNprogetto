import json
import numpy as np
import matplotlib.pyplot as plt

from Line import *
from SignalInformation import *

class Node(object):
    def __init__(self, node):
        self._label = node['label']  # string
        self._position = node['position']  # tuple (float, float)
        self._connected_nodes = node['connected_nodes']  # list [string]
        self._successive = {}  # dict [Line] - empty dict
        self._switching_matrix = None
        self._transceiver=''
    
    @property #lb6 fixedrate-flexrate-shannon
    def transceiver(self):
        return self._transceiver
    
    @transceiver.setter
    def transceiver(self, value):
        self._transceiver=value

    @property
    def switching_matrix(self):
        return self._switching_matrix

    @switching_matrix.setter
    def switching_matrix(self, value):
        self._switching_matrix = value

    @property
    def label(self):
        return self._label

    @property
    def position(self):
        return self._position

    @property
    def connected_nodes(self):
        return self._connected_nodes

    @property
    def successive(self):
        return self._successive

    @successive.setter
    def successive(self, value):
        self._successive = value

    #  update a signal information object modifying its path attribute
    #  and call the successive element  propagate method 
    def propagate(self, lightpath, occupation=False):
        path = lightpath.path  # signal information--> path
        if len(path) > 1:
            line_label = path[:2]  # the 1st and the 2nd element of path
            line = self.successive[line_label]
            lightpath.next()
            lightpath = line.propagate(lightpath, occupation)
        return lightpath
