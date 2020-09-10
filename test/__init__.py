from fixture import *

import unittest
from StringIO import StringIO

def run(testClass):
	stream = StringIO()
	runner = unittest.TextTestRunner(stream=stream, verbosity=2)
	result = runner.run(unittest.makeSuite(testClass))
	stream.seek(0)
	print (stream.read())
 