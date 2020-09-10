import revitron
import unittest
import os 
import sys
from revitron import _

dn = os.path.dirname
sys.path.append(dn(dn(dn(dn(dn(__file__))))))

import revitrontests

__context__ = 'zero-doc'

class BoundingBoxTests(revitrontests.RevitronTestCase):
		   
	def testContainsXY(self):
		wall1 = self.fixture.createWall([0, 0],[20, 20])
		wall2 = self.fixture.createWall([2, 5],[12, 15])
		self.assertTrue(_(wall1).getBbox().containsXY(_(wall2).getBbox()))
		self.assertTrue(_(wall1).getBbox().containsXY(_(wall1).getBbox()))
		self.assertFalse(_(wall2).getBbox().containsXY(_(wall1).getBbox()))

revitrontests.run(BoundingBoxTests)