import unittest
from retrieval import load_documents,retrieve,grounded_answer
class RetrievalTests(unittest.TestCase):
    def test_policy_retrieval(self):
        docs=load_documents()
        matches=retrieve("P1 incident response time",docs)
        self.assertTrue(matches)
        self.assertEqual(matches[0]["source"],"sla_policy.txt")
    def test_no_support(self):
        message,items=grounded_answer("quantum banana telescope",load_documents())
        self.assertEqual(items,[])
        self.assertIn("No supporting",message)
if __name__=="__main__":
    unittest.main()
