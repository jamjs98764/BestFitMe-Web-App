"""Classes to model nodes in a DAG."""

import abc
import typing


T = typing.TypeVar("T")


def disabled_function(*args, **kwargs):
    raise AssertionError("Called a disabled function!")


class Node(typing.Generic[T]):
    """An abc representing a Node."""

    def __init__(self):
        self._children = []
        self._is_leaf = True

    @property
    def is_leaf(self):
        return self._is_leaf

    @property
    def children(self):
        return list(self._children)

    @property
    def value(self) -> T:
        return self._value

    def set_value(self, arg: T):
        self.set_value = disabled_function
        self._value = arg

    def add_child(self, node):
        self._children.append(node)
        self._is_leaf = False;

    def freeze_structure(self):
        self.add_child = disabled_function


class Transverser(object):
    """A object that transverses a tree."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def transverse(self, answer):
        """Move an edge in the graph."""

    @abc.abstractmethod
    def is_at_leaf(self) -> bool:
        """Returns True if the transverser is at a leaf node"""
