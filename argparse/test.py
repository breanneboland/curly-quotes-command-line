import unittest
from quotes_argparse import judge_your_string

class TestStringJudging(unittest.TestCase):

    def test_judgment(self):
        self.assertFalse(['T', 'h', 'i', 's', ' ', 'p', 'a', 's', 's', 'e', 's', '.'])
        self.assertTrue(['“', 'S', 'o', ' ', 'c', 'u', 'r', 'l', 'y', '!', '”'])

if __name__ == '__main__':
    unittest.main()

# Current problem: original function is too tied up in that namespace.
# So: fix that, and then revisit these tests.
