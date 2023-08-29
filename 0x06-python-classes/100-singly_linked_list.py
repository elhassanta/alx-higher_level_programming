#!/usr/bin/python3
class Node:

    def __init__(self, data, next_node=None):
        self.data = data

    def data(self):
        return self.data

    def def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.data = value

    def next_node(self):
        return self.next_node

    def next_node(self, value):
        if value is not None or not isinstance(value, self.Node):
            raise TypeError("next_node must be a Node object")
        self.next_node = value
