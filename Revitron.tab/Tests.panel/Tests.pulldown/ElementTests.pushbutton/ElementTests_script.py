import revitron
import unittest
import os 
import sys
from revitron import _
import revitrontests

__context__ = 'zero-doc'

class ElementTests(revitrontests.RevitronTestCase):
	
	def testGetBbox(self):
		wall = self.fixture.createWall([0, 10], [10, 10])
		bbox = _(wall).getBbox().bbox
		self.assertEquals(bbox.Max.X, 10.0)
	
	def testGetClassName(self):
		wall = self.fixture.createWall()
		self.assertEquals(_(wall).getClassName(), 'Wall')
  
	def testGetSet(self):
		wall = self.fixture.createWall()
		t = revitron.Transaction()
		_(wall).set('Test', 'Value')
		_(wall).set('Comments', 'Some comment')
		t.commit()
		self.assertEquals(_(wall).get('Test'), 'Value')
		self.assertEquals(_(wall).get('Comments'), 'Some comment')
 
revitrontests.run(ElementTests)