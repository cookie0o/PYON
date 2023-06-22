from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import os

# get and define dir´s
current_dir = os.path.dirname(os.path.realpath(__file__))
upper_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

back_png = upper_dir+'\\res\\arrow-left.png'
forward_png = upper_dir+'\\res\\arrow-right.png'
reload_png = upper_dir+'\\res\\refresh.png'
home_png = upper_dir+'\\res\\home.png'
settings_png = upper_dir+'\\res\\settings.png'
close_png = upper_dir.replace("\\", "/")+'/res/close.png'

class Ui_tabbar(object):
    def tabsetupUi(self, tabWidget):
        # creating a tab widget
        self.tabs = QTabWidget()
        # making document mode true
        self.tabs.setDocumentMode(True)
        # adding action when double clicked
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        # adding action when tab is changed
        self.tabs.currentChanged.connect(self.current_tab_changed)
        # making tabs closeable
        self.tabs.setTabsClosable(True)
        # adding action when tab close is requested
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        # making tabs visible
        self.tabs.setObjectName("tabs")
        # create stylesheet for the tabs
        self.tabs.setStyleSheet("""
            QTabBar::close-button {
                image: none;
            }

            QTabBar::close-button:selected {
                image: url("""+close_png+"""); 
            }

            QTabBar::close-button:hover {
                background-color:rgba(144, 144, 144, 30);
                border-radius:5px;
            }
            
            QTabBar {
                background-color: rgb(35, 34, 39);
                color: rgb(255, 255, 255);
            }

            QTabBar::tab {
                background-color: rgb(27, 27, 27);
                margin-left: 1px;
                margin-right: 2px;
                margin-top: 2px;
                margin-bottom: 4px;
            }

            QTabBar::tab:selected {
                background-color: rgb(27, 27, 27);
                border: 0.5px solid white;
                border-bottom: 0px solid;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            """)

        # add tabs to widget
        self.verticalLayout_3.addWidget(self.tabs)
        
        QtCore.QMetaObject.connectSlotsByName(tabWidget)