"""Unit test for policies.recommender.health."""

import unittest

from bestfit.recommender import question as question_helper

from policies.recommender import health as recommender_health


class TestAnswerTransversal(unittest.TestCase):

    def setUp(self):
        self.graph = question_helper.QuestionGraphTransverser(
                recommender_health.decision_graph)

    def assert_head_question_equals(self, graph, question):
        self.assertEquals(graph.current_node.value.question, question)

    def test_correct_root(self):
        self.assert_head_question_equals(
                self.graph, recommender_health.age_question)


if __name__ == '__main__':
    unittest.main()
