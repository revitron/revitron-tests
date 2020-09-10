import unittest
from StringIO import StringIO


from fixture import *


def run(testClass):
	stream = StringIO()
	suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
	runner = unittest.TextTestRunner(stream=stream, verbosity=2)
	result = runner.run(suite)
	stream.seek(0)
	print(stream.read())
 

class RevitronTestCase(unittest.TestCase):
	
	def setUp(self):
		self.fixture = Fixture()
		
	def tearDown(self):
		self.fixture.closeDoc()
 