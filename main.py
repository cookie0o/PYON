# importing required libraries
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from datetime import datetime
import configparser
import time
import sys
import os
import re
# web page ui
from dep.UIelements.webUI import Ui_wpWidget, SettingsPage, back_png, forward_png, reload_png, settings_png, close_png
# tabs ui
from dep.UIelements.tabbarUI import Ui_tabbar
# outside functions
from dep.func import *
# block func.
from dep.block import Block, WebEngineUrlRequestInterceptor, RULES_AD_local, RULES_TRACKER_local
# settings func.
from dep.SettingsFunctions import ApplySettings
# event func.
from dep.EventFunctions import (AllowJavascript_, EnableADblocker_, EnableTrackerblocker_, UserAgent_, UserAgent_combobox,
                                 SessionTabs_, SearchPage_, Lists_) 

# enable debugger
debugger = False
# open http://127.0.0.1:5588 in a different browser to access dev-console
DEBUG_PORT = '5588'
DEBUG_URL = 'http://127.0.0.1:%s' % DEBUG_PORT
os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = DEBUG_PORT

# hide js logs
class WebEnginePage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        if debugger == True:
            print (msg)

current_dir = os.path.dirname(os.path.realpath(__file__))

# init config and select file
config = configparser.ConfigParser()
config_dir = current_dir+'\\dep\\config\\config.ini'
config.read(config_dir)

