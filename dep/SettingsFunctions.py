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

        log("", "Settings applied")
    except Exception as e:
        raise (e)