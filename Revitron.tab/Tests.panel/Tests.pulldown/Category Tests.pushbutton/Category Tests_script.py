import revitron, unittest, os, sys

path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

import tests

class CatergoryTests(unittest.TestCase):
    
    def testGet(self):
        self.assertEqual(revitron.Category('Walls').get().Name, 'Walls')
        
    def testGetBic(self):
        self.assertEqual(revitron.Category('Walls').getBic(), revitron.DB.BuiltInCategory.OST_Walls)
      
tests.run(CatergoryTests)