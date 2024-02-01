#!/usr/bin/python3
""" tests for rectangle.py"""

import io
import unittest
import models.base import Base
import sys
from models.rectangle import Rectangle

class TestRecatngle_instantiation(unittest.TestCase):
    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

        def test_Area(self)
        """is the area working"""
        testrect = Rectangle(7, 6)
        with self.subTest():
            self.assertEqual(testrectangle,area(), 42)
            test rectangle.width = 4
            test rectangle.height = 5
            with self.subTest():
                self.assertEqual(testrectangle.area(), 20)