from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
import configparser
import os

# get and define dir´s
current_dir = os.path.dirname(os.path.realpath(__file__))
upper_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
# init config and select file
config = configparser.ConfigParser()
config_dir = upper_dir+'\\config\\config.ini'

back_png = upper_dir+'\\res\\arrow-left.png'
forward_png = upper_dir+'\\res\\arrow-right.png'
reload_png = upper_dir+'\\res\\refresh.png'
home_png = upper_dir+'\\res\\home.png'
settings_png = upper_dir+'\\res\\settings.png'
close_png = upper_dir.replace("\\", "/")+'/res/close.png'

# select everything in the search bar when selected
class LineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(LineEdit, self).__init__(parent)
        self.readyToEdit = True

    def mousePressEvent(self, e, Parent=None):
        super(LineEdit, self).mousePressEvent(e) #required to deselect on 2e click
        if self.readyToEdit:
            self.selectAll()
            self.readyToEdit = False

    def focusOutEvent(self, e):
        super(LineEdit, self).focusOutEvent(e) #required to remove cursor on focusOut
        self.readyToEdit = True

# settings page event
def SettingsPage(self):
    if self.verticalLayoutWidget.isHidden():
        # update blocked trackers / ads int from settings
        config.read(config_dir)
        TrackersBlocked = config["values"]["blocked_trackers"]
        AdsBlocked      = config["values"]["blocked_ads"]
        self.label_6.setText(f"Trackers Blocked (since installation): {TrackersBlocked}")
        self.label_9.setText(f"Advertisements Blocked (since installation): {AdsBlocked}")
        # show page
        self.verticalLayoutWidget.show()
    else:
        self.verticalLayoutWidget.hide()


