from PyQt5.QtCore import QByteArray, QBuffer, QIODevice, QUrl
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWebEngineWidgets import *
from fake_useragent import UserAgent
from PyQt5 import QtWebEngineCore
from datetime import datetime
import configparser
import requests
import re
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# init config and select file
config = configparser.ConfigParser()
config_dir = current_dir+'\\config\\config.ini'
config.read(config_dir)

class comp_data():
    data = [
    "github.com", "youtube.com", "twitch.tv", "reddit.com", "spotify.com", "github.com/cookie0o", "facebook.com", "wikipedia.com", "amazon.com", "instagram.com", "yahoo.com", "twitter.com",
    "naver.com", "bit.ly", "vk.com", "live.com", "gmail.com", "google.com", "duckduckgo.com"
    ]

# validate url
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

# log events and errors
def log(type, msg):
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    msg = str(msg)
    if type == "":
        print(f"[{time} +] "+msg)
    elif type == "placeholder":
        raise ("not implemented yet.")
    return

# reload all tabs
def reload_tabs(self):
    # reload all open tabs
    for i in range(self.tabs.count()):
        widget = self.tabs.widget(i)
        # Refresh the content of the widget
        widget.reload()
    return

# update user agent
def UpdateUserAgent(self, Settings_Agent):
    # check if enabled
    if self.UserAgentSwitcher_checkBox.isChecked() == False:
        # reset user agent
        self.tabs.currentWidget().page().profile().setHttpUserAgent("")
        # clear old values
        self.CustomUserAgent_plainTextEdit.clear()
        self.CurrentUserAgent_plainTextEdit.clear()
        # display current user agent to user
        CurrentUserAgent = self.tabs.currentWidget().page().profile().httpUserAgent()
        self.CurrentUserAgent_plainTextEdit.insertPlainText(str(CurrentUserAgent))
        # reload browser
        reload_tabs(self)
        return
    else:
        pass
    # set custom user agent
    if self.UserAgentMode_comboBox.currentText() == "Custom":
        # show all elements for input and move button down to update
        self.CustomUserAgent_plainTextEdit.show()
        self.label_8.show()
        try:
            # get custom user agent
            if Settings_Agent == "":
                CustomUserAgent = self.CustomUserAgent_plainTextEdit.toPlainText()
                config["useragent"]["customuseragent"] = str(CustomUserAgent)
            else:
                CustomUserAgent = Settings_Agent
            # apply User Agent
            self.tabs.currentWidget().page().profile().setHttpUserAgent(str(CustomUserAgent))
            log("", "Custom User Agent set")
            # save settings
            config['useragent']['useragent_combobox'] = "Custom"
            with open(config_dir, 'w') as configfile:
                config.write(configfile)
        except Exception as e:
            raise (e)

    # set random client agent
    elif self.UserAgentMode_comboBox.currentText() == "Random":
        # hide all elements for input and move button up to update
        self.CustomUserAgent_plainTextEdit.hide()
        self.label_8.hide()
        try:
            # get random user agent
            ua=UserAgent()
            RandomUserAgent_raw = ua["google chrome"]
            # add QtWebEngine/5.15.2 so the browser does not break
            raw1, raw2 = RandomUserAgent_raw.split("Gecko)")
            RandomUserAgent = str(raw1+" QtWebEngine/5.15.2 "+raw2)
            # apply User Agenr
            self.tabs.currentWidget().page().profile().setHttpUserAgent(str(RandomUserAgent))
            log("", "Random User Agent set")
            # save settings
            config['useragent']['useragent_combobox'] = "Random"
            with open(config_dir, 'w') as configfile:
                config.write(configfile)
        except Exception as e:
            raise (e)

    # clear old values
    self.CustomUserAgent_plainTextEdit.clear()
    self.CurrentUserAgent_plainTextEdit.clear()
    # display current user agent to user
    CurrentUserAgent = self.tabs.currentWidget().page().profile().httpUserAgent()
    self.CurrentUserAgent_plainTextEdit.insertPlainText(str(CurrentUserAgent))
    # reload all tabs
    reload_tabs(self)

# change tab title
def set_tab_title(i, browser, tabs, title):
    # check if tab title is provided if not get it
    if title is None:
        title = browser.page().title()

    # set tab title and shorten it after 25 chars
    if len(title) > 25:
        title = title[:25] + "..."
    tabs.setTabText(i, " "+title+" ") 