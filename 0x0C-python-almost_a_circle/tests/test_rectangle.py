#!/usr/bin/python3
"""
====================
Test rectangle class
====================
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test the Rectangle class"""

    def test_init(self):
        """Test initializing class"""
        r1 = Rectangle(4, 5, 4, 0)
        r2 = Rectangle(1, 8, 7, 3)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id + 1, r2.id)

    def test_area(self):
        """test area method"""
        r3 = Rectangle(2, 3)
        self.assertEqual(r3.area(), 6)

    def test_display(self):
        """Test Display function"""
        r4 = Rectangle(2, 3, 1, 2)
        output = " \n  ##\n  ##\n  ##\n"
        self.assertEqual(r4.display(), output)

    def test_str(self):
        r5 = Rectangle(2, 3, 4, 5)
        output = "[Rectangle] (5) 4/5 - 2/3"
        self.assertEqual(str(r5), output)

    def test_update(self):
        """Test the update method of a rectangle object"""
        r6 = Rectangle(1, 2, 3, 4, 5)
        r6.update(6, 7, 8, 9, 10)
        self.assertEqual(r6.id, 6)
        self.assertEqual(r6.width, 7)
        self.assertEqual(r6.height, 8)
        self.assertEqual(r6.x, 9)
        self.assertEqual(r6.y, 10)
        r6.update(id=11, x=12, height=13)
        self.assertEqual(r6.id, 11)
        self.assertEqual(r6.width, 7)
        self.assertEqual(r6.height, 13)
        self.assertEqual(r6.x, 12)
        self.assertEqual(r6.y, 10)

    def test_validation(self):
        """Test the validation of the attributes of a rectangle object"""
        with self.assertRaises(TypeError):
            r7 = Rectangle("a", 1)
        with self.assertRaises(ValueError):
            r8 = Rectangle(0, 1)
        with self.assertRaises(TypeError):
            r9 = Rectangle(1, 2, "a", 1)
        with self.assertRaises(TypeError):
            r10 = Rectangle(1, 2, 1, "a")


if __name__ == "__main__":
    unittest.main()
