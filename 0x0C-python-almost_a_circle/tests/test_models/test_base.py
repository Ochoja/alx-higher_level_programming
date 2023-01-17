import unittest
from models.base import Base
import sys

sys.path.append('../../')

class TestBaseClass(unittest.TestCase):
    def test_Base(self):
        result = Base()
        self.assertEqual(result.id, 1)
