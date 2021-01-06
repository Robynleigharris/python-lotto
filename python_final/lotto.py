import unittest

class  agetesting(unittest.TestCase):
    def test(self):

        x=21
        message="False"
        self.assertIn(x, range(1, 250), message)

