"""Unit test for policies.recommender.health."""

import unittest

from bestfit.recommender import question_dag

from policies.recommender import health as recommender_health


class TestAnswerTransversal(unittest.TestCase):

    def setUp(self):
        self.transverser = question_dag.QuestionGraphTransverser(
                recommender_health.decision_graph)

    def assert_head_question_equals(
            self,
            transverser: question_dag.QuestionGraphTransverser,
            question: question_dag.QuestionBase):
        self.assertEquals(transverser.current_question, question)

    def test_correct_root(self):
        self.assert_head_question_equals(
                self.transverser, recommender_health.age_question)

    def test_transverse_one_step(self):
        question = self.transverser.current_question
        previous_node = self.transverser.current_node
        self.transverser.transverse(question.choices[0])

        self.assertEquals(self.transverser.current_question,
                          recommender_health.family_question)
        self.assertNotEquals(self.transverser.current_node,
                             previous_node)

    def test_answer_cross_and_join_graph(self):
        transverser_a = question_dag.QuestionGraphTransverser(
                recommender_health.decision_graph)
        transverser_b = question_dag.QuestionGraphTransverser(
                recommender_health.decision_graph)

        self.assertEquals(transverser_a.current_node,
                          transverser_b.current_node)
        self.assertEquals(transverser_a.current_question,
                          transverser_b.current_question)
        transverser_a.transverse(transverser_a.current_question.choices[0])
        transverser_b.transverse(transverser_b.current_question.choices[0])

        self.assertEquals(transverser_a.current_node,
                          transverser_b.current_node)
        self.assertEquals(transverser_a.current_question,
                          transverser_b.current_question)
        transverser_a.transverse(transverser_a.current_question.choices[0])
        transverser_b.transverse(transverser_b.current_question.choices[1])

        self.assertEquals(transverser_a.current_question,
                          recommender_health.emergency_case_cover_question)
        self.assertEquals(transverser_b.current_question,
                          recommender_health.joint_policy_question)

        transverser_b.transverse(transverser_b.current_question.choices[0])
        self.assertEquals(transverser_b.current_question,
                          recommender_health.extend_to_children_question)

        transverser_b.transverse(transverser_b.current_question.choices[0])
        self.assertEquals(transverser_b.current_question,
                          transverser_a.current_question)
        self.assertEquals(transverser_b.current_node,
                          transverser_a.current_node)

    def test_transversal_end(self):
        questions = [
                recommender_health.age_question,
                recommender_health.family_question,
                recommender_health.joint_policy_question,
                recommender_health.extend_to_children_question,
                recommender_health.emergency_case_cover_question,
                recommender_health.overseas_cover_question]

        for ques in questions:
            self.assertEquals(ques, self.transverser.current_question)
            self.assertFalse(self.transverser.is_at_leaf())
            self.transverser.transverse(
                    self.transverser.current_question.choices[1])

        self.assertTrue(self.transverser.is_at_leaf()) 


if __name__ == '__main__':
    unittest.main()
