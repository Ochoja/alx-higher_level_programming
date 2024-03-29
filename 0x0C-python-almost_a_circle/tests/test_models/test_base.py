import unittest
import sys
sys.path.append('../../')
from models.base import Base


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


if __name__ == "__main__":
    unittest.main()
