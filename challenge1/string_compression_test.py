import unittest

from .string_compression import compress


class StringCompressionTest(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(compress('a'), 'a')
        self.assertEqual(compress('abcd'), 'abcd')
        self.assertEqual(compress('bbcceeee'), 'b2c2e4')
        self.assertEqual(compress('aaabbbcccaaa'), 'a3b3c3a3')
        self.assertEqual(compress('aaaabbbccddddddee'), 'a4b3c2d6e2')
