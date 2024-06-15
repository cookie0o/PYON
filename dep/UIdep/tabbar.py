from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtCore import *
from PyQt5 import QtCore
import os

# import outside python
from dep.python.functions import functions


# get dir
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")


class Ui_tabbar(object):
    def tabsetupUi(self, tabWidget):
        # creating a tab widget
        self.tabs = QTabWidget()
        # make tabs closable
        self.tabs.setTabsClosable(True)
        # making document mode true
        self.tabs.setDocumentMode(True)
        # making tabs visible
        self.tabs.setObjectName("tabs")

        # add tabs to widget
        self.verticalLayout_3.addWidget(self.tabs)
        
        QtCore.QMetaObject.connectSlotsByName(tabWidget)
        
        # creating first tab
        functions.tab_functions.add_new_tab(self, self.tabs, functions.misc.set_url(self), 'Homepage')
      
        # adding action when double clicked
        self.tabs.tabBarDoubleClicked.connect(lambda: functions.tab_functions.add_new_tab(self, self.tabs))
        
        # adding action when tab is changed
        self.tabs.currentChanged.connect(lambda: functions.tab_functions.current_tab_changed(self, self.tabs))
        
        # adding action when tab close is requested
        self.tabs.tabCloseRequested.connect(self.close_current_tab)  


    def get_pages(self):
        # list of the current tab pages
        return [self.tabs.widget(index) for index in range(self.tabs.count())]

    # close tab
    def close_current_tab(self, index):
        # dont close the last tab
        if not self.tabs.count() < 2:
            pages = self.get_pages()
            if 0 <= index < self.tabs.count():
                page_to_close = pages[index]
                # remove tab and browser instance
                self.tabs.removeTab(index)
                page_to_close.deleteLater()
            else:
                print("Invalid tab index.")
        return
    