# -*- coding: UTF-8 -*-

from outwiker.core.config import BooleanOption

class PluginConfig (object):
	def __init__ (self, config):
		self.__config = config
		self.section = u"AutoRenamerPlugin"

		AUTORENAME_ALL_PAGES_OPTION = u"AutoRenameAllPages"
		AUTORENAME_ALL_PAGES_DEFAULT = True
		self.__autoRenameAllPages = BooleanOption (self.__config, self.section, AUTORENAME_ALL_PAGES_OPTION, AUTORENAME_ALL_PAGES_DEFAULT)

	@property
	def autoRenameAllPages (self):
		return self.__autoRenameAllPages.value

	@autoRenameAllPages.setter
	def autoRenameAllPages (self, value):
		self.__autoRenameAllPages.value = value