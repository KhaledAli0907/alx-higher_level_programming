#!/usr/bin/python3
"""Singly likned linked class"""


class Node:
    """
    Class that defines properties Node.

    Attributes:
        data: data field of node."""

    def __init__(self, data, next_node=None):
        """
        Creates new instances of node.

        Args:
            __data : data field of node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self) -> int:
        """Retrieves the data field instance.

        Returns: the data field of a node."""
        return self.__data

    @property
    def next_node(self):
        """Retrives the next_node instance.

        Returns: The next_node instance."""
        return self.__next_node

    @data.setter
    def data(self, value: int):
        """Propery setter for data.

        Args:
            value (int): data field of a node.

        Raises:
            TypeError: data must be an integer"""
        if not (isinstance(value, int)):
            raise TypeError("data must be an integer")

        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Property setter for Node.

        Args:
            value (None): next node of a Node.

        Raises:
            TypeError: next_node must be a Node object ."""
        if not (isinstance(value, Node)) and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Class to the singly linked list"""

    def __init__(self):
        """Creates new instances of SinglyLinkedList .

        Args:
            __head : head of the SinglyLinkedList .
        """
        self.__head = None

    def __str__(self) -> str:
        """Represent the class object as a string"""
        temp_head = self.__head
        printed = []

        while temp_head:
            printed.sort()
            printed.append(str(temp_head.data))
            temp_head = temp_head.next_node

        printed.sort(key=int)
        return "\n".join(printed)

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted postion"""
        if self.__head is None:
            node = Node(value)
            node.next_node = self.__head
            self.__head = node
        else:
            node = Node(value)
            node.data = value
            node.next_node = self.__head
            self.__head = node
