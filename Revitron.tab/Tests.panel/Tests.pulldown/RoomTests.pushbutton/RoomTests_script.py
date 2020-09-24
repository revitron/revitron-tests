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

revitrontests.run(RoomTests)