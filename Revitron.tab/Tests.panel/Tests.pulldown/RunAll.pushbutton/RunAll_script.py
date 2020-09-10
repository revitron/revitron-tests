import unittest
import os 
import sys
import glob
import inspect

dn = os.path.dirname
sys.path.append(dn(dn(dn(dn(dn(__file__))))))

import revitrontests

__context__ = 'zero-doc'

testsDir = dn(dn(__file__))
suite = unittest.TestSuite()

for directory in glob.glob(testsDir + '\*Tests.pushbutton'):
    sys.path.append(directory)
    for file in glob.glob(directory + '\*Tests_script.py'):
        module = os.path.basename(file).replace('.py', '')
        __import__(module)
        for name, obj in inspect.getmembers(sys.modules[module]):
            if inspect.isclass(obj):
            	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(obj))
        
revitrontests.runSuite(suite)