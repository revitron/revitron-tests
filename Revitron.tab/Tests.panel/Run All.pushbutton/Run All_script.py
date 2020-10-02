import unittest
import os 
import sys
import glob
import inspect
import revitrontests

__context__ = 'zero-doc'

testsDir = os.path.dirname(os.path.dirname(__file__))
suite = unittest.TestSuite()

for directory in glob.glob(testsDir + '\Tests.pulldown\*Tests.pushbutton'):
    sys.path.append(directory)
    for file in glob.glob(directory + '\*Tests_script.py'):
        module = os.path.basename(file).replace('.py', '')
        __import__(module)
        for name, obj in inspect.getmembers(sys.modules[module]):
            if inspect.isclass(obj):
            	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(obj))
        
revitrontests.runSuite(suite)