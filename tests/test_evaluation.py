import unittest
from evaluation import evaluate
class EvaluationTests(unittest.TestCase):
    def test_evaluation_returns_bounded_score(self):
        result=evaluate()
        self.assertEqual(result["cases"],4)
        self.assertTrue(0 <= result["top1_accuracy"] <= 1)
if __name__=="__main__":
    unittest.main()
