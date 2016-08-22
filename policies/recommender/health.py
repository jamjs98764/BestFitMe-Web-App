"""Policy question DAG for health insurance."""

from bestfit.recommender import DAG
from bestfit.recommender import question_dag


# ======================================================
# ============= Questions that we will ask =============
# ======================================================

age_question = question_dag.MCQQuestion(
        name="age",
        question="Are you younger or older than 35 years of age?",
        description="Age of the user",
        choices=["> 35 years old", "<= 35 years old"])

overseas_cover_question = question_dag.MCQQuestion(
        name="overseas_cover",
        question="Do you want overseas cover",
        description="International protection",
        choices=["No", "Yes"])

extend_to_children_question = question_dag.MCQQuestion(
        name="extend_to_children",
        question="Do you want to extend your cover to your children?",
        description="In case the children is injured",
        choices=["No", "Yes"])

family_question = question_dag.MCQQuestion(
        name="family",
        question="Have you established a family?",
        description="Are you married",
        choices=["No", "Yes"])

joint_policy_question = question_dag.MCQQuestion(
        name="joint_policy",
        question="Are you interested in a joint policy?",
        description="Joint policy",
        choices=["No", "Yes"])

emergency_case_cover_question = question_dag.MCQQuestion(
        name="emergency_case_cover",
        question="Do you want emergency case cover",
        description="lorem ipsum",
        choices=["No", "Yes"])


# ======================================================
# ================= The tree structure =================
# ======================================================

def _construct_tree():
    """Constructs a DAG-representation of the questions to ask."""
    # Attribute naming convention
    # n{layer_number}_{node_number}
    n0_0 = DAG.Node()
    n1_0 = DAG.Node()
    n2_0 = DAG.Node()
    n3_0 = DAG.Node()
    n4_0 = DAG.Node()
    n5_0 = DAG.Node()
    exit_node = DAG.Node()

    n0_0.add_child(n1_0)
    n1_0.add_child(n2_0)
    n1_0.add_child(n4_0)
    n2_0.add_child(n3_0)
    n3_0.add_child(n4_0)
    n4_0.add_child(n5_0)
    n5_0.add_child(exit_node)

    n0_0.freeze_structure()
    n1_0.freeze_structure()
    n2_0.freeze_structure()
    n3_0.freeze_structure()
    n4_0.freeze_structure()
    n5_0.freeze_structure()

    rule_args = [
        (n0_0, age_question, [n1_0, n1_0]),
        (n1_0, family_question, [n4_0, n2_0]),
        (n2_0, joint_policy_question, [n3_0, n3_0]),
        (n3_0, extend_to_children_question, [n4_0, n4_0]),
        (n4_0, emergency_case_cover_question, [n5_0, n5_0]),
        (n5_0, overseas_cover_question, [exit_node, exit_node])]

    for node, question, answer_mapping in rule_args:
        question_dag.register_rule(node=node,
                                    question=question,
                                    answer_mapping=answer_mapping)

    return n0_0

decision_graph = _construct_tree()  # type: DAG.Node
