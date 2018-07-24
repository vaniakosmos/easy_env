import os
from unittest import TestCase

import easy_env as environ


class SetterTests(TestCase):
    def test_int(self):
        environ.set_int('VALUE', 123)
        value = os.environ.get('VALUE')
        self.assertEqual(value, '123')
        environ.set_int('VALUE', 123.9)
        value = os.environ.get('VALUE')
        self.assertEqual(value, '123.9')

    def test_float(self):
        environ.set_float('VALUE', 123.9)
        value = os.environ.get('VALUE')
        self.assertEqual(value, '123.9')

    def test_bool(self):
        environ.set_bool('VALUE', True)
        value = os.environ.get('VALUE')
        self.assertEqual(value, '1')

        environ.set_bool('VALUE', False)
        value = os.environ.get('VALUE')
        self.assertEqual(value, '0')

    def test_str(self):
        environ.set_str('VALUE', '0')
        value = os.environ.get('VALUE')
        self.assertEqual(value, '0')

    def test_bytes(self):
        environ.set_bytes('VALUE', b'foo')
        value = os.environ.get('VALUE')
        self.assertEqual(value, 'Zm9v')

    def test_list(self):
        environ.set_list('VALUE', [1, 2, 3])
        value = os.environ.get('VALUE')
        self.assertEqual(value, '1,2,3')

    def test_auto(self):
        environ.set_var('VALUE', [1, 2, 3])
        value = os.environ.get('VALUE')
        self.assertEqual(value, '1,2,3')
        environ.set_var('VALUE', True)
        value = os.environ.get('VALUE')
        self.assertEqual(value, '1')
        environ.set_var('VALUE', b'foo')
        value = os.environ.get('VALUE')
        self.assertEqual(value, 'Zm9v')
