import revitron
from revitron import _
import revitrontests

__context__ = 'zero-doc'

class RoomTagTests(revitrontests.RevitronTestCase):
	
	def testCreate(self):
     
		room = self.fixture.createRoom()
  
		t = revitron.Transaction()
		tag = revitron.RoomTag.center(room)
		t.commit()
		self.assertEquals(tag.Id.IntegerValue, _(room).getTags()[0].Id.IntegerValue)

		t = revitron.Transaction()
		tag = revitron.RoomTag.topLeft(room)
		t.commit()
		self.assertEquals(tag.Id.IntegerValue, _(room).getTags()[0].Id.IntegerValue)

		t = revitron.Transaction()
		tag = revitron.RoomTag.topRight(room)
		t.commit()
		self.assertEquals(tag.Id.IntegerValue, _(room).getTags()[0].Id.IntegerValue)
  
		t = revitron.Transaction()
		tag = revitron.RoomTag.bottomLeft(room)
		t.commit()
		self.assertEquals(tag.Id.IntegerValue, _(room).getTags()[0].Id.IntegerValue)
  
		t = revitron.Transaction()
		tag = revitron.RoomTag.bottomRight(room)
		t.commit()
		self.assertEquals(tag.Id.IntegerValue, _(room).getTags()[0].Id.IntegerValue)

revitrontests.run(RoomTagTests)