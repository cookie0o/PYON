from PyQt5.QtNetwork import QNetworkProxy, QNetworkRequest, QNetworkAccessManager, QNetworkReply
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json
import re
import os

# import outside python
from dep.python.lists import *
from dep.python.pages import *
from dep.python.fake import *

# get current dir
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

back_png = current_dir+'/UIres/dark/arrow-left.png'
forward_png = current_dir+'/UIres/dark/arrow-right.png'
reload_png = current_dir+'/UIres/dark/refresh.png'


# validate url
regex = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain
    r'localhost|' #localhost
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE
)


class IconLoader(QObject):
    icon_loaded = pyqtSignal(QIcon)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager = QNetworkAccessManager(self)

    def get_icon_from_url(self, self_, url):
        request = QNetworkRequest(QUrl(url))
        reply = self.manager.get(request)
        reply.finished.connect(lambda: self.on_reply_finished(self_, reply))

    def on_reply_finished(self, self_, reply):
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            pixmap = self.remove_transparent_pixels(pixmap)
            pixmap = pixmap.scaled(60, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon = self.add_padding_to_icon(pixmap)
            self.icon_loaded.emit(icon)
        else:
            if self_.debug_javaScriptConsoleMessage:
                print("Error loading icon:", reply.errorString())

        reply.deleteLater()
        return

    def remove_transparent_pixels(self, pixmap):
        image = pixmap.toImage()
        rect = image.rect()

        def is_transparent(x, y):
            return image.pixelColor(x, y).alpha() == 0

        top, bottom, left, right = 0, rect.bottom(), 0, rect.right()
        
        # Find top
        for y in range(rect.top(), rect.bottom() + 1):
            for x in range(rect.left(), rect.right() + 1):
                if not is_transparent(x, y):
                    top = y
                    break
            if top != 0:
                break

        # Find bottom
        for y in range(rect.bottom(), rect.top() - 1, -1):
            for x in range(rect.left(), rect.right() + 1):
                if not is_transparent(x, y):
                    bottom = y
                    break
            if bottom != rect.bottom():
                break

        # Find left
        for x in range(rect.left(), rect.right() + 1):
            for y in range(rect.top(), rect.bottom() + 1):
                if not is_transparent(x, y):
                    left = x
                    break
            if left != 0:
                break

        # Find right
        for x in range(rect.right(), rect.left() - 1, -1):
            for y in range(rect.top(), rect.bottom() + 1):
                if not is_transparent(x, y):
                    right = x
                    break
            if right != rect.right():
                break

        cropped_rect = QRect(left, top, right - left + 1, bottom - top + 1)
        cropped_image = image.copy(cropped_rect)
        cropped_pixmap = QPixmap.fromImage(cropped_image)
        return cropped_pixmap

    def add_padding_to_icon(self, pixmap, padding_top=7, padding_left=12):
        width = pixmap.width() + padding_left
        height = pixmap.height() + padding_top
        padded_pixmap = QPixmap(width, height)
        padded_pixmap.fill(Qt.transparent)  # Ensure the background is transparent
        
        painter = QPainter(padded_pixmap)
        painter.drawPixmap(padding_left, padding_top, pixmap)
        painter.end()
        
        return QIcon(padded_pixmap)
    


class functions():
    # showContextMenu, UpdateUserAgent, get_profile, TorSearchEngineBypassFunc, Tor_status_msg
    class misc():
        # hide js logs
        def MessageHandler(messageType, context, message):
            # Constants for message types
            QtInfoMsg = 0
            QtWarningMsg = 1
            # Ignore QtWebEngine informational and warning messages
            if messageType not in [QtInfoMsg, QtWarningMsg]:
                return

        def showContextMenu(self):
            # get mouse position
            mouse_position = self.mapFromGlobal(QCursor.pos())
            
            # Create the context menu and add actions
            menu = QMenu(self)
            open_url_in_new_tab = QAction("Open URL in new Tab", self)
            copy_url = QAction("Copy URL", self)
            back_action = QAction("back", self)
            forward_action = QAction( "forward", self)
            reload_action = QAction("reload", self)
            menu.addAction(open_url_in_new_tab)
            menu.addAction(copy_url)
            menu.addAction(back_action)
            menu.addAction(forward_action)
            menu.addAction(reload_action)
            # set style (hover aka. selected is not working I will have to fix this)
            menu.setStyleSheet("""\
                            QMenu {
                                background-color: rgb(35, 34, 39);
                                color: white;
                            }
                            QMenu::item:hover {
                                background-color: rgb(27, 27, 27);
                            }
                        """)

            # EVENTS [context menu]
            # back event
            open_url_in_new_tab.triggered.connect(lambda: functions.tab_functions.add_new_tab(self, self.tabs, self.tabs.currentWidget().url()))
            # back event
            copy_url.triggered.connect(lambda: QApplication.clipboard().setText(self.tabs.currentWidget().url().toString()))
            # back event
            back_action.triggered.connect(lambda: self.tabs.currentWidget().back())
            # forward event
            forward_action.triggered.connect(lambda: self.tabs.currentWidget().forward())
            # reload event
            reload_action.triggered.connect(lambda: self.tabs.currentWidget().reload())

            # Show the context menu at the mouse position
            menu.exec_(self.mapToGlobal(QPoint(mouse_position.x(), mouse_position.y())))

        
        # create and get a profile
        def get_profile(self, current_dir):
            self.profile = QWebEngineProfile.defaultProfile()
            # set the cookie path
            self.profile.setPersistentStoragePath(os.path.join(current_dir, "data/defaultUser"))
            # set the cache path
            self.profile.setCachePath(os.path.join(current_dir, "data/defaultUser"))


        # get default search engine
        def set_url(self):
            if self.RouteTrafficThroughTor:
                return self.tor_search_engine
            else:
                return self.search_engine
            
        # Tor Search Engine Bypass
        def TorSearchEngineBypassFunc(self, url=None):
            # only active when tor routing is on
            if self.RouteTrafficThroughTor:
                if self.TorSearchEngineBypass:
                    self.browser.stop()
                    if url is None:
                        url = self.browser.url().host().replace("www.", "")
                    if url in SearchEngineUrl:
                        QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.NoProxy))
                    else:
                        # set proxy
                        self.proxy.setType(QNetworkProxy.Socks5Proxy)
                        self.proxy.setHostName("127.0.0.1")
                        self.proxy.setPort(self.socks_port)
                        # set proxy
                        QNetworkProxy.setApplicationProxy(self.proxy) 
                    self.browser.load()

            
        
    # set_tab_title, update_urlbar, add_new_tab, navigate_to_url,
    # tab_open_doubleclick, current_tab_changed, close_current_tab, reload_tabs, get_icon_from_url
    class tab_functions():  
        # get favicon
        def get_icon_from_url(self, i, tabs):
            def on_icon_loaded(icon, loader, tabs, i):
                loader.deleteLater()  # Clean up the loader
                # set icon
                tabs.setTabIcon(i, icon)

            widget = tabs.widget(i)
            if widget is None:
                return
            url = widget.page().iconUrl().toString()

            loader = IconLoader()
            loader.icon_loaded.connect(lambda icon: on_icon_loaded(icon, loader, tabs, i))
            loader.get_icon_from_url(self, url)


        # activate fullscreen mode
        def Fullscreen(self, request):
            if request.toggleOn():
                self.showFullScreen()
                # hide gui elements
                self.tabs.setTabBarAutoHide(True) # tabbar
                self.wpWidget_3.hide() # search bar  
            else:
                self.showNormal()
                # show gui elements
                self.tabs.setTabBarAutoHide(False) # tabbar
                self.wpWidget_3.show() # search bar
            # accept the request
            request.accept()
        

        # change tab title
        def set_tab_title(i, browser, tabs, title):
            def set_title(browser, tabs, title):
                widget = tabs.widget(i)
                if widget is None:
                    return
                # check if tab title is provided if not get it
                if title is None:
                    title = widget.page().title()
                    
                # set tab title and shorten it after 25 chars
                if len(title) > 25:
                    title = title[:25] + "..."
                tabs.setTabText(i, " "+title+" ")  
            # get title when the page fully loaded
            browser.loadFinished.connect(lambda: set_title(browser, tabs, title))
          

        # update the url bar
        def update_urlbar(self, q, browser = None):
            if browser != self.tabs.currentWidget():
                return
            
            # dont update prefix urls
            #if ((q.toString()).replace("file:///", "")) in self.pages_paths:
            #    return
            
            # set text to the url bar
            self.urlbar.setText(q.toString())
            # set cursor position
            self.urlbar.setCursorPosition(0)  
        
        
        # method for adding new tab
        def add_new_tab(self, tabs, qurl = None, label ="Blank"):
            self.tabs = tabs
            try:
                # if url is blank
                if qurl is None:
                    # get start page url
                    qurl = functions.misc.set_url(self)

                # creating a QWebEngineView object
                self.browser = QWebEngineView()
                page = QWebEnginePage(self.browser)
                self.browser.setPage(page)
                self.browser.page().setBackgroundColor(QColor(45, 45, 45, 255))
                self.browser.setObjectName("browser")
                self.verticalLayout_3.addWidget(self.browser)

                # create custom context menu
                self.browser.setContextMenuPolicy(Qt.CustomContextMenu)
                self.browser.customContextMenuRequested.connect(lambda: functions.misc.showContextMenu(self))

                # full screen
                self.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
                # plugins
                self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, False)
                # DNS prefetch
                self.browser.settings().setAttribute(QWebEngineSettings.DnsPrefetchEnabled, True)

                # apply settings
                self.settings_apply()

                # setting url to browser
                self.browser.setUrl(QUrl(qurl))

                # setting tab index
                self.i = self.tabs.addTab(self.browser, label)
                self.tabs.setCurrentIndex(0)

                # adding action to the browser when url is changed
                # update the url
                self.browser.urlChanged.connect(lambda qurl, browser = self.browser:
                                        functions.tab_functions.update_urlbar(self, qurl, browser))

                # adding action to the browser when loading is finished
                # set the tab title
                self.browser.urlChanged.connect(lambda _, i=self.i, browser=self.browser, tabs=tabs:
                                        functions.tab_functions.set_tab_title(i, browser, tabs, None))
                
                # javascript injection
                self.browser.urlChanged.connect(lambda _, i=self.i, tabs=self.tabs:  
                                self.inject_qt(i, tabs))
                
                # set favicon
                self.browser.iconChanged.connect(lambda _, i=self.i, tabs=self.tabs:  
                                functions.tab_functions.get_icon_from_url(self, i, tabs))
            
                # fullscreen mode event
                self.browser.page().fullScreenRequested.connect(lambda request: functions.tab_functions.Fullscreen(self, request))
            except Exception as e:
                raise (e)  



        # navigate to url
        def navigate_to_url(self):
            q = QUrl(self.urlbar.text())

            # pages
            if q.toString() == self.prefix+"settings":
                # get and load pages url
                q = self.pages(q.toString())

            # if scheme is blank and there is no domain end then use the default search machine to get a result
            if q.scheme() == "":
                # add a scheme to check if the user just forgot to add it if its still not valid use google
                if (re.match(regex, "https://"+q.toString()) is not None) == False:
                    # domain is not a url use search engine (if Tor: tor search engine)
                    search = (q.toString()).replace(" ", "+")
                    if self.RouteTrafficThroughTor:
                        q = QUrl(self.tor_search_engine_addr + search)
                    else:
                        q = QUrl(self.search_engine_addr + search)
                else:
                    # domain is a url add https
                    q.setScheme("https")
                
            # if scheme is http
            if q.scheme() == "http":
                reply = QMessageBox.question(self, 'Warning', 'You are using "http" change to "https" ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    # set scheme
                    q.setScheme("https")
                else:
                    pass
                
            # check Tor Search EngineBypass before loading
            functions.misc.TorSearchEngineBypassFunc(self, q)
            # set the url
            self.tabs.currentWidget().load(q)


        # when tab is changed
        def current_tab_changed(self, tabs):
            # get the curl
            qurl = tabs.currentWidget().url()
            # update the url
            functions.tab_functions.update_urlbar(self, qurl, self.tabs.currentWidget())
            
            
        # reload all tabs
        def reload_tabs(self):
            # reload all open tabs
            for i in range(self.tabs.count()):
                widget = self.tabs.widget(i)
                # Refresh the content of the widget
                widget.reload()
            return