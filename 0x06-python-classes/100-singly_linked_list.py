#!/usr/bin/python3
"""contains Node class"""


class Node:
    """Node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Constructor"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Singly linked list"""
    def __init__(self):
        """constructor"""
        self.__head = None

    def sorted_insert(self, value):
        node = Node(value)
        current = self.__head

        if self.__head is None:
            self.__head = node
        elif node.data < current.data:
            node.next_node = current
            self.__head = node
        else:
            while current.next_node:
                if node.data < current.next_node.data:
                    break
                current = current.next_node
            node.next_node = current.next_node
            current.next_node = node

    def __str__(self):
        text = ""
        current = self.__head
        while current:
            if current.next_node is None:
                text += str(current.data)
                current = current.next_node
            else:
                text += (str(current.data) + '\n')
                current = current.next_node
        return text
