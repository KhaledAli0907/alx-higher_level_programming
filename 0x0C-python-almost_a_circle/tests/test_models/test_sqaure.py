#!/usr/bin/python3

"""
Test the Sqaure Class
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for square class"""

    def test_init(self):
        s1 = Square(1, 5, 6)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 5)
        self.assertEqual(s1.y, 6)

    def test_area(self):
        """Test area method"""
        s2 = Square(3)

        self.assertEqual(s2.area(), 9)

    def test_str(self):
        """Test string"""
        s3 = Square(2)
        self.assertEqual(str(s3), "[Square] (3) 0/0 - 2")
