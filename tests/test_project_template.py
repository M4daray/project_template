import unittest
from project_template import __version__

class TestStringMethods(unittest.TestCase):

    def test_version(self):
        self.assertEqual(__version__, '0.1.0')
