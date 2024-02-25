from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
import os

# get and define dir´s
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

close_png = current_dir+'/UIres/close.png'
info_png = current_dir+'/UIres/info.png'

height = 2

class Ui_settings(object):
    def show_hideSettingsPage(self):
        if self.settings_widget.isHidden():
            self.settings_widget.show()
        else:
            self.settings_widget.hide()
            
    def settingssetupUi(self, wpWidget):
        wpWidget.setObjectName("wpWidget")
        wpWidget.resize(315, height)
        self.settings_widget = QtWidgets.QWidget(wpWidget)
        self.settings_widget.setGeometry(QtCore.QRect(0, 0, 320, height))
        self.settings_widget.setObjectName("widget")
        self.background = QtWidgets.QLabel(self.settings_widget)
        self.background.setGeometry(QtCore.QRect(0, 0, 320, height))
        self.background.setStyleSheet("background-color: rgb(35, 34, 39);")
        self.background.setText("")
        self.background.setObjectName("background")
        self.scrollArea = QtWidgets.QScrollArea(self.settings_widget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, height, height))
        self.scrollArea.setStyleSheet("background-color: rgb(35, 34, 39);")
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 313, height))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(5, 0, 270, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.CloseSettings_pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.CloseSettings_pushButton.setGeometry(QtCore.QRect(270, 10, 30, 30))
        self.CloseSettings_pushButton.setIcon(QtGui.QIcon(close_png))
        self.CloseSettings_pushButton.setObjectName("CloseSettings_pushButton")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(5, 40, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.DisableJavascript_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.DisableJavascript_checkBox.setGeometry(QtCore.QRect(5, 60, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DisableJavascript_checkBox.setFont(font)
        self.DisableJavascript_checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.DisableJavascript_checkBox.setObjectName("DisableJavascript_checkBox")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(5, 89, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.AdBlocker_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.AdBlocker_checkBox.setGeometry(QtCore.QRect(5, 110, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.AdBlocker_checkBox.setFont(font)
        self.AdBlocker_checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.AdBlocker_checkBox.setObjectName("AdBlocker_checkBox")
        self.TrackerBlocker_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.TrackerBlocker_checkBox.setGeometry(QtCore.QRect(5, 130, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TrackerBlocker_checkBox.setFont(font)
        self.TrackerBlocker_checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.TrackerBlocker_checkBox.setObjectName("TrackerBlocker_checkBox")
        self.CookieBlocker_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.CookieBlocker_checkBox.setGeometry(QtCore.QRect(5, 150, 300, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CookieBlocker_checkBox.setFont(font)
        self.CookieBlocker_checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.CookieBlocker_checkBox.setObjectName("CookieBlocker_checkBox")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(5, 170, 290, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setGeometry(QtCore.QRect(5, 190, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.DefaultUserAgent_radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.DefaultUserAgent_radioButton.setGeometry(QtCore.QRect(5, 220, 300, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DefaultUserAgent_radioButton.setFont(font)
        self.DefaultUserAgent_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.DefaultUserAgent_radioButton.setObjectName("DefaultUserAgent_radioButton")
        self.RandomUserAgent_radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.RandomUserAgent_radioButton.setGeometry(QtCore.QRect(5, 240, 300, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RandomUserAgent_radioButton.setFont(font)
        self.RandomUserAgent_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.RandomUserAgent_radioButton.setObjectName("RandomUserAgent_radioButton")
        self.CustomUserAgent_radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.CustomUserAgent_radioButton.setGeometry(QtCore.QRect(5, 260, 300, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CustomUserAgent_radioButton.setFont(font)
        self.CustomUserAgent_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.CustomUserAgent_radioButton.setObjectName("CustomUserAgent_radioButton")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setGeometry(QtCore.QRect(5, 339, 297, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.RouteTrafficThroughTor_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.RouteTrafficThroughTor_checkBox.setGeometry(QtCore.QRect(5, 360, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.RouteTrafficThroughTor_checkBox.setFont(font)
        self.RouteTrafficThroughTor_checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.RouteTrafficThroughTor_checkBox.setObjectName("RouteTrafficThroughTor_checkBox")
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(5, 369, 300, 41))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.TrackingLinkProtection_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.TrackingLinkProtection_checkBox.setGeometry(QtCore.QRect(5, 430, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TrackingLinkProtection_checkBox.setFont(font)
        self.TrackingLinkProtection_checkBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 255, 0));")
        self.TrackingLinkProtection_checkBox.setObjectName("TrackingLinkProtection_checkBox")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setGeometry(QtCore.QRect(5, 469, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setGeometry(QtCore.QRect(0, 490, 301, 51))
        self.widget_2.setObjectName("widget_2")
        self.OffProxy_radioButton = QtWidgets.QRadioButton(self.widget_2)
        self.OffProxy_radioButton.setGeometry(QtCore.QRect(5, 0, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.OffProxy_radioButton.setFont(font)
        self.OffProxy_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.OffProxy_radioButton.setObjectName("OffProxy_radioButton")
        self.CustomProxy_radioButton = QtWidgets.QRadioButton(self.widget_2)
        self.CustomProxy_radioButton.setGeometry(QtCore.QRect(5, 21, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CustomProxy_radioButton.setFont(font)
        self.CustomProxy_radioButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.CustomProxy_radioButton.setObjectName("CustomProxy_radioButton")
        self.CustomProxy_radioButton.raise_()
        self.OffProxy_radioButton.raise_()
        self.ProxyInput_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.ProxyInput_widget.setGeometry(QtCore.QRect(0, 540, 371, 90))
        self.ProxyInput_widget.setObjectName("ProxyInput_widget")
        self.label_11 = QtWidgets.QLabel(self.ProxyInput_widget)
        self.label_11.setGeometry(QtCore.QRect(5, 0, 300, 16))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.CustomProxyAddress_lineEdit = QtWidgets.QLineEdit(self.ProxyInput_widget)
        self.CustomProxyAddress_lineEdit.setGeometry(QtCore.QRect(5, 15, 300, 21))
        self.CustomProxyAddress_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.CustomProxyAddress_lineEdit.setObjectName("CustomProxyAddress_lineEdit")
        self.label_12 = QtWidgets.QLabel(self.ProxyInput_widget)
        self.label_12.setGeometry(QtCore.QRect(5, 35, 300, 16))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setTextFormat(QtCore.Qt.PlainText)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.CustomProxyPort_lineEdit = QtWidgets.QLineEdit(self.ProxyInput_widget)
        self.CustomProxyPort_lineEdit.setGeometry(QtCore.QRect(5, 50, 181, 21))
        self.CustomProxyPort_lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.CustomProxyPort_lineEdit.setObjectName("CustomProxyPort_lineEdit")
        self.ApplyProxy_pushButton = QtWidgets.QPushButton(self.ProxyInput_widget)
        self.ApplyProxy_pushButton.setGeometry(QtCore.QRect(195, 50, 111, 21))
        self.ApplyProxy_pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.ApplyProxy_pushButton.setObjectName("ApplyProxy_pushButton")
        self.label_13 = QtWidgets.QLabel(self.ProxyInput_widget)
        self.label_13.setGeometry(QtCore.QRect(5, 70, 291, 21))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setTextFormat(QtCore.Qt.PlainText)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.UserAgentInput_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.UserAgentInput_widget.setGeometry(QtCore.QRect(0, 277, 480, 60))
        self.UserAgentInput_widget.setObjectName("UserAgentInput_widget")
        self.UserAgentInput_plainTextEdit = QtWidgets.QPlainTextEdit(self.UserAgentInput_widget)
        self.UserAgentInput_plainTextEdit.setGeometry(QtCore.QRect(5, 5, 300, 50))
        self.UserAgentInput_plainTextEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.UserAgentInput_plainTextEdit.setPlainText("")
        self.UserAgentInput_plainTextEdit.setObjectName("UserAgentInput_plainTextEdit")
        self.TorSearchEngineBypass_checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.TorSearchEngineBypass_checkBox.setGeometry(QtCore.QRect(5, 399, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.TorSearchEngineBypass_checkBox.setFont(font)
        self.TorSearchEngineBypass_checkBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.TorSearchEngineBypass_checkBox.setObjectName("TorSearchEngineBypass_checkBox")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setGeometry(QtCore.QRect(5, 420, 311, 16))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.label_14.setTextFormat(QtCore.Qt.PlainText)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setGeometry(QtCore.QRect(5, 450, 300, 21))
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.label_15.setTextFormat(QtCore.Qt.PlainText)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.label_5.raise_()
        self.CloseSettings_pushButton.raise_()
        self.label_3.raise_()
        self.DisableJavascript_checkBox.raise_()
        self.label_4.raise_()
        self.AdBlocker_checkBox.raise_()
        self.TrackerBlocker_checkBox.raise_()
        self.CookieBlocker_checkBox.raise_()
        self.label_2.raise_()
        self.label_6.raise_()
        self.DefaultUserAgent_radioButton.raise_()
        self.RandomUserAgent_radioButton.raise_()
        self.CustomUserAgent_radioButton.raise_()
        self.label_7.raise_()
        self.widget_2.raise_()
        self.ProxyInput_widget.raise_()
        self.UserAgentInput_widget.raise_()
        self.TorSearchEngineBypass_checkBox.raise_()
        self.RouteTrafficThroughTor_checkBox.raise_()
        self.label_15.raise_()
        self.TrackingLinkProtection_checkBox.raise_()
        self.label_8.raise_()
        self.label_14.raise_()
        self.label_10.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        button = ("""
            QPushButton{
                background-color:rgba(0, 0, 0, 0);
                color:rgb(255, 255, 255);
                font-size:17px;
            }
            QPushButton:hover{
                background-color:rgba(144, 144, 144, 30);
                border-radius:5px;
            }
            QPushButton:pressed{
                padding-top:5px;
                padding-left:5px;
            }
        """)
        self.CloseSettings_pushButton.setStyleSheet(button)

        self.retranslateUi(wpWidget)
        QtCore.QMetaObject.connectSlotsByName(wpWidget)
        
        # close settings event
        self.CloseSettings_pushButton.pressed.connect(lambda: self.show_hideSettingsPage())
        
        
        # load settings states
        # [General]
        self.DisableJavascript_checkBox.setChecked(self.javascript)
        # [Blocker]
        self.AdBlocker_checkBox.setChecked(self.ad_blocker)
        self.TrackerBlocker_checkBox.setChecked(self.privacy_blocker)
        self.CookieBlocker_checkBox.setChecked(self.cookie_blocker)
        # [User.Agent]
        self.DefaultUserAgent_radioButton.setChecked(self.default_user_agent)
        self.RandomUserAgent_radioButton.setChecked(self.random_user_agent)
        self.CustomUserAgent_radioButton.setChecked(self.custom_user_agent)
        self.UserAgentInput_plainTextEdit.setPlainText(self.custom_user_agent_input)
        # [Privacy]
        self.RouteTrafficThroughTor_checkBox.setChecked(self.RouteTrafficThroughTor)
        self.TorSearchEngineBypass_checkBox.setChecked(self.TorSearchEngineBypass)
        self.TrackingLinkProtection_checkBox.setChecked(self.TrackingLinkProtection)
        # [Proxy]
        self.OffProxy_radioButton.setChecked(self.OffProxy)
        self.CustomProxy_radioButton.setChecked(self.CustomProxy)
        self.CustomProxyAddress_lineEdit.setText(self.custom_proxy_address_input)
        self.CustomProxyPort_lineEdit.setText(self.custom_proxy_port_input)
        
        # setting changed event
        # [General]
        self.DisableJavascript_checkBox.stateChanged.connect(lambda state: self.setJavascript(state))
        # [Blocker]
        self.AdBlocker_checkBox.stateChanged.connect(lambda state: self.setAdBlocker(state))
        self.TrackerBlocker_checkBox.stateChanged.connect(lambda state: self.setTrackerBlocker(state))
        self.CookieBlocker_checkBox.stateChanged.connect(lambda state: self.setCookieBlocker(state))
        # [User.Agent]
        self.DefaultUserAgent_radioButton.toggled.connect(lambda state: self.setDefaultUserAgent(state))
        self.RandomUserAgent_radioButton.toggled.connect(lambda state: self.setRandomUserAgent(state))
        self.CustomUserAgent_radioButton.toggled.connect(lambda state: self.setCustomUserAgent(state))
        self.UserAgentInput_plainTextEdit.textChanged.connect(lambda: self.setUserAgentInput())
        # [Privacy]
        self.RouteTrafficThroughTor_checkBox.toggled.connect(lambda state: self.setRouteTrafficThroughTor(state))
        self.TorSearchEngineBypass_checkBox.toggled.connect(lambda state: self.setTorSearchEngineBypass(state))
        self.TrackingLinkProtection_checkBox.toggled.connect(lambda state: self.setTrackingLinkProtection(state))
        # [Proxy]
        self.OffProxy_radioButton.toggled.connect(lambda state: self.setOffProxy(state))
        self.CustomProxy_radioButton.toggled.connect(lambda state: self.setCustomProxy(state))
        self.CustomProxyAddress_lineEdit.textChanged.connect(lambda: self.setCustomProxyAddress())
        self.CustomProxyPort_lineEdit.textChanged.connect(lambda: self.setCustomProxyPort())
        self.ApplyProxy_pushButton.clicked.connect(lambda state: self.setApplyProxy(state))
        
    def setJavascript(self, state): 
        if state == 0: self.javascript = False 
        else: self.javascript = True
        self.settings_apply()
        
    def setAdBlocker(self, state): 
        if state == 0: self.ad_blocker = False 
        else: self.ad_blocker = True
        self.settings_apply()
        
    def setTrackerBlocker(self, state): 
        if state == 0: self.privacy_blocker = False 
        else: self.privacy_blocker = True
        self.settings_apply()

    def setCookieBlocker(self, state): 
        if state == 0: self.cookie_blocker = False 
        else: self.cookie_blocker = True
        self.settings_apply()
        
    def setDefaultUserAgent(self, state): 
        if state == 0: self.default_user_agent = False 
        else: self.default_user_agent = True
        self.settings_apply()    

    def setRandomUserAgent(self, state): 
        if state == 0: self.random_user_agent = False 
        else: self.random_user_agent = True
        self.settings_apply()  
    
    def setCustomUserAgent(self, state): 
        if state == 0: self.custom_user_agent = False 
        else: self.custom_user_agent = True
        self.settings_apply() 
        
    def setUserAgentInput(self):
        self.custom_user_agent_input = str(self.UserAgentInput_plainTextEdit.toPlainText())
        self.settings_apply() 
        
    def setRouteTrafficThroughTor(self, state):
        if state == 0: self.RouteTrafficThroughTor = False 
        else: self.RouteTrafficThroughTor = True
        self.settings_apply() 
        
    def setTorSearchEngineBypass(self, state):
        if state == 0: self.TorSearchEngineBypass = False 
        else: self.TorSearchEngineBypass = True
        self.settings_apply()  
        
    def setTrackingLinkProtection(self, state):
        if state == 0: self.TrackingLinkProtection = False 
        else: self.TrackingLinkProtection = True
        self.settings_apply()    
        
    def setOffProxy(self, state):
        if state == 0: self.OffProxy = False 
        else: self.OffProxy = True
        self.settings_apply()  
        
    def setCustomProxy(self, state):
        if state == 0: self.CustomProxy = False 
        else: self.CustomProxy = True
        self.settings_apply()  
        
    def setCustomProxyAddress(self):
        self.applyProxy = False
        self.custom_proxy_address_input = str(self.CustomProxyAddress_lineEdit.text())
        self.settings_apply() 
        
    def setCustomProxyPort(self):
        self.applyProxy = False
        self.custom_proxy_port_input = str(self.CustomProxyPort_lineEdit.text())
        self.settings_apply() 
        
    def setApplyProxy(self, state):
        self.applyProxy = True
        self.settings_apply()  
           
    def retranslateUi(self, wpWidget):
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("wpWidget", "Settings"))
        self.label_3.setText(_translate("wpWidget", "General"))
        self.DisableJavascript_checkBox.setText(_translate("wpWidget", "Disable Javascript"))
        self.label_4.setText(_translate("wpWidget", "Blocker"))
        self.AdBlocker_checkBox.setText(_translate("wpWidget", "Ad Blocker"))
        self.TrackerBlocker_checkBox.setText(_translate("wpWidget", "Tracker Blocker"))
        self.CookieBlocker_checkBox.setText(_translate("wpWidget", "Cookie Blocker"))
        self.label_2.setText(_translate("wpWidget", "Ad, Tracker and Cookie blocker will slow down your browser!"))
        self.label_6.setText(_translate("wpWidget", "User Agent"))
        self.DefaultUserAgent_radioButton.setText(_translate("wpWidget", "Default"))
        self.RandomUserAgent_radioButton.setText(_translate("wpWidget", "Random"))
        self.CustomUserAgent_radioButton.setText(_translate("wpWidget", "Custom"))
        self.label_7.setText(_translate("wpWidget", "Privacy"))
        self.RouteTrafficThroughTor_checkBox.setText(_translate("wpWidget", "Route Traffic through Tor"))
        self.label_8.setText(_translate("wpWidget", "Tor routing will make your browser slower, default search engine will be changed to duckduckgo.com"))
        self.TrackingLinkProtection_checkBox.setText(_translate("wpWidget", "Tracking Link Protection"))
        self.label_10.setText(_translate("wpWidget", "Proxy"))
        self.OffProxy_radioButton.setText(_translate("wpWidget", "OFF"))
        self.CustomProxy_radioButton.setText(_translate("wpWidget", "Custom"))
        self.label_11.setText(_translate("wpWidget", "Address"))
        self.CustomProxyAddress_lineEdit.setPlaceholderText(_translate("wpWidget", "ProxyXY.com"))
        self.label_12.setText(_translate("wpWidget", "Port"))
        self.CustomProxyPort_lineEdit.setPlaceholderText(_translate("wpWidget", "7773"))
        self.ApplyProxy_pushButton.setText(_translate("wpWidget", "Apply Proxy"))
        self.label_13.setText(_translate("wpWidget", "Proxy will be deactivated when tor Routing is active"))
        self.TorSearchEngineBypass_checkBox.setText(_translate("wpWidget", "Tor Search Engine Bypass"))
        self.label_14.setText(_translate("wpWidget", "Tor bypass (Ip wont be hidden on Search Engine sites)"))
        self.label_15.setText(_translate("wpWidget", "Will try to block ip grabber links from sites like \"grabify.link\""))