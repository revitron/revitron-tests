import pyrevit
import revitron
import Autodesk.Revit.UI as rui

 
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

	def createRoom(self):
		self.createWall([0, 0], [0, 10])
		self.createWall([0, 0], [10, 0])
		self.createWall([10, 10], [0, 10])
		self.createWall([10, 10], [10, 0])
		t = revitron.DB.Transaction(self.doc, 'Add Room')
		t.Start()
		room = revitron.DOC.Create.NewRoom(self.level, revitron.DB.UV(4,6))
		t.Commit()
		return room
		
	def show(self, element):
		uidoc = rui.UIDocument(self.doc)
		uidoc.ShowElements(element)