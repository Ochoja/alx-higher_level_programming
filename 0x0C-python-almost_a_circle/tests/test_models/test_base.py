import unittest
from models.base import Base
import sys

sys.path.append('../../')

class TestBaseClass(unittest.TestCase):
    def test_Base(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        c = Base()
        self.assertEqual(c.id, 3)
        d = Base(12)
        self.assertEqual(d.id, 12)
        e = Base()
        self.assertEqual(e.id, 4)
