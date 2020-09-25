import revitron
import unittest
import os 
import sys
from revitron import _

dn = os.path.dirname
sys.path.append(dn(dn(dn(dn(dn(__file__))))))

import revitrontests

__context__ = 'zero-doc'

class RoomTests(revitrontests.RevitronTestCase):
	
	def testRoomTag(self):
		room = self.fixture.createRoom()
		t = revitron.Transaction()
		tag = _(room).tagCenter()
		t.commit()
		self.assertEquals(tag.Id.IntegerValue, _(room).getTags()[0].Id.IntegerValue)
	
	def testRoomCenter(self):
		room = self.fixture.createRoom()
		center = _(room).getBboxCenter()
		self.assertEquals(center.X, 5.0)
		self.assertEquals(center.Y, 5.0)
  
	def testRoomPoints(self):
		xyz = revitron.DB.XYZ
		room = self.fixture.createRoom()
		boundaryPoints = _(room).getBoundaryPoints()
		testPoints = [
			xyz(0, 10, 0),
			xyz(0, 0, 0),
			xyz(10, 0, 0),
			xyz(10, 10, 0)
		]
		for i in range(0, 4):
			self.assertTrue(boundaryPoints[i].IsAlmostEqualTo(testPoints[i]))
   
	def testRoomInsetPoints(self):
		xyz = revitron.DB.XYZ
		room = self.fixture.createRoom()
		boundaryPoints = _(room).getBoundaryInsetPoints(1.0)
		testPoints = [
			xyz(1, 9, 0),
			xyz(1, 1, 0),
			xyz(9, 1, 0),
			xyz(9, 9, 0)
		]
		for i in range(0, 4):
			self.assertTrue(boundaryPoints[i].IsAlmostEqualTo(testPoints[i]))

revitrontests.run(RoomTests)