import unittest

class BasicTests(unittest.TestCase):

    def test_string_equals(self):

        message = "this is a string"
        self.assertEqual(message, "this is a string")

        message = "another string"
        self.assertEqual(message, "another string")