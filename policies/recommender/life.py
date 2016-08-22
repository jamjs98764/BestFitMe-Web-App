"""Policy question DAF for life insurance policies."""

from bestfit.recommender import DAG
from bestfit.recommender import question_dag


# ======================================================
# ============= Questions that we will ask =============
# ======================================================

mortage_question = question_dag.MCQQuestion(
        name="mortage",
        question="Do you own a mortage?",
        description="",
        choices=["No", "Yes"])

children_education_fund_question = question_dag.MCQQuestion(
        name="children_education_fund",
        question="Are you interested in saving for your child's education?",
        description="",
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
    exit_node = DAG.Node()

    n0_0.add_child(n1_0)
    n1_0.add_child(n2_0)

    n0_0.freeze_structure()
    n1_0.freeze_structure()
    exit_node.freeze_structure()

    rule_args = [
        (n0_0, mortage_question, [n1_0, n1_0]),
        (n1_0, children_education_fund_question, [exit_node, exit_node])]

    for node, question, answer_mapping in rule_args:
        question_dag.register_rule(node=node,
                                   question=question,
                                   answer_mapping=answer_mapping)

    return n0_0

decision_graph = _construct_tree()  # type: DAG.Node
