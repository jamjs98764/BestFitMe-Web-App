"""Classes, tools and functions for constructing question graphs."""

import abc
import collections
import typing

from bestfit.recommender import DAG


T = typing.TypeVar("T")
S = typing.TypeVar("S")


class QuestionBase(typing.Generic[S, T]):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def classify_answer(self, answer) -> int:
        """
        Returns a response indicating the "class" of the answer.

        In a MCQ scenario, this would generally be the index
        of the answer. In more open-ended questions, it would
        mean some infered heriustics of the answer.

        There is no constraint on the type returned by the
        function, by it is required to be consistent throughout.
        """

    @abc.abstractmethod
    def total_answer_klasses(self) -> int:
        """
        Returns the number of possible answer classes.
        """


MCQQuestionBase = collections.namedtuple("MCQQuestionBase",
        ["name", "question", "description", "choices"])


class MCQQuestion(QuestionBase, MCQQuestionBase):

    def __new__(cls, *args, **kwargs):
        return MCQQuestionBase.__new__(cls, *args, **kwargs)

    def classify_answer(self, answer) -> int:
        return self.choices.index(answer)

    def total_answer_klasses(self):
        return len(self.choices)


class QuestionRule(object):

    def __init__(
            self,
            node: DAG.Node,
            question: QuestionBase,
            answer_mapping: typing.List[DAG.Node]):
        """
        Args:
            node: The node to bind this question to.
                  At this point, we assume that the graph
                  is already frozen. (i.e: It won't change any more).
            question: The QuestionBase object.
            answer_klass_to_node: The mapping of answer class
                                  to which node to look at next.
        """
        self._node = node
        self._question = question
        self._answer_mapping = answer_mapping

        # All of the answer mapping nodes
        for dest_node in answer_mapping:
            assert dest_node in node.children

        # make sure that all the destination childrens are covered.
        # If it isn't, that means there is probably something
        # wrong with out graph structure.

        for child in node.children:
            assert child in answer_mapping

    @property
    def question(self):
        return self._question

    def next_node(self, answer):
        return self._answer_mapping[self._question.classify_answer(answer)]


def register_rule(node: DAG.Node,
                  question: QuestionBase,
                  answer_mapping: typing.List[DAG.Node]):
    rule = QuestionRule(
            node=node, question=question, answer_mapping=answer_mapping)
    node.set_value(rule)


class QuestionGraphTransverser(DAG.Transverser):

    def __init__(self, node: DAG.Node):
        self._current_node = node
        self._path = []

    @property
    def current_node(self):
        return self._current_node

    @property
    def current_question(self) -> QuestionBase:
        return self._current_node.value.question

    def is_at_leaf(self):
        return self._current_node.is_leaf

    def transverse(self, answer):
        if self.is_at_leaf():
            return None

        next_node = self._current_node.value.next_node(answer)
        self._path.append((self._current_node.value.question,
                           answer))
        self._current_node = next_node
