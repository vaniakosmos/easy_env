import os
from unittest import TestCase

import easy_env as environ


class IntTests(TestCase):
    def setUp(self):
        os.environ.clear()

    def test_get(self):
        os.environ['VALUE'] = '1'
        value = environ.get_int('VALUE')
        self.assertEqual(value, 1)

    def test_get_default(self):
        value = environ.get_int('VALUE', 2)
        self.assertEqual(value, 2)

    def test_none(self):
        value = environ.get_int('VALUE')
        self.assertIsNone(value)

    def test_raise_error(self):
        with self.assertRaises(KeyError):
            environ.get_int('VALUE', raise_error=True)

    def test_bad_value(self):
        os.environ['VALUE'] = 'not int'
        with self.assertRaises(ValueError):
            environ.get_int('VALUE')


class FloatTests(TestCase):
    def setUp(self):
        os.environ.clear()

    def test_get(self):
        os.environ['VALUE'] = '1.1'
        value = environ.get_float('VALUE')
        self.assertAlmostEqual(value, 1.1)

    def test_get_int(self):
        os.environ['VALUE'] = '1'
        value = environ.get_float('VALUE')
        self.assertAlmostEqual(value, 1.0)

    def test_get_default(self):
        value = environ.get_float('VALUE', 2.25)
        self.assertAlmostEqual(value, 2.25)

    def test_none(self):
        value = environ.get_float('VALUE')
        self.assertIsNone(value)

    def test_raise_error(self):
        with self.assertRaises(KeyError):
            environ.get_float('VALUE', raise_error=True)

    def test_bad_value(self):
        os.environ['VALUE'] = 'not float'
        with self.assertRaises(ValueError):
            environ.get_float('VALUE')


class BoolTests(TestCase):
    def setUp(self):
        os.environ.clear()

    def test_get(self):
        os.environ['VALUE'] = '1'
        value = environ.get_bool('VALUE')
        self.assertTrue(value)
        os.environ['VALUE'] = '0'
        value = environ.get_bool('VALUE')
        self.assertFalse(value)

    def test_get_default(self):
        value = environ.get_bool('VALUE', True)
        self.assertTrue(value)
        value = environ.get_bool('VALUE', False)
        self.assertFalse(value)

    def test_none(self):
        value = environ.get_bool('VALUE')
        self.assertIsNone(value)

    def test_raise_error(self):
        with self.assertRaises(KeyError):
            environ.get_bool('VALUE', raise_error=True)

    def test_bad_value(self):
        os.environ['VALUE'] = 'not bool'
        with self.assertRaises(ValueError):
            environ.get_bool('VALUE')


class StrTests(TestCase):
    def setUp(self):
        os.environ.clear()

    def test_get(self):
        os.environ['VALUE'] = '1'
        value = environ.get_str('VALUE')
        self.assertEqual(value, '1')

    def test_get_default(self):
        value = environ.get_str('VALUE', 'foo bar')
        self.assertEqual(value, 'foo bar')

    def test_none(self):
        value = environ.get_str('VALUE')
        self.assertIsNone(value)

    def test_raise_error(self):
        with self.assertRaises(KeyError):
            environ.get_str('VALUE', raise_error=True)


class BytesTests(TestCase):
    def setUp(self):
        os.environ.clear()

    def test_get(self):
        os.environ['VALUE'] = 'Zm9v'
        value = environ.get_bytes('VALUE')
        self.assertEqual(value, b'foo')

    def test_get_default(self):
        value = environ.get_bytes('VALUE', b'yes')
        self.assertEqual(value, b'yes')

    def test_none(self):
        value = environ.get_bytes('VALUE')
        self.assertIsNone(value)

    def test_raise_error(self):
        with self.assertRaises(KeyError):
            environ.get_bytes('VALUE', raise_error=True)


class ListTests(TestCase):
    def setUp(self):
        os.environ.clear()

    def test_get(self):
        os.environ['VALUE'] = '1,2'
        value = environ.get_list('VALUE')
        self.assertEqual(value, ['1', '2'])
        os.environ['VALUE'] = '1,2'
        value = environ.get_list('VALUE', item_factory=int)
        self.assertEqual(value, [1, 2])

    def test_another_separator(self):
        os.environ['VALUE'] = '1 2'
        value = environ.get_list('VALUE', separator=' ')
        self.assertEqual(value, ['1', '2'])

    def test_get_default(self):
        value = environ.get_list('VALUE', [1, 2])
        self.assertEqual(value, [1, 2])

    def test_none(self):
        value = environ.get_list('VALUE')
        self.assertIsNone(value)

    def test_raise_error(self):
        with self.assertRaises(KeyError):
            environ.get_list('VALUE', raise_error=True)

    def test_bad_value(self):
        os.environ['VALUE'] = '1,,2'
        with self.assertRaises(ValueError):
            environ.get_list('VALUE', item_factory=int)

    def test_collections(self):
        os.environ['VALUE'] = '1,2'
        value = environ.get_list('VALUE', item_factory=int, collection=list)
        self.assertListEqual(value, [1, 2])
        value = environ.get_list('VALUE', item_factory=int, collection=set)
        self.assertSetEqual(value, {1, 2})


class AutoGetterTests(TestCase):
    def setUp(self):
        os.environ.clear()

    def test_bad_default(self):
        with self.assertRaises(ValueError):
            environ.get('VALUE', default=object())

    def test_without_default(self):
        os.environ['VALUE'] = '432'
        value = environ.get('VALUE')
        self.assertEqual(value, '432')

    def test_get_int(self):
        os.environ['VALUE'] = '5'
        value = environ.get('VALUE', 1)
        self.assertEqual(value, 5)

    def test_get_int_default(self):
        value = environ.get('VALUE', 1)
        self.assertEqual(value, 1)

    def test_get_list(self):
        os.environ['VALUE'] = '1,2,4'
        value = environ.get('VALUE', [], item_factory=int)
        self.assertEqual(value, [1, 2, 4])
