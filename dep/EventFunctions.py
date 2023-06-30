from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl, Qt
import os

from dep.func import log, config, config_dir

current_dir = os.path.dirname(os.path.realpath(__file__))

# events (run func when checkbox state was changed)
# allow javascript
def AllowJavascript_(self):
    if self.AllowJavascript_checkBox.isChecked():
        # on
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        # save setting
        config['settings']['Javascript'] = "True"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)
        log("", "javascript enabled and saved")
    else:
        # off
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, False)
        # save setting
        config['settings']['Javascript'] = "False"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)
        log("", "javascript disabled and saved")
    return

# enable ADblocker
def EnableADblocker_(self):
    if self.EnableADblocker_checkBox.isChecked():
        # on
        config['settings']['ADblocker'] = "True"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)        
        log("", "ADblocker enabled and saved")
    else:
        # off
        config['settings']['ADblocker'] = "False"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)
        log("", "ADblocker disabled and saved")
    return

# enable Tracker-blocker
def EnableTrackerblocker_(self):
    if self.EnableTrackerblocker_checkBox.isChecked():
        # on
        config['settings']['trackerblocker'] = "True"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)        
        log("", "Tracker-blocker enabled and saved")
    else:
        # off
        config['settings']['trackerblocker'] = "False"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)
        log("", "Tracker-blocker disabled and saved")
    return

# enable User Agent switcher
def UserAgent_(self):
    if self.UserAgentSwitcher_checkBox.isChecked():
        # on
        config['useragent']['useragent'] = "True"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)       
    else:
        # off
        config['useragent']['useragent'] = "False"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)
    log("", "User Agent switcher saved")
    return

# combobox user agent
def UserAgent_combobox(self):
    if self.UserAgentMode_comboBox.currentText() == "Custom":
        # custom
        config['useragent']['useragent_combobox'] = "Custom"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)
        log("", "User Agent switcher mode applied")    
    else:
        # random
        config['useragent']['useragent_combobox'] = "Random"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)
        log("", "User Agent switcher mode applied")
    return

# save and load tabs on next session
def SessionTabs_(self):
    if self.SaveAndOpenTabsOnNextSession_checkBox.isChecked():
        # on
        config["tabs"]["openloadtabs"] = "True"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)  
        log("", "Save and load tabs enabled and saved")     
    else:
        # off
        config["tabs"]["openloadtabs"] = "False"
        with open(config_dir, 'w') as configfile:
            config.write(configfile)
        log("", "Save and load tabs disabled and saved")
    return


# default serach engine
def SearchPage_(self):
    def UpdateEngine(self, engine):
        # update homepage tab
        self.tabs.setCurrentIndex(0)
        self.tabs.currentWidget().setUrl(QUrl(engine))
    # check selected search engine

    # google
    if self.DefaultSearchEngine_comboBox.currentText() == "google.com":
       engine = "https://www.google.com"

    # duckduckgo
    if self.DefaultSearchEngine_comboBox.currentText() == "duckduckgo.com":
        engine = "https://duckduckgo.com"

    # bing
    if self.DefaultSearchEngine_comboBox.currentText() == "bing.com":
        engine = "https://www.bing.com"  

    UpdateEngine(self, engine)

    self.search_address = engine
    config["startpage"]["search_address"] = self.search_address

    # save config
    with open(config_dir, 'w') as configfile:
        config.write(configfile)

    log("", "Search engine saved and applied")


def Lists_(self, RULES_AD_local, RULES_TRACKER_local):
    # check what lists are checked and not and save values

    # ad blocker lists
    for name, keys in RULES_AD_local.items():
        index =  keys[1]
        item = self.ADblockerLists_comboBox.model().item(int(index))
        if item.checkState() == Qt.Checked:
            config["lists"][str(name)] = "True"
        else:
            config["lists"][str(name)] = "False"

    # tracker blocker lists
    for name, keys in RULES_TRACKER_local.items():
        index =  keys[1]
        item = self.TrackerblockerLists_comboBox.model().item(int(index))
        if item.checkState() == Qt.Checked:
            config["lists"][str(name)] = "True"
        else:
            config["lists"][str(name)] = "False"

    with open(config_dir, 'w') as configfile:
        config.write(configfile)