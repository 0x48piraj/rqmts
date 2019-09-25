#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
sys.path.append('..')
from rqmts.parsing import parse, fetch

class TestApp(unittest.TestCase):
   """Test the parse(), fetch() function"""

   def setup(self):
       """This runs before the test cases are executed"""

   def test_0001(self):
       """Test module parsing function"""
       script = open('test.py', 'r').read()
       result = parse(script)
       print("\n======================================================================\n")
       [print(num+1, module) for num, module in enumerate(result)]
       print("\n======================================================================\n")
       self.assertEqual(len(result), 16)
       
   def test_0002(self):
       """Test module package version fetching function"""
       script = open('test.py', 'r').read()
       result = parse(script)
       self.assertEqual(len(result), 16)
       requirements_list = []
       for i in result:
        try:
            pkg_name, version = fetch(i)
            res = pkg_name + '==' + version
            requirements_list.append(res)
        except Exception as e:
            pass
       self.assertEqual(len(requirements_list), 7)

def suite():
   """Test suite"""
   suite = unittest.TestSuite()
   suite.addTests(
       unittest.TestLoader().loadTestsFromTestCase(TestApp)
   )
   return suite

if __name__ == '__main__':
   unittest.TextTestRunner(verbosity=2).run(suite())