# main window
class MainWindow(QWidget, Ui_wpWidget, Ui_tabbar):
    
    # run function if the user is trying to close the window
    def closeEvent(self, event):
        # check if tabs should be saved
        if self.SaveAndOpenTabsOnNextSession_checkBox.isChecked() == True:
            # Save URLs of all open tabs
            log("", "remembering your current tabs for next time")
            tab_urls = []
            for i in range(self.tabs.count()):
                tab = self.tabs.widget(i)
                # check if url is just the default search engine if yes dont save it
                if not self.search_address+"/" in tab.url().toString(): # dont open home address twice
                    tab_urls.append(tab.url().toString())
                else:
                    pass
            config['tabs']['urls'] = ';'.join(tab_urls)
            config["startpage"]["search_address"] = self.search_address
            # Save config file
            with open(config_dir, 'w') as configfile:
                config.write(configfile)

        # close browsere
        log("", "closing see you next time...")
        exit()
 
    # constructor
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent = parent)
        self.setMouseTracking(True)
        self.setupUi(self, RULES_AD_local, RULES_TRACKER_local) # main search bar
        self.tabsetupUi(self) # tab bar
        # setup
        self.setup()
        self.resize(1500, 800)

        # get search address from file
        config.read(config_dir)
        self.search_address = config["startpage"]["search_address"]

        # creating first tab
        self.add_new_tab(QUrl(str(self.search_address)), 'Homepage')

        # check if tabs should be loaded
        if config["tabs"]["openloadtabs"] == "True":
            # load tabs from last session
            log("", "loading tabs from last session")
            for url in config['tabs']['urls'].split(';'):
                # check if the url is valid before loading it
                if (re.match(regex, url) is not None) != False:
                    self.add_new_tab(QUrl(str(url)))

        # EVENTS
        # search event
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        # back event
        self.back_PushButton.clicked.connect(lambda: self.tabs.currentWidget().back())
        # forward event
        self.forward_PushButton.clicked.connect(lambda: self.tabs.currentWidget().forward())
        # reload event
        self.reload_PushButton.clicked.connect(lambda: self.tabs.currentWidget().reload())
        # home event
        self.home_PushButton.clicked.connect(lambda: self.tabs.currentWidget().setUrl(QUrl(self.search_address)))
        # settings event
        self.settings_PushButton.clicked.connect(lambda: SettingsPage(self))
        # ally User Agent event
        self.UpdateUserAgent_pushButton.clicked.connect(lambda: UpdateUserAgent(self, ""))

        # events (run func when checkbox state was changed or combobox)
        # allow javascript
        self.AllowJavascript_checkBox.stateChanged.connect(lambda: AllowJavascript_(self))
        # enable ADblocker
        self.EnableADblocker_checkBox.stateChanged.connect(lambda: EnableADblocker_(self)) 
        # enable Tracker-blocker
        self.EnableTrackerblocker_checkBox.stateChanged.connect(lambda: EnableTrackerblocker_(self)) 
        # enable User Agent switchern
        self.UserAgentSwitcher_checkBox.stateChanged.connect(lambda: UserAgent_(self)) 
        # combobox user agent
        self.UserAgentMode_comboBox.currentIndexChanged.connect(lambda: UserAgent_combobox(self))
        # save and load tabs on next session
        self.SaveAndOpenTabsOnNextSession_checkBox.stateChanged.connect(lambda: SessionTabs_(self)) 
        # custom search engine
        self.DefaultSearchEngine_comboBox.currentIndexChanged.connect(lambda: SearchPage_(self))
        # lists
        self.ADblockerLists_comboBox.activated.connect(lambda: Lists_(self, RULES_AD_local, RULES_TRACKER_local))
        self.TrackerblockerLists_comboBox.activated.connect(lambda: Lists_(self, RULES_AD_local, RULES_TRACKER_local))

        # display current user agent to user
        CurrentUserAgent = self.tabs.currentWidget().page().profile().httpUserAgent()
        self.CurrentUserAgent_plainTextEdit.insertPlainText(str(CurrentUserAgent))

        # apply settings
        ApplySettings(self, config, log)


    # method for adding new tab
    def add_new_tab(self, qurl = None, label ="Blank"):
        try:
            # if url is blank
            if qurl is None:
                # creating aurl
                qurl = (str(self.search_address))

            # creating a QWebEngineView object
            self.browser = QWebEngineView()
            page = WebEnginePage(self.browser)
            self.browser.setPage(page)
            self.browser.page().setBackgroundColor(QColor(45, 45, 45, 255))
            self.browser.setObjectName("browser")
            self.verticalLayout_3.addWidget(self.browser)

            # create custom context menu
            self.browser.setContextMenuPolicy(Qt.CustomContextMenu)
            self.browser.customContextMenuRequested.connect(self.showContextMenu)

            # allow full screen
            self.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
            # allow plugins
            self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)

            # setting url to browser
            self.browser.setUrl(QUrl(qurl))

            # setting tab index
            self.i = self.tabs.addTab(self.browser, label)
            self.tabs.setCurrentIndex(0)

            # adding action to the browser when url is changed
            # update the url
            self.browser.urlChanged.connect(lambda qurl, browser = self.browser:
                                    self.update_urlbar(qurl, browser))

            # adding action to the browser when loading is finished
            # set the tab title
            self.browser.loadFinished.connect(lambda _, i=self.i, browser=self.browser, tabs=self.tabs:
                                    set_tab_title(i, browser, tabs, None))
            

            """
            self.inspector = QWebEngineView()
            self.inspector.setWindowTitle('Web Inspector')
            self.inspector.load(QtCore.QUrl(DEBUG_URL))
            self.browser.page().setDevToolsPage(self.inspector.page())
            self.inspector.show()
            """
            
            # fullscreen mode event
            self.browser.page().fullScreenRequested.connect(lambda: self.fullscreen())
            self.browser.page().fullScreenRequested.connect(lambda request: request.accept())
            log("", "Opened new Tab")
        except Exception as e:
            raise (e)

    # when double clicked is pressed on tabs
    def tab_open_doubleclick(self, i):
        # checking index i.e
        # No tab under the click
        if i == -1:
            # creating a new tab
            self.add_new_tab()

    # when tab is changed
    def current_tab_changed(self, i):
        # get the curl
        qurl = self.tabs.currentWidget().url()
        # update the url
        self.update_urlbar(qurl, self.tabs.currentWidget())

    # when tab is closed
    def close_current_tab(self, i):
        # if there is only one tab
        if self.tabs.count() < 2:
            # do nothing
            return
        # else remove the tab
        self.tabs.removeTab(i)

    # method for navigate to url
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())

        # if scheme is blank and there is no domain end then use the default search machine to get a result
        if q.scheme() == "":
            # add a scheme to check if the user just forgot to add it if its still not valid use google
            if (re.match(regex, "https://"+q.toString()) is not None) == False:
                # domain is not a url use search engine
                search = (q.toString()).replace(" ", "+")
                if self.search_address == "https://www.google.com" or self.search_address == "https://www.bing.com":
                    q = QUrl(f"{self.search_address}/search?q={search}")
                elif self.search_address == "https://duckduckgo.com":
                    q = QUrl(f"{self.search_address}/?q={search}")
            else:
                # domain is a url add https
                q.setScheme("https")
            
        # if scheme is http give message for sec.
        if q.scheme() == "http":
            reply = QMessageBox.question(self, 'Warning', 'You are using "http" change to "https" ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # set scheme
                q.setScheme("https")
            else:
                pass

        # set the url
        self.tabs.currentWidget().load(q)

     
    # update the url
    def update_urlbar(self, q, browser = None):
        if browser != self.tabs.currentWidget():
            return
        # set text to the url bar
        self.urlbar.setText(q.toString())
        # set cursor position
        self.urlbar.setCursorPosition(0)

    # fullscreen mode
    def fullscreen(self):
        if not self.isFullScreen():
            # show window over any other one and hide title bar
            self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint)
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            # toggle full screen
            self.showFullScreen()
        else:
            # revert changes
            self.setWindowFlags(QtCore.Qt.Window)
            # toggle minimized
            self.showNormal()
            # show window in normal size
            self.resize(1500, 800)


    def showContextMenu(self, event):
        # Create the context menu and add actions
        menu = QMenu(self)
        back_action = QAction(QIcon(back_png), "back", self)
        forward_action = QAction(QIcon(forward_png), "forward", self)
        reload_action = QAction(QIcon(reload_png), "reload", self)
        menu.addAction(back_action)
        menu.addAction(forward_action)
        menu.addAction(reload_action)
        # set style (hover aka. selected is not working I will have to fix this)
        menu.setStyleSheet('background-color: rgb(35, 34, 39);\n'
                        'color: white;\n'
                        'QMenu::item:selected{\n'
                        '    background-color: rgb(27, 27, 27);\n'
                        '}')

        # EVENTS [context menu]
        # back event
        back_action.triggered.connect(lambda: self.tabs.currentWidget().back())
        # forward event
        forward_action.triggered.connect(lambda: self.tabs.currentWidget().forward())
        # reload event
        reload_action.triggered.connect(lambda: self.tabs.currentWidget().reload())

        # Show the context menu at the mouse position
        menu.exec_(self.mapToGlobal(QPoint(event.x()-2, event.y()+62)))

    # create browser profile and add paths
    def setup(self):
        try:
            self.profile = QWebEngineProfile.defaultProfile()
            # set the cookie path
            self.profile.setPersistentStoragePath(current_dir+"\\data")
            # set the cache path
            self.profile.setCachePath(current_dir+"\\data")

            log("", "created profile and defined paths")
            # update ADblock urls
            Block()
        except Exception as e:
            raise (e)

if __name__ == '__main__':
    # get window name and version
    with open(current_dir+"\\app\\info.txt") as info_f:
        window_name = info_f.readline()
        app_version = info_f.readline()
        info_f.close() # close file after information was read
    # create app
    app = QApplication(sys.argv)
    app.setApplicationName(window_name+" " +app_version)
    # block for ads and trackers
    interceptor = WebEngineUrlRequestInterceptor()
    QWebEngineProfile.defaultProfile().setUrlRequestInterceptor(interceptor)
    # create window
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())