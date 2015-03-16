# -*- coding: UTF-8 -*-

import wx

from outwiker.core.commands import MessageBox, testPageTitle, renamePage

class AutoRenamer (object):
	def __init__ (self, plugin, application):
		self._application = application
		self._plugin = plugin

	def initialize (self):
		self._application.onForceSave += self._renamePage
	def destroy (self):
		self._application.onForceSave -= self._renamePage
	def _renamePage (self):
		currentPage = self._application.selectedPage
                text = currentPage.content.splitlines()[0]
                if not text == "" and text != currentPage.title:
			if testPageTitle (text) == True:
				renamePage(currentPage, text)
