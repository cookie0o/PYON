from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QCompleter
import os

# get and define dir´s
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")


class CheckableComboBox(QtWidgets.QComboBox):
	def __init__(self):
		super().__init__()
		self._changed = False

		self.view().pressed.connect(self.handleItemPressed)

	def setItemChecked(self, index, checked=False):
		item = self.model().item(index, self.modelColumn()) # QStandardItem object

		if checked:
			item.setCheckState(QtCore.Qt.Checked)
		else:
			item.setCheckState(QtCore.Qt.Unchecked)

	def handleItemPressed(self, index):
		item = self.model().itemFromIndex(index)

		if item.checkState() == QtCore.Qt.Checked:
			item.setCheckState(QtCore.Qt.Unchecked)
		else:
			item.setCheckState(QtCore.Qt.Checked)
		self._changed = True


	def hidePopup(self):
		if not self._changed:
			super().hidePopup()
		self._changed = False

	def itemChecked(self, index):
		item = self.model().item(index, self.modelColumn())
		return item.checkState() == QtCore.Qt.Checked

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


class Ui_searchbar(object):
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
        self.wpWidget_3.setObjectName("wpWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wpWidget_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 10, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wpWidget_5 = QtWidgets.QWidget(self.wpWidget_3)
        self.wpWidget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.wpWidget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.wpWidget_5.setObjectName("wpWidget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wpWidget_5)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.back_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.back_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.back_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.back_PushButton.setObjectName("back_PushButton")
        self.horizontalLayout.addWidget(self.back_PushButton)
        self.forward_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.forward_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.forward_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.forward_PushButton.setObjectName("forward_PushButton")
        self.horizontalLayout.addWidget(self.forward_PushButton)
        self.reload_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.reload_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.reload_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.reload_PushButton.setObjectName("reload_PushButton")
        self.horizontalLayout.addWidget(self.reload_PushButton)
        self.settings_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.settings_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.settings_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.settings_PushButton.setObjectName("settings_PushButton")
		
        # self.horizontalLayout.addWidget(self.settings_PushButton)
        self.home_PushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.home_PushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.home_PushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.home_PushButton.setObjectName("home_PushButton")
        self.horizontalLayout.addWidget(self.home_PushButton)
        self.horizontalLayout_2.addWidget(self.wpWidget_5)

        self.urlbar = LineEdit(self.wpWidget_3)
        self.urlbar.setMinimumSize(QtCore.QSize(300, 28))
        self.urlbar.setMaximumSize(QtCore.QSize(16777215, 28))
        self.urlbar.setObjectName("urlbar")


        self.horizontalLayout_2.addWidget(self.urlbar)
		
        self.spacer = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.spacer)	
        self.horizontalLayout_2.addWidget(self.settings_PushButton)	

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
                        
        
        # read auto complete sites from txt
        with open((os.path.join(current_dir, "auto_complete_sites.txt")), 'r') as file:
            AutoCompleteWords = [line.strip() for line in file]
            # set auto completer for the url bar
            completer = QCompleter(AutoCompleteWords)
            self.urlbar.setCompleter(completer)
            # close the file
            file.close()


        QtCore.QMetaObject.connectSlotsByName(wpWidget)

        # set tooltips
        self.settings_PushButton.setToolTip('Open Settings Window')  
        self.home_PushButton.setToolTip("return to Homepage")
        self.reload_PushButton.setToolTip("reload current page")
        self.back_PushButton.setToolTip("back")
        self.forward_PushButton.setToolTip("forward")

        # set tooltip duration and style
        self.setToolTipDuration(50)
