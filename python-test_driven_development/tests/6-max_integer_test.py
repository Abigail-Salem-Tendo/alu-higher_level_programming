#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        """Test when list is ordered"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max at the beginning"""
        self.assertEqual(max_integer([9, 3, 4, 1]), 9)

    def test_one_element(self):
        """Test with only one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 5, -2]), 5)

    def test_all_same(self):
        """Test when all elements are the same"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.2, 3.4, 2.5]), 3.4)

    def test_mix_int_float(self):
        """Test with mix of ints and floats"""
        self.assertEqual(max_integer([1, 2.2, 3, 0.5]), 3)

    def test_large_list(self):
        """Test with a large list"""
        self.assertEqual(max_integer(list(range(10000))), 9999)

    def test_string_input(self):
        """Test with string as a list"""
        self.assertEqual(max_integer("hello"), 'o')

    def test_list_of_strings(self):
        """Test with list of strings"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

if __name__ == '__main__':
    unittest.main()
