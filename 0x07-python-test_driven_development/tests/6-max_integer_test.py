#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([2, 3.5, 8.9]), 8.9)
        self.assertEqual(max_integer([2, 5.2, 9.1, 3.33]), 9.1)

    def test_tuple(self):
        self.assertEqual(max_integer((1, 2, 3)), 3)
        self.assertEqual(max_integer((1.0, 7.9, 5.6)), 7.9)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_string(self):
        self.assertEqual(max_integer("Strong"), 't')

    def test_dictionary(self):
        self.assertRaises(KeyError, max_integer, {"key": "one", "two": "two"})

    def test_set(self):
        self.assertRaises(TypeError, max_integer, {"key", "value"})

    def test_array(self):
        self.assertRaises(TypeError, max_integer, [2, 3, "value"])
