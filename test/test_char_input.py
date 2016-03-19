import unittest

from char_input.char_input import StringChallenge

class TestStringChallenge(unittest.TestCase):
    def test_4words(self):
        text_input = 'My name is Anna'
        sc = StringChallenge()
        result = sc.get_reversed_string(text_input)
        self.assertEqual(result, 'Anna is name My')
