import abc
import collections
import typing

from bestfit.recommender import DAG


T = TypeVar("T")
S = TypeVar("S")


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
    @property
    def total_answer_klasses(self) -> int:
        """
        Returns the number of possible answer classes.
        """


MCQQuestionBase = collections.namedtuple("MCQQuestionBase",
        ["name", "description", "choices"])


class MCQQuestion(QuestionBase, MCQQuestionBase):

    def classify_answer(self, answer) -> int:
        return self.choices.index(answer)

    def total_answer_klasses(self):
        return len(self.choices)



class QuestionRule(object):
    def __init__(
            self,
            node: DAG.Node,
            question: Question,
            answer_mapping: dict[int, Node]):
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
        for answer_klass, dest_node in answer_mapping:
            assert dest_node in node.children
            assert answer_klass >= 0
            assert answer_klass < question.total_answer_klasses

        dest_nodes = set(dest_node for _, dest_node in answer_mapping)
        
        # make sure that all the destination childrens are covered.
        # If it isn't, that means there is probably something
        # wrong with out graph structure.
        for child in hold.children:
            assert child in dest_nodes

    @property
    def question(self):
        return self._question

    def next_node(self, answer):
        return self._answer_mapping[self._question.classify_answer(answer)]


class QuestionGraphTransverser(DAG.Transverser):
    def transverse(self, answer):
        if self.is_at_leaf:
            return None

        next_node = self._current_node.value.next_node(self, answer)
        self._path.append((self._current_node.value.question,
                           answer))
        self._current_node = next_node
        return self._current_node

    def is_at_leaf(self):
        return self._current_node.is_at_leaf
