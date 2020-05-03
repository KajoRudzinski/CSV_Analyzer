import unittest
import master

class TestOfDemoFunction(unittest.TestCase):

    def test_demofunction(self):
        self.assertEqual(master.demo_function(12),24)
