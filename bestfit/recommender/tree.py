"""Classes to model nodes in a Q & A decision tree / forest."""

import abc


class NodeBase(object):
    """An abc representing a Node."""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def is_leaf(self) -> bool:
        """Returns true if the node is a leaf."""

    @abc.abstractmethod
    def parent(self) -> typing.optional[NodeBase]:
        """Returns the parent of this node."""


class QuestionNode(NodeBase):
    @abc.abstractmethod
    def next_node(self, answer) -> QuestionNode:
        """Returns the next node given an answer to a question."""

    @abc.abstractmethod
    def is_open_ended(self, answer) -> bool:
        """Returns true is the question is open-ended / subjective."""


class DecisionNode(NodeBase):
    def __init__(self, value):
        self._value = value

    @property
    def decision(self):
        return self._value
        
    def is_leaf(self):
        return True


class ObjectiveQuestion(ObjectiveQuestion):

    def __init__(self,
                 response_map: dict[Any, Any],
                 description: str,
                 question: str):
        self._response_map = response_map
        self._choices = response_map.keys()
        self._description = description
        self._question = question

    def question(self):
        return self._name

    def description(self):
        return self._description

    def next_node(self, answer):
        return self._choices[answer]


class Transverser(object):
    """A object that transverses a tree with memory."""

    def __init__(self, node):
        self._current_node = node  # type: NodeBase
        self._visited_nodes = []  # type: (QuestionNode, Any)

    @property
    def current_node(self):
        return self._current_node

    def next(self, answer) -> None:
        next_node = self._current_node.next_node(answer)
        self._visited_nodes.append((self._current_node, answer))
        self._current_node = next_node

    def is_done(self) -> bool:
        return self._current_node.is_leaf()

    def make_decision(self, decision_maker_func):
        if not self.is_done():
            raise RuntimeError("Cannot make decision until we have"
                               "transversed to the leaf of the tree")

        return decision_maker_func(self._visited_nodes)