class Ui_wpWidget(object):
    def setupUi(self, wpWidget):
        wpWidget.setObjectName("wpWidget")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wpWidget.sizePolicy().hasHeightForWidth())
        wpWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(wpWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wpWidget_2 = QtWidgets.QWidget(wpWidget)
        self.wpWidget_2.setObjectName("wpWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wpWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wpWidget_3 = QtWidgets.QWidget(self.wpWidget_2)
        self.wpWidget_3.setMinimumSize(QtCore.QSize(0, 40))
        self.wpWidget_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.wpWidget_3.setStyleSheet("QWidget#wpWidget_3{\n"
"    background-color:rgb(35, 34, 39);\n"
"}")
        self.wpWidget_3.setObjectName("wpWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wpWidget_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 18, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wpWidget_5 = QtWidgets.QWidget(self.wpWidget_3)
        self.wpWidget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.wpWidget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.wpWidget_5.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0, 0, 0, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    font-size:17px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(144, 144, 144, 30);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.wpWidget_5.setObjectName("wpWidget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wpWidget_5)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.back_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.back_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.back_PushButton.setIcon(QtGui.QIcon(back_png))
        self.back_PushButton.setObjectName("back_PushButton")
        self.horizontalLayout.addWidget(self.back_PushButton)
        self.forward_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.forward_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.forward_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.forward_PushButton.setIcon(QtGui.QIcon(forward_png))
        self.forward_PushButton.setObjectName("forward_PushButton")
        self.horizontalLayout.addWidget(self.forward_PushButton)
        self.reload_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.reload_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.reload_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.reload_PushButton.setIcon(QtGui.QIcon(reload_png))
        self.reload_PushButton.setObjectName("reload_PushButton")
        self.horizontalLayout.addWidget(self.reload_PushButton)
        self.home_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.home_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.home_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.home_PushButton.setIcon(QtGui.QIcon(home_png))
        self.home_PushButton.setObjectName("home_PushButton")
        self.horizontalLayout.addWidget(self.home_PushButton)
        self.settings_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.settings_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.settings_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.settings_PushButton.setIcon(QtGui.QIcon(settings_png))
        self.settings_PushButton.setObjectName("settings_PushButton")
        self.horizontalLayout.addWidget(self.settings_PushButton)
        self.horizontalLayout_2.addWidget(self.wpWidget_5)

        self.urlbar = LineEdit(self.wpWidget_3)
        self.urlbar.setMinimumSize(QtCore.QSize(300, 28))
        self.urlbar.setMaximumSize(QtCore.QSize(16777215, 28))
        self.urlbar.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(27, 27, 27);\n"
"    border-radius:12px;\n"
"    color:rgb(240, 240, 240);\n"
"    padding-left:15px;\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgba(99, 173, 229, 150);\n"
"}")
        self.urlbar.setObjectName("urlbar")


        self.horizontalLayout_2.addWidget(self.urlbar)
        self.verticalLayout_2.addWidget(self.wpWidget_3)
        self.wpWidget_4 = QtWidgets.QWidget(self.wpWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wpWidget_4.sizePolicy().hasHeightForWidth())
        self.wpWidget_4.setSizePolicy(sizePolicy)
        self.wpWidget_4.setObjectName("wpWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wpWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.wpWidget_4)
        self.verticalLayout.addWidget(self.wpWidget_2)

        # settings win
        self.verticalLayoutWidget = QtWidgets.QWidget(wpWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(2, 42, 330, 790))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 5))
        self.label_5.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 5))
        self.label_4.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.AllowJavascript_checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.AllowJavascript_checkBox.setFont(font)
        self.AllowJavascript_checkBox.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.AllowJavascript_checkBox.setObjectName("AllowJavascript_checkBox")
        self.verticalLayout.addWidget(self.AllowJavascript_checkBox)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 5))
        self.label_10.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.SaveAndOpenTabsOnNextSession_checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.SaveAndOpenTabsOnNextSession_checkBox.setFont(font)
        self.SaveAndOpenTabsOnNextSession_checkBox.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.SaveAndOpenTabsOnNextSession_checkBox.setObjectName("SaveAndOpenTabsOnNextSession_checkBox")
        self.verticalLayout.addWidget(self.SaveAndOpenTabsOnNextSession_checkBox)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 5))
        self.label_3.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.EnableADblocker_checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.EnableADblocker_checkBox.setFont(font)
        self.EnableADblocker_checkBox.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.EnableADblocker_checkBox.setObjectName("EnableADblocker_checkBox")
        self.verticalLayout.addWidget(self.EnableADblocker_checkBox)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 5))
        self.label.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.EnableTrackerblocker_checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.EnableTrackerblocker_checkBox.setFont(font)
        self.EnableTrackerblocker_checkBox.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.EnableTrackerblocker_checkBox.setObjectName("EnableTrackerblocker_checkBox")
        self.verticalLayout.addWidget(self.EnableTrackerblocker_checkBox)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 5))
        self.label_11.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setMaximumSize(QtCore.QSize(700, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.DefaultSearchEngine_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.DefaultSearchEngine_comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.DefaultSearchEngine_comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.DefaultSearchEngine_comboBox.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.DefaultSearchEngine_comboBox.setFrame(True)
        self.DefaultSearchEngine_comboBox.setObjectName("DefaultSearchEngine_comboBox")
        self.DefaultSearchEngine_comboBox.addItem("")
        self.DefaultSearchEngine_comboBox.addItem("")
        self.DefaultSearchEngine_comboBox.addItem("")
        self.verticalLayout.addWidget(self.DefaultSearchEngine_comboBox)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 5))
        self.label_14.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 5))
        self.label_15.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.UserAgentSwitcher_checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.UserAgentSwitcher_checkBox.setFont(font)
        self.UserAgentSwitcher_checkBox.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.UserAgentSwitcher_checkBox.setObjectName("UserAgentSwitcher_checkBox")
        self.verticalLayout.addWidget(self.UserAgentSwitcher_checkBox)
        self.UserAgentMode_comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.UserAgentMode_comboBox.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.UserAgentMode_comboBox.setObjectName("UserAgentMode_comboBox")
        self.UserAgentMode_comboBox.addItem("")
        self.UserAgentMode_comboBox.addItem("")
        self.verticalLayout.addWidget(self.UserAgentMode_comboBox)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.CurrentUserAgent_plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.CurrentUserAgent_plainTextEdit.setMaximumSize(QtCore.QSize(99999, 50))
        self.CurrentUserAgent_plainTextEdit.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.CurrentUserAgent_plainTextEdit.setPlainText("")
        self.CurrentUserAgent_plainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.CurrentUserAgent_plainTextEdit.setObjectName("CurrentUserAgent_plainTextEdit")
        self.verticalLayout.addWidget(self.CurrentUserAgent_plainTextEdit)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.CustomUserAgent_plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.CustomUserAgent_plainTextEdit.setMaximumSize(QtCore.QSize(99999, 50))
        self.CustomUserAgent_plainTextEdit.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.CustomUserAgent_plainTextEdit.setPlainText("")
        self.CustomUserAgent_plainTextEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.CustomUserAgent_plainTextEdit.setObjectName("CustomUserAgent_plainTextEdit")
        self.verticalLayout.addWidget(self.CustomUserAgent_plainTextEdit)
        self.UpdateUserAgent_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.UpdateUserAgent_pushButton.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.UpdateUserAgent_pushButton.setFlat(False)
        self.UpdateUserAgent_pushButton.setObjectName("UpdateUserAgent_pushButton")
        self.verticalLayout.addWidget(self.UpdateUserAgent_pushButton)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        spacerItem = QtWidgets.QSpacerItem(88, 438, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        # hide settings window by default
        self.verticalLayoutWidget.hide()

        # set auto completer for the url bar
        from dep.func import comp_data
        completer = QCompleter(comp_data.data)
        self.urlbar.setCompleter(completer)

        self.retranslateUi(wpWidget)
        QtCore.QMetaObject.connectSlotsByName(wpWidget)

        # set universal style
        self.setStyleSheet("""
            QLineEdit { color: rgb(255, 255, 255); }
            QCheckBox { color: rgb(255, 255, 255); }
            QPlainTextEdit { color: rgb(255, 255, 255); }
            QLabel { color: rgb(255, 255, 255); }
            QComboBox { color: rgb(255, 255, 255); }
            QListView { color: rgb(255, 255, 255); }
            QPushButton { color: rgb(255, 255, 255); }
        """)

        # set tooltips
        self.settings_PushButton.setToolTip('Open Settings Window')  
        self.home_PushButton.setToolTip("return to Homepage")
        self.reload_PushButton.setToolTip("reload current page")
        self.back_PushButton.setToolTip("back")
        self.forward_PushButton.setToolTip("forward")
        # settings tooltips
        self.AllowJavascript_checkBox.setToolTip("Disable Javascript to load in your browser \n"
            "(may break some sites but improves your privacy)")
        self.SaveAndOpenTabsOnNextSession_checkBox.setToolTip("Open Tabs that where open \n"
            "when you closed the Browser")
        self.EnableADblocker_checkBox.setToolTip("Block some ads on a site \n"
            "(may not block every ad and break sites)")
        self.EnableTrackerblocker_checkBox.setToolTip("Block some trackers on a site \n"
            "(may not block every Tracker)")
        self.UserAgentSwitcher_checkBox.setToolTip("Change your user Agent \n"
            "(may break some sites but improves your privacy)")
        self.UpdateUserAgent_pushButton.setToolTip("Apply selected User Agent on all Tabs")

        # set tooltip duration and style
        self.setToolTipDuration(50)

    def retranslateUi(self, wpWidget):
        _translate = QtCore.QCoreApplication.translate
        # wpWidget.setWindowTitle(_translate("wpWidget", "x"))
        self.label_2.setText(_translate("wpWidget", "Settings"))
        self.AllowJavascript_checkBox.setText(_translate("wpWidget", "Allow Javascript"))
        self.SaveAndOpenTabsOnNextSession_checkBox.setText(_translate("wpWidget", "Save Tabs and open on next session"))
        self.EnableADblocker_checkBox.setText(_translate("wpWidget", "Enable ADblocker"))
        self.label_9.setText(_translate("wpWidget", "Advertisements Blocked (since installation):"))
        self.EnableTrackerblocker_checkBox.setText(_translate("wpWidget", "Enable Tracker-blocker"))
        self.label_6.setText(_translate("wpWidget", "Trackers Blocked (since installation):"))
        self.label_13.setText(_translate("wpWidget", "Default Search Engine"))
        self.UserAgentSwitcher_checkBox.setText(_translate("wpWidget", "User Agent switcher"))
        self.UserAgentMode_comboBox.setItemText(0, _translate("wpWidget", "Custom"))
        self.UserAgentMode_comboBox.setItemText(1, _translate("wpWidget", "Random"))
        self.label_7.setText(_translate("wpWidget", "Current User Agent:"))
        self.label_8.setText(_translate("wpWidget", "Custom User Agent:"))
        self.UpdateUserAgent_pushButton.setText(_translate("wpWidget", "Update User Agent"))
        self.DefaultSearchEngine_comboBox.setItemText(0, _translate("wpWidget", "google.com"))
        self.DefaultSearchEngine_comboBox.setItemText(1, _translate("wpWidget", "duckduckgo.com"))
        self.DefaultSearchEngine_comboBox.setItemText(2, _translate("wpWidget", "bing.com"))
        