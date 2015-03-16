# -*- coding: UTF-8 -*-

from outwiker.core.pluginbase import Plugin
from outwiker.core.application import Application

from autorenamer import AutoRenamer
__version__ = u"0.0.0.1"

class PluginVKO (Plugin):
	
	def __init__ (self, application):
		self._autorenamer = AutoRenamer(self, application)	

	@property
	def name (self):
		return u"Vitalii Koshura plugin"

	@property
	def description (self):
		return u'''Plugin to work with directory structure'''

	@property
	def url (self):
		return u"https://github.com/AenBleidd/OutwikerPlugin"

	@property
	def version (self):
		return __version__

	def initialize(self):
		self._autorenamer.initialize()

	def destroy(self):
		pass