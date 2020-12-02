import revitron
import unittest
from revitron import _
import revitrontests

__context__ = 'zero-doc'

class FilterTests(revitrontests.RevitronTestCase):
	
	def testStringFilters(self):
	 
		w1 = self.fixture.createWall([0, 10], [10, 10])
		w2 = self.fixture.createWall([0, 20], [10, 20])
		w3 = self.fixture.createWall([0, 30], [10, 30])
		w4 = self.fixture.createWall([0, 40], [10, 40])
		w5 = self.fixture.createWall([0, 50], [10, 50])

		t = revitron.Transaction()
		_(w1).set('test', 'an awesome test wall')
		_(w2).set('test', 'another awesome test wall')
		_(w3).set('test', 'and one more wall')
		_(w4).set('Comments', 'test comment')
  		t.commit()
  
		f = revitron.Filter
		toStr = revitrontests.idsToStr		
		
		self.assertEquals(toStr([w1.Id, w2.Id]),
			toStr(f().byStringContains('test', 'awesome').noTypes().getElementIds()))

		self.assertEquals(toStr([w4.Id, w5.Id]),
			toStr(f().byCategory('Walls').byStringContains('test', 'wall', True).noTypes().getElementIds()))
 
		self.assertEquals(toStr([w3.Id]), 
			toStr(f().byStringBeginsWith('test', 'and one').noTypes().getElementIds()))

		self.assertEquals(toStr([w1.Id, w2.Id, w3.Id]), 
			toStr(f().byStringEndsWith('test', 'wall').noTypes().getElementIds()))

		self.assertEquals(toStr([w3.Id]), 
			toStr(f().byStringEquals('test', 'and one more wall').noTypes().getElementIds()))
		
		self.assertEquals(toStr([w4.Id]), 
			toStr(f().byStringEquals('Comments', 'test comment').noTypes().getElementIds()))

	def testRegexFilter(self):
		family = self.fixture.createGenericModelFamily()
		genModel = self.fixture.createGenericModelInstance(family, revitron.DB.XYZ(0,0,0))
		f = revitron.Filter
		toStr = revitrontests.idsToStr
		self.assertEquals(toStr([genModel.Id]),
			toStr(f().noTypes().byRegex('Family and Type', '\-genericModel\-Revit').getElementIds()))

revitrontests.run(FilterTests)