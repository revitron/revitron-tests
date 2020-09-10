import pyrevit
import revitron

 
class Fixture:
	 
	def __init__(self):
		self.doc = pyrevit.revit.db.create.create_new_project(template=None, imperial=True)
		revitron.DOC = self.doc	
