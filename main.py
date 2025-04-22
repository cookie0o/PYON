from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pkg_resources
import sys
import os

# import UI components
from dep.UIdep.searchbar import Ui_searchbar
from dep.UIdep.tabbar import Ui_tabbar

# import outside python
from dep.python.interceptor import UrlRequestInterceptor
from dep.python.javascriptInjecting import javascript
from dep.python.functions import functions
from dep.python.settings import settings
from dep.python.pages import pages_vars
from dep.python.fake import *

# get current dir
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

# open http://127.0.0.1:5588 to access dev-console
DEBUG_PORT = '5588'
DEBUG_URL = 'http://127.0.0.1:%s' % DEBUG_PORT
os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = DEBUG_PORT



class MainWindow(QWidget, javascript, Ui_searchbar, Ui_tabbar, settings, pages_vars):       
    # constructor    
    def __init__(self, parent = None):
        try:
            # check dependency's
            requirements_file = (os.path.join(current_dir, "requirements.txt"))

            # Read requirements.txt file
            with open(requirements_file, 'r') as f:
                dependencies = f.read().splitlines()

            # Check if each package is installed
            for dependency in dependencies:
                try:
                    pkg_resources.require(dependency)
                except pkg_resources.DistributionNotFound:
                    print (f"{dependency} is not installed (Might cause crashes)")
                except pkg_resources.VersionConflict as e:
                    print (f"{dependency} has a version conflict: {e} (Might cause crashes)")
        except Exception as e:
            raise e
        
        try:
            super(MainWindow, self).__init__(parent = parent)
            self_ = self
            self.socks_port = 9001
            self.control_port = 9002
            
            class JsInterfaces(QObject):
                @pyqtSlot(str)
                def settings(self, localStorageStates):
                    # clean the string before parsing it 
                    safe_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.,{}:,""1234567890'
                    if all(char in safe_characters for char in str(localStorageStates)):
                        settings.settings_page_fetch(self_, localStorageStates)
                    else:
                        return

            # window settings
            self.setMouseTracking(True)

            self.vars()
            self.prefix = "about:"

            # load settings
            self.settings_load()

            # get profile
            functions.misc.get_profile(self, current_dir)
            
            # outside uis
            self.setupUi(self) # main search bar
            self.tabsetupUi(self) # tab bar

            # apply settings
            self.settings_apply()
        
            # javascript injection
            self.inject()
                    
            # setup
            self.resize(1500, 800)


            # Events
            self.urlbar.returnPressed.connect(lambda: functions.tab_functions.navigate_to_url(self))
            self.back_PushButton.clicked.connect(lambda: self.tabs.currentWidget().back())
            self.forward_PushButton.clicked.connect(lambda: self.tabs.currentWidget().forward())
            self.reload_PushButton.clicked.connect(lambda: self.tabs.currentWidget().reload())
            self.home_PushButton.clicked.connect(lambda: self.tabs.currentWidget().setUrl(QUrl(functions.misc.set_url(self))))
            self.settings_PushButton.clicked.connect(lambda: functions.tab_functions.add_new_tab(self, self.tabs, self.pages("settings")))

            # settings page channel
            self.channel = QWebChannel()
            self.js_interface = JsInterfaces()
            self.channel.registerObject("JsInterface", self.js_interface)
        except Exception as e:
            raise e

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
        
    def resizeEvent(self, event):
        # Set the spacer width to 10% of the window width searchbar
        window_width = self.width()
        spacer_width = window_width * 0.10
        self.spacer.changeSize(int(spacer_width), 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout_2.invalidate()


def main(appName, appVersion):
    # Handle high resolution displays:
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    # create app
    app = QApplication(sys.argv)
    app.setApplicationName(appName +" "+ appVersion)
    app.setApplicationVersion(appVersion)
    
    # start interceptor
    interceptor = UrlRequestInterceptor()
    QWebEngineProfile.defaultProfile().setUrlRequestInterceptor(interceptor)
    
    # create window
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())    

if __name__ == "__main__":
    # open file and read app info
    with open (os.path.join(current_dir, "appInfo.txt")) as F:
        appName = F.readline()
        appVersion = F.readline()
    F.close()
    
    # start app
    main(appName, appVersion)
    
    