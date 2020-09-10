import revitron
import unittest
import os 
import sys

dn = os.path.dirname
sys.path.append(dn(dn(dn(dn(dn(__file__))))))

import test

__context__ = 'zero-doc'

class CatergoryTests(unittest.TestCase):
    
    def setUp(self):
        f = test.Fixture()
        
    def testGet(self):
        self.assertEqual(revitron.Category('Walls').get().Name, 'Walls')
        
    def testGetBic(self):
        self.assertEqual(revitron.Category('Walls').getBic(), revitron.DB.BuiltInCategory.OST_Walls)
      
test.run(CatergoryTests)