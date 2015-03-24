# -*- coding: UTF-8 -*-

import wx

from outwiker.core.commands import MessageBox, testPageTitle, renamePage
from outwiker.gui.preferences.preferencepanelinfo import PreferencePanelInfo
from .preferencesPanel import PreferencesPanel

from i18n import get_

class AutoRenamer (object):
	def __init__ (self, plugin, application):
		self._application = application
		self._plugin = plugin
		global _
		_ = get_()

	def initialize (self):
		self._application.onForceSave += self._renamePage
		self._application.onPreferencesDialogCreate += self.__onPreferencesDialogCreate
	def destroy (self):
		self._application.onForceSave -= self._renamePage
		self._application.onPreferencesDialogCreate -= self.__onPreferencesDialogCreate
	def _renamePage (self):
		currentPage = self._application.selectedPage
		if currentPage is not None:
	                text = currentPage.content.splitlines()[0]
	                text = self.getValidName(text)
	                if not text == "" and text != currentPage.title:
				if testPageTitle (text) == True:
					renamePage(currentPage, text)
	def getValidName (self, name):
		name = "".join(char for char in name if char not in "\/:*?<>|")
		while name[-1] in " .":
			name = name[0:len(name)-1]
		return name

	def __onPreferencesDialogCreate (self, dialog):
		prefPanel = PreferencesPanel (dialog.treeBook, self._application.config)
		panelName = _(u"AutoRenamer [Plugin]")
		panelList = [PreferencePanelInfo (prefPanel, panelName)]
		dialog.appendPreferenceGroup (panelName, panelList)