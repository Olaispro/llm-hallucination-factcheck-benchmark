import unittest
from src.factcheck import summarize
class TestFactcheck(unittest.TestCase):
 def test_uncertain_claim_is_unsupported(self):
  self.assertEqual(summarize([{"label":"supported"},{"label":"not_enough_evidence"}])["unsupported_rate"],.5)
