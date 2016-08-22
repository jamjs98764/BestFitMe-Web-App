"""Unit test for bestfit.recommender.life."""

import unittest

from bestfit.recommender import question_dag
from bestfit.recommender import life as recommender_life


class TestAnswerTransversal(unittest.TestCase):

    def setUp(self):
        self.transverser = question_dag.QuestionGraphTransverser(
                recommender_life.decision_graph)

    def assert_head_question_equals(
            self,
            transverser: question_dag.QuestionGraphTransverser,
            question: question_dag.QuestionBase):
        self.assertEquals(transverser.current_question, question)

    def test_exit_leaf(self):
        choices = self.transverser.current_question.choices
        self.assertFalse(self.transverser.is_at_leaf())
        self.transverser.transverse(choices[0])
        self.assertFalse(self.transverser.is_at_leaf())
        self.transverser.transverse(choices[0])
        self.assertTrue(self.transverser.is_at_leaf())

    def test_root(self):
        self.assert_head_question_equals(
                self.transverser, recommender_life.mortage_question)


if __name__ == '__main__':
    unittest.main()
