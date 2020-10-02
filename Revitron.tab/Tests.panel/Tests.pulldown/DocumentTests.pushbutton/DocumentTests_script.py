import revitron
import unittest
import os 
import sys
from revitron import _
import revitrontests

__context__ = 'zero-doc'

class DocumentTests(revitrontests.RevitronTestCase):
	
	def testIsFamily(self):
		self.assertFalse(revitron.Document().isFamily())
	
	def testConfigStorage(self):
		config = revitron.DocumentConfigStorage()
		config.set('test.1', {'key': 'value'})
		config.set('test.2', 'string')
		raw = revitron._(revitron.DOC.ProjectInformation).get(config.storageName)
		self.assertEquals(raw, '{"test.1": {"key": "value"}, "test.2": "string"}')
		self.assertEquals(config.get('test.2'), 'string')
	
revitrontests.run(DocumentTests)