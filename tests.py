import unittest

from wordpad import pad


class Tests(unittest.TestCase):

    def test_pad_left(self):

        self.assertEqual(pad('1', 3), '001')
        self.assertEqual(pad('QA', 2), 'QA')
        self.assertEqual(pad('his', 4, char='t'), 'this')

    def test_pad_right(self):

        self.assertEqual(pad('1', 3, direction='right'), '100')
        self.assertEqual(pad('QA', 2, direction='right'), 'QA')
        self.assertEqual(pad('his', 4, char='t', direction='right'), 'hist')

if __name__ == '__main__':
    unittest.main()
