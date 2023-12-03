from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os

# import UI components
from dep.UIdep.settingspage import Ui_settings
from dep.UIdep.searchbar import Ui_searchbar
from dep.UIdep.tabbar import Ui_tabbar

# import outside python
from dep.python.interceptor import UrlRequestInterceptor
from dep.python.javascriptInjecting import javascript
from dep.python.TorRouting import TorProxy
from dep.python.functions import functions
from dep.python.settings import settings
from dep.python.fake import *

# get current dir
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

# open http://127.0.0.1:5588 to access dev-console
DEBUG_PORT = '5588'
DEBUG_URL = 'http://127.0.0.1:%s' % DEBUG_PORT
os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = DEBUG_PORT


# hide js logs
class WebEnginePage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        if self.debug_javaScriptConsoleMessage:
            print("Lvl: "+level+" - Msg: "+msg)
            

class MainWindow(QWidget, javascript, Ui_searchbar, Ui_tabbar, Ui_settings, settings, TorProxy):
    # constructor
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent = parent)
        # get profile
        functions.misc.get_profile(self, current_dir)
        
        # load settings
        self.settings_load()
        
        # outside uis
        self.setMouseTracking(True)
        self.setupUi(self) # main search bar
        self.tabsetupUi(self) # tab bar
        self.settingssetupUi(self)
        # hide setting page on start
        self.show_hideSettingsPage()
        
        # apply settings
        self.settings_apply()
    
        # javascript injection
        self.inject()
        
        # setup
        self.resize(1500, 800)
        
        # launch tor proxy
        self.launchTorProxy()

        # Events
        self.urlbar.returnPressed.connect(lambda: functions.tab_functions.navigate_to_url(self))
        self.back_PushButton.clicked.connect(lambda: self.tabs.currentWidget().back())
        self.forward_PushButton.clicked.connect(lambda: self.tabs.currentWidget().forward())
        self.reload_PushButton.clicked.connect(lambda: self.tabs.currentWidget().reload())
        self.home_PushButton.clicked.connect(lambda: self.tabs.currentWidget().setUrl(QUrl(functions.misc.set_url(self))))
        self.settings_PushButton.clicked.connect(lambda: self.show_hideSettingsPage())
            
    def resizeEvent(self, event):
        # settings window positioning
        self.settings_widget.setGeometry(QRect((self.width() - 320), 62, 320, self.height()))
        # set height of its elements
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 320, (self.height() - 20)))
        self.background.setGeometry(QRect(0, 0, 320, (self.height())))
        self.scrollArea.setGeometry(QRect(0, 0, 320, (self.height())))
        # height of all options combined
        self.scrollAreaWidgetContents.setMinimumSize(self.scrollAreaWidgetContents.minimumWidth(), 700)

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
    
    