#!/usr/bin/python3

"""Unit tests of max int function"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unit tests for max int in list"""

    def test_orderd_list(self):
        """Test an orderd list"""
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)

    def test_not_orderd(self):
        """Test not orderd list"""
        list = [5, 8, 2, 33]
        self.assertEqual(max_integer(list), 33)

    def test_negative_number(self):
        """Test list have negative number"""
        list = [-43, 47, -44, -1, -2]
        self.assertEqual(max_integer(list), 47)

    def test_all_negative(self):
        """Test list that all numbers are negative"""
        list = [-5, -3, -45, -12]
        self.assertEqual(max_integer(list), -3)

    def test_emety_list(self):
        """Test emety list"""
        list = []
        self.assertEqual(max_integer(list), None)

    def test_single_list(self):
        """Test a List That have one element"""
        list = [7]
        self.assertEqual(max_integer(list), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)
if __name__ == '__main__':
    unittest.main()
