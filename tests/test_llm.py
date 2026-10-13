import unittest
from unittest.mock import patch,MagicMock
import json
from llm import build_prompt,ollama_answer

class LocalLLMTests(unittest.TestCase):
    def setUp(self):
        self.matches=[{"source":"sla_policy.txt","text":"P1 response is 15 minutes.","score":0.8}]
    def test_prompt_has_source_labels(self):
        prompt=build_prompt("What is P1 response?",self.matches)
        self.assertIn("[1] SOURCE: sla_policy.txt",prompt)
    def test_no_evidence_abstains(self):
        self.assertIn("cannot answer",ollama_answer("unknown",[]))
    def test_rejects_remote_endpoint(self):
        with self.assertRaises(ValueError):
            ollama_answer("P1?",self.matches,base_url="https://remote.example")
    @patch("llm.urlopen")
    def test_local_response(self,mock_open):
        response=MagicMock()
        response.__enter__.return_value=response
        response.read.return_value=json.dumps({"message":{"content":"15 minutes [1]"}}).encode()
        mock_open.return_value=response
        self.assertEqual(ollama_answer("P1?",self.matches),"15 minutes [1]")
if __name__=="__main__":
    unittest.main()
