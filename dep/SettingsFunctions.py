from PyQt5.QtCore import Qt

def ApplySettings(self, config, log): 
    try:
        # javascript
        if config['settings']['javascript'] == "True":
            self.AllowJavascript_checkBox.setChecked(True)
        else:
            self.EnableADblocker_checkBox.setChecked(False)
        # ad blocker
        if config['settings']['adblocker'] == "True":
            self.EnableADblocker_checkBox.setChecked(True)
        else:
            self.EnableADblocker_checkBox.setChecked(False)
        # tracker blocker
        if config['settings']['trackerblocker'] == "True":
            self.EnableTrackerblocker_checkBox.setChecked(True)
        else:
            self.EnableTrackerblocker_checkBox.setChecked(False)
        # user agent
        if config["useragent"]["useragent_combobox"] == "Custom":
            self.UserAgentMode_comboBox.setCurrentIndex(0)
        else:
            self.UserAgentMode_comboBox.setCurrentIndex(1)
        if config["useragent"]["customuseragent"] != "":
            self.CustomUserAgent_plainTextEdit.insertPlainText(str(config["useragent"]["customuseragent"]))
        if config["useragent"]["useragent"] == "True":
            self.UserAgentSwitcher_checkBox.setChecked(True)
        else:
            self.UserAgentSwitcher_checkBox.setChecked(False) 
        # save and load tabs
        if config["tabs"]["openloadtabs"] == "True":
            self.SaveAndOpenTabsOnNextSession_checkBox.setChecked(True)
        else:
            self.SaveAndOpenTabsOnNextSession_checkBox.setChecked(False)  
        # get current search engine
        if  "https://www.google.com" == str(config['startpage']['search_address']):
            self.DefaultSearchEngine_comboBox.setCurrentIndex(0) 
        elif "https://duckduckgo.com" == str(config['startpage']['search_address']):
            self.DefaultSearchEngine_comboBox.setCurrentIndex(1) 
        elif "https://www.bing.com" == str(config['startpage']['search_address']):
            self.DefaultSearchEngine_comboBox.setCurrentIndex(2)

        # lists
        easylist_en_item = self.ADblockerLists_comboBox.model().item(0)
        if config["lists"]["easylist_en"] == "True":
            easylist_en_item.setCheckState(Qt.Checked)
        else:
            easylist_en_item.setCheckState(Qt.Unchecked)

        easylist_ko_item = self.ADblockerLists_comboBox.model().item(1)
        if config["lists"]["easylist_ko"] == "True":
            easylist_ko_item.setCheckState(Qt.Checked)
        else:
            easylist_ko_item.setCheckState(Qt.Unchecked)

        adblockplus_item = self.ADblockerLists_comboBox.model().item(2)
        if config["lists"]["adblockplus"] == "True":  
            adblockplus_item.setCheckState(Qt.Checked)
        else:
            adblockplus_item.setCheckState(Qt.Unchecked)

        easylist_thirdparty_item = self.ADblockerLists_comboBox.model().item(3)
        if config["lists"]["easylist_thirdparty"] == "True":
            easylist_thirdparty_item.setCheckState(Qt.Checked)
        else:
            easylist_thirdparty_item.setCheckState(Qt.Unchecked)

        easylist_adservers_item = self.ADblockerLists_comboBox.model().item(4)
        if config["lists"]["easylist_adservers"] == "True":
            easylist_adservers_item.setCheckState(Qt.Checked)
        else:
            easylist_adservers_item.setCheckState(Qt.Unchecked)

        easyprivacy_item = self.TrackerblockerLists_comboBox.model().item(0)
        if config["lists"]["easyprivacy"] == "True":  
            easyprivacy_item.setCheckState(Qt.Checked)
        else:
            easyprivacy_item.setCheckState(Qt.Unchecked)

        log("", "Settings applied")
    except Exception as e:
        raise (e)