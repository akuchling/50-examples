#!/usr/bin/env python3

import unittest
import to_celsius

class TestCelsius(unittest.TestCase):
    def test_freezing(self):
        self.assertEqual(to_celsius.convert_f2c('32'), 0)

    def test_boiling(self):
        self.assertEqual(to_celsius.convert_f2c('212'), 100)

    def test_minus40(self):
        self.assertEqual(to_celsius.convert_f2c('-40'), -40)

    def test_error(self):
        self.assertRaises(ValueError, to_celsius.convert_f2c, 'abc')


if __name__ == '__main__':
    unittest.main()

