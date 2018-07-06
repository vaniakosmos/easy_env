import os
from unittest import TestCase

import easy_env as environ


class IntGetterTests(TestCase):
    def setUp(self):
        os.environ.clear()

    def test_get(self):
        environ.set_int('INT_VAL', 1)
        value = environ.get_int('INT_VAL')
        self.assertEqual(value, 1)

    def test_get_default(self):
        value = environ.get_int('INT_VAL', 2)
        self.assertEqual(value, 2)

    def test_none(self):
        value = environ.get_int('INT_VAL')
        self.assertIsNone(value)

    def test_raise_error(self):
        with self.assertRaises(KeyError):
            environ.get_int('INT_VAL', raise_error=True)

    def test_bad_value(self):
        os.environ['INT_VAL'] = 'not int'
        with self.assertRaises(ValueError):
            environ.get_int('INT_VAL')
