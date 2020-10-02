import revitron
import unittest
import revitrontests

__context__ = 'zero-doc'

class CatergoryTests(revitrontests.RevitronTestCase):
		   
	def testGet(self):
		self.assertEqual(revitron.Category('Walls').get().Name, 'Walls')
		
	def testGetBic(self):
		self.assertEqual(revitron.Category('Walls').getBic(), revitron.DB.BuiltInCategory.OST_Walls)
		
	  
revitrontests.run(CatergoryTests)