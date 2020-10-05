import pyrevit
import revitron
import Autodesk.Revit.UI as rui
from revitron import _

 
class Fixture:
	 
	def __init__(self):
		self.doc = pyrevit.revit.db.create.create_new_project(template=None, imperial=True)
		revitron.DOC = self.doc	
		revitron.APP = self.doc.Application
		self.level = revitron.Filter().byCategory('Levels').noTypes().getElements()[0]
		revitron.ACTIVEVIEW = revitron.Filter().byCategory('Views').noTypes().getElements()[0]

	def closeDoc(self):
		self.doc.Close(False)

	def createWall(self, xy1 = [0, 0], xy2 = [10, 10]):
		p1 = revitron.DB.XYZ(xy1[0], xy1[1], 0)
		p2 = revitron.DB.XYZ(xy2[0], xy2[1], 0)
		line = revitron.DB.Line.CreateBound(p1, p2)
		t = revitron.DB.Transaction(self.doc, 'Add Wall')
		t.Start()
		wall = revitron.DB.Wall.Create(self.doc, line, self.level.Id, False)
		t.Commit()
		return wall

	def createRoom(self, points = False, location = False):
		t = revitron.DB.Transaction(self.doc, 'Add Room')
		t.Start()
		if not points:
			p = revitron.DB.XYZ
			points = [
				p(0,0,0),
				p(10,0,0),
				p(10,10,0),
				p(0,10,0)
			]
		if not location:
			location = revitron.DB.UV(4,6)
		curveArray = self.polygon(points)
		self.doc.Create.NewRoomBoundaryLines(revitron.ACTIVEVIEW.SketchPlane, curveArray, revitron.ACTIVEVIEW)
		room = revitron.DOC.Create.NewRoom(self.level, location)
		t.Commit()
		return room

	def createRoomComplex(self):
		p = revitron.DB.XYZ
		points = [
			p(3,0,0),
			p(9,0,0),
			p(9,4,0),
			p(14,4,0),
			p(14,9,0),
			p(12,9,0),
			p(12,12,0),
			p(2,12,0),
			p(2,7,0),
			p(0,7,0),
			p(0,2,0),
			p(3,2,0)
		]
		location = revitron.DB.UV(4,6)
		return self.createRoom(points, location)
		
	def polygon(self, points):
		curveArray = revitron.DB.CurveArray()
		for i in range(len(points)):
			j = i - 1
			line = revitron.DB.Line.CreateBound(points[j], points[i])
			curveArray.Append(line)
		return curveArray 
  
	def show(self, element):
		uidoc = rui.UIDocument(self.doc)
		uidoc.ShowElements(element)