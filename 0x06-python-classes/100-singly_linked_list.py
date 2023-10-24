#!/usr/bin/python3
"""Singly likned linked class"""


class Node:
    """Node of a singly linked list"""

    def __init__(self, data, next_node=None) -> None:
        """Initilize the node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self) -> int:
        """Retrieve the data"""
        return self.__data

    @property
    def next_node(self):
        """Retrieve next node"""
        return self.__next_node

    @data.setter
    def data(self, value: int):
        """Set data in the node"""
        if not (isinstance(value, int)):
            raise TypeError("data must be an integer")

        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not (isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Class to the singly linked list"""

    def __init__(self) -> None:
        """Initlize the list with head arg"""
        self.__head = None

    def __str__(self):
        """Represents the class objects as a string.

        Returns: The class object represented as a string.
        """
        temp_var = self.__head
        print_node = []
        while temp_var:
            print_node.sort()
            print_node.append(str(temp_var.data))
            temp_var = temp_var.next_node

        print_node.sort(key=int)
        return "\n".join(print_node)

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted postion"""
        if self.__head == None:
            node = Node(value)
            node.next_node = self.__head
            self.__head = node
        else:
            node = Node(value)
            node.data = value
            node.next_node = self.__head
            self.__head = node
