#!/usr/bin/python3
"""Testing the base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test the base class"""

    def test_hasatrr(self) -> None:
        """test that base class hash the correct attributes"""
        self.assertTrue(hasattr(Base, "__Base__nb_objects"))
        self.assertEqual(Base.__nb_objects, 0)

    def test_init(self) -> None:
        """Test initilizing class"""
        test = Base()
        self.assertEqual(test.id, 1)
        self.assertEqual(test.__dict__, {"id": 1})
        b2 = Base()
        self.assertEqual(b2.id, 2)


if __name__ == "__main__":
    unittest.main()
