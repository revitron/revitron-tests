import revitron
import unittest
from revitron import _
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

	def testRoomTopLeft(self):
		room = self.fixture.createRoomComplex()
		topLeft = _(room).getTopLeftPoint(0.5)
		self.assertTrue(topLeft.IsAlmostEqualTo(revitron.DB.XYZ(2.5,11.5,0)))

	def testRoomTopRight(self):
		room = self.fixture.createRoomComplex()
		topLeft = _(room).getTopRightPoint(0.5)
		self.assertTrue(topLeft.IsAlmostEqualTo(revitron.DB.XYZ(11.5,11.5,0)))
  
	def testRoomBottomLeft(self):
		room = self.fixture.createRoomComplex()
		topLeft = _(room).getBottomLeftPoint(0.5)
		self.assertTrue(topLeft.IsAlmostEqualTo(revitron.DB.XYZ(0.5,2.5,0)))
  
	def testRoomBottomRight(self):
		room = self.fixture.createRoomComplex()
		topLeft = _(room).getBottomRightPoint(0.5)
		self.assertTrue(topLeft.IsAlmostEqualTo(revitron.DB.XYZ(13.5,4.5,0)))

revitrontests.run(RoomTests)