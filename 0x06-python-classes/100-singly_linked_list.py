#!/usr/bin/python3

"""The Module Has Class 'Node'"""


class Node:
    """The Node Class for linked listed"""
    def __init__(self, data, next_node=None):
        """Initialize the Node object.
        Args:
            data (int) the data that the node carry
            next_node (node) the next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data property"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node property"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The linked list Class"""
    def __init__(self):
        """Inistialize the linked list object"""
        self.__head = None

    def __str__(self):
        re = ""
        tmp = self.__head
        while tmp:
            re += str(tmp.data)
            if tmp.next_node is not None:
                re += '\n'
            tmp = tmp.next_node
        return re

    def sorted_insert(self, value):
        tmp = None
        new = Node(value)
        head = self.__head
        if not self.__head or self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
            return
        while head:
            tmp = head.next_node
            if tmp is not None:
                if tmp.data > value:
                    head.next_node = new
                    new.next_node = tmp
                    break
                else:
                    head = tmp
                    continue
            else:
                if head.data < value:
                    head.next_node = new
                    new.next_node = None
                    break
                else:
                    tmp = head
                    head = new
                    new.next_node = tmp
                    tmp.next_node = None
                    break
