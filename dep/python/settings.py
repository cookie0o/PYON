from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtNetwork import QNetworkProxy
import configparser
import json
import os

from PyQt5.QtCore import *

# import outside python
from dep.UIdep.colors import set_style
from dep.python.functions import *
from dep.python.fake import *


# dirs
dep_dir = os.path.abspath(os.path.join(os.path.realpath(__file__), '..', '..')).replace("\\", "/")

# get config
config_file = os.path.join(dep_dir, "config.cfg")
config = configparser.ConfigParser()
config.read(config_file)

# default values
default_search_engine = "https://start.duckduckgo.com"
default_search_engine_addr = "https://duckduckgo.com/?&q="
tor_default_search_engine = "https://start.duckduckgo.com"
tor_default_search_engine_addr = "https://duckduckgo.com/?&q="
default_theme_name = "Dark"

developer = config['Developer']
general = config['General']
custom = config['Custom'] 
blocker = config['Blocker']
useragent = config['User.Agent']
privacy = config['Privacy']
proxy = config['Proxy']


class settings():
    def settings_load(self): 
        config.read(config_file)
        developer = config['Developer']
        general = config['General']
        custom = config['Custom']
        blocker = config['Blocker']
        useragent = config['User.Agent']
        privacy = config['Privacy']
        proxy = config['Proxy']
        
        # [Developer]
        debug_javaScriptConsoleMessage = developer["debug_javaScriptConsoleMessage"]
        if debug_javaScriptConsoleMessage == "True": self.debug_javaScriptConsoleMessage = True
        else: self.debug_javaScriptConsoleMessage = False

        # [General]
        javascript = general["javascript"]
        if javascript == "True": self.javascript = True
        else: self.javascript = False
        self.javascript = True
        
        theme_name = general["theme_name"]
        if theme_name == "": self.theme_name = default_theme_name
        else: self.theme_name = theme_name
        
        # [Custom]
        search_engine = custom["search_engine"]
        if search_engine == "": self.search_engine = default_search_engine
        else: self.search_engine = search_engine
        search_engine_addr = custom["search_engine_addr"]
        if search_engine_addr == "": self.search_engine_addr = default_search_engine_addr
        else: self.search_engine_addr = search_engine_addr
        #
        tor_search_engine = custom["tor_search_engine"]
        if tor_search_engine == "": self.tor_search_engine = tor_default_search_engine
        else: self.tor_search_engine = tor_search_engine
        tor_search_engine_addr = custom["tor_search_engine_addr"]
        if tor_search_engine_addr == "": self.tor_search_engine_addr = tor_default_search_engine_addr
        else: self.tor_search_engine_addr = tor_search_engine_addr    
        
        # [Blocker]
        # ad blocking
        ad_blocker = blocker["ad_blocker"]
        if ad_blocker == "True": self.ad_blocker = True
        else: self.ad_blocker = False
        #
        ad_auto_update = blocker["ad_auto_update"]
        if ad_auto_update == "True": self.ad_auto_update = True
        else: self.ad_auto_update = False
        #
        ad_lists = blocker["ad_lists"]
        if ad_lists == "": self.ad_lists = ""
        else: self.ad_lists = ad_lists
        
        # privacy blocking
        privacy_blocker = blocker["privacy_blocker"]
        if privacy_blocker == "True": self.privacy_blocker = True
        else: self.privacy_blocker = False
        #
        privacy_auto_update = blocker["privacy_auto_update"]
        if privacy_auto_update == "True": self.privacy_auto_update = True
        else: self.privacy_auto_update = False
        #
        privacy_lists = blocker["privacy_lists"]
        if privacy_lists == "": self.privacy_lists = ""
        else: self.privacy_lists = privacy_lists
        
        # cookie blocking
        cookie_blocker = blocker["cookie_blocker"]
        if cookie_blocker == "True": self.cookie_blocker = True
        else: self.cookie_blocker = False
        #
        cookie_auto_update = blocker["cookie_auto_update"]
        if cookie_auto_update == "True": self.cookie_auto_update = True
        else: self.cookie_auto_update = False
        #
        cookie_lists = blocker["cookie_lists"]
        if cookie_lists == "": self.cookie_lists = ""
        else: self.cookie_lists = cookie_lists

        # youtube blocking
        youtube_ad_blocker = blocker["youtube_ad_blocker"]
        if youtube_ad_blocker == "True": self.youtube_ad_blocker = True
        else: self.youtube_ad_blocker = False

        # [User.Agent]
        user_agent_option = useragent["user_agent_option"]
        if user_agent_option == "": self.user_agent_option = ""
        else: self.user_agent_option = user_agent_option
        #
        custom_useragent = useragent["custom_useragent"]
        if custom_useragent == "": self.custom_useragent = ""
        else: self.custom_useragent = custom_useragent
        
        # [Privacy]
        RouteTrafficThroughTor = privacy["RouteTrafficThroughTor"]
        if RouteTrafficThroughTor == "True": self.RouteTrafficThroughTor = True
        else: self.RouteTrafficThroughTor = False
        #
        TorSearchEngineBypass = privacy["TorSearchEngineBypass"]
        if TorSearchEngineBypass == "True": self.TorSearchEngineBypass = True
        else: self.TorSearchEngineBypass = False
        #
        TrackingLinkProtection = privacy["TrackingLinkProtection"]
        if TrackingLinkProtection == "True": self.TrackingLinkProtection = True
        else: self.TrackingLinkProtection = False
        
        # [Proxy]
        proxy_option = proxy["proxy_option"]
        if proxy_option == "": self.proxy_option = ""
        else: self.proxy_option = proxy_option
        #
        custom_proxy_address_input = proxy["custom_proxy_address_input"]
        if custom_proxy_address_input == "": self.custom_proxy_address_input = ""
        else: self.custom_proxy_address_input = custom_proxy_address_input
        #
        custom_proxy_port_input = proxy["custom_proxy_port_input"]
        if custom_proxy_port_input == "": self.custom_proxy_port_input = 0000
        else: self.custom_proxy_port_input = custom_proxy_port_input
        #
        applyProxy = proxy["applyProxy"]
        if applyProxy == "True": self.applyProxy = True
        else: self.applyProxy = False   
        
        
    def settings_save(self):
        # [Developer]
        developer["debug_javaScriptConsoleMessage"] = str(self.debug_javaScriptConsoleMessage)

        # [General]
        general["javascript"] = str(self.javascript)
        general["theme_name"] = str(self.theme_name)
        
        # [Custom]
        custom["search_engine"] = str(self.search_engine)
        custom["search_engine_addr"] = str(self.search_engine_addr)
        #
        custom["tor_search_engine"] = str(self.tor_search_engine)
        custom["tor_search_engine_addr"] = str(self.tor_search_engine_addr)
        
        # [Blocker]
        # ad blocking
        blocker["ad_blocker"] = str(self.ad_blocker)
        #
        blocker["ad_auto_update"] = str(self.ad_auto_update)
        #
        blocker["ad_lists"] = str(self.ad_lists)
        
        # privacy blocking
        blocker["privacy_blocker"] = str(self.privacy_blocker)
        #
        blocker["privacy_auto_update"] = str(self.privacy_auto_update)
        #
        blocker["privacy_lists"] = str(self.privacy_lists)
        
        # cookie blocking
        blocker["cookie_blocker"] = str(self.cookie_blocker)
        #
        blocker["cookie_auto_update"] = str(self.cookie_auto_update)
        #
        blocker["cookie_lists"] = str(self.cookie_lists)
        
        # youtube ad blocking
        blocker["youtube_ad_blocker"] = str(self.youtube_ad_blocker)
        
        # [User.Agent]
        useragent["user_agent_option"] = str(self.user_agent_option)
        #
        useragent["custom_useragent"] = str(self.custom_useragent)
        
        # [Privacy]
        privacy["RouteTrafficThroughTor"] = str(self.RouteTrafficThroughTor)
        #
        privacy["TorSearchEngineBypass"] = str(self.TorSearchEngineBypass)
        #
        privacy["TrackingLinkProtection"] = str(self.TrackingLinkProtection)
        
        # [Proxy]
        proxy["proxy_option"] = str(self.proxy_option)  
        #
        proxy["custom_proxy_address_input"] = str(self.custom_proxy_address_input)
        #
        proxy["custom_proxy_port_input"] = str(self.custom_proxy_port_input)
        # 
        proxy["applyProxy"] = str(self.applyProxy)
        
  
        with open(config_file, 'w') as configfile:
            config.write(configfile)


    def settings_apply(self):
        # save the settings before applying them
        self.settings_save()
        
        self.proxy = QNetworkProxy()
        
        # apply all settings than can be applied
        
        # [Developer]
        if self.debug_javaScriptConsoleMessage:
            qInstallMessageHandler(None)
        else:
            qInstallMessageHandler(functions.misc.MessageHandler)

        # [General]
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, self.javascript)
            
        # [User.Agent]
        # check if random user agent should be used
        if self.user_agent_option == "random":
            # generate and set a random useragent
            self.profile.setHttpUserAgent(fake.useragent())
        
        # check if custom user agent should be used
        elif self.user_agent_option == "custom":
            # get and set useragent
            self.profile.setHttpUserAgent(str(self.custom_useragent))
            
         # check if the default user agent should be used (and default if nothing is set)
        else:
            self.profile.setHttpUserAgent("")
            
            
        # [Privacy]
        # rote traffic through tor
        if self.RouteTrafficThroughTor:
            # set proxy
            self.proxy.setType(QNetworkProxy.Socks5Proxy)
            self.proxy.setHostName("127.0.0.1")
            self.proxy.setPort(self.socks_port)
        else:
            QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.NoProxy))
            
            
        # [Proxy]
        if not self.RouteTrafficThroughTor:
            # set custom proxy
            if self.proxy_option == "custom":
                self.proxy.setType(QNetworkProxy.Socks5Proxy)
                self.proxy.setHostName(str(self.custom_proxy_address_input))
                self.proxy.setPort(int(self.custom_proxy_port_input))
            
            # Deactivate proxy
            else:
                # Deactivate proxy
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.NoProxy))
            
        # set proxy
        QNetworkProxy.setApplicationProxy(self.proxy) 

        # reload the browser so settings can apply except pages pages
        self.browser.reload()
        
        # update/set stylesheets
        set_style(self)


    def settings_page_fetch(self, localStorageStates):
        # convert str back to dict 
        localStorageStates = json.loads(localStorageStates)
        
        if localStorageStates is not None:
            self.javascript                 = localStorageStates.get("javascript")
            self.theme_name                 = localStorageStates.get("theme_name")
            self.ad_blocker                 = localStorageStates.get("ad_blocker")
            self.cookie_blocker             = localStorageStates.get("cookie_blocker")
            self.privacy_blocker            = localStorageStates.get("privacy_blocker")
            self.proxy_option               = localStorageStates.get("proxyOption")
            self.custom_proxy_address_input = localStorageStates.get("customProxyAddress")
            self.custom_proxy_port_input    = localStorageStates.get("customProxyPort")
            self.RouteTrafficThroughTor     = localStorageStates.get("routeThroughTor")
            self.TorSearchEngineBypass      = localStorageStates.get("torSearchEngineBypass")
            self.TrackingLinkProtection     = localStorageStates.get("trackingLinkProtection")
            self.youtube_ad_blocker         = localStorageStates.get("youtube_ad_blocker")
            self.user_agent_option          = localStorageStates.get("userAgentOption")
            self.custom_useragent           = localStorageStates.get("custom_useragent")

            # save and apply settings
            self.settings_save()
            self.settings_apply()
        return


    def inject_qt(self, i, tabs):
        try:
            widget = tabs.widget(i)

            if not (widget.page().url().toString()).replace("file:///", "") == self.settings_page:
                return

            widget.page().setWebChannel(self.channel)
            widget.page().loadFinished.connect(lambda: inject(widget))
        except:
            return
        
        def inject(widget):
            widget.page().runJavaScript("""
                (function() {
                    // Check if the script is already present to avoid adding it multiple times
                    if (!document.querySelector('script[src="qrc:///qtwebchannel/qwebchannel.js"]')) {
                        var script = document.createElement('script');
                        script.src = 'qrc:///qtwebchannel/qwebchannel.js';
                        script.onload = function() {
                            var webChannel = new QWebChannel(qt.webChannelTransport, function(channel) {
                                const saveBtn = document.getElementById('save_btn');

                                // Remove any existing click event listener to avoid duplicates
                                saveBtn.removeEventListener('click', handleSaveBtnClick);

                                // Add click event listener to the save button
                                saveBtn.addEventListener('click', handleSaveBtnClick);

                                function handleSaveBtnClick() {
                                    window.jsInterface = channel.objects.JsInterface;

                                    let localStorageStates = {};
                                    for (let i = 0; i < localStorage.length; i++) {
                                        const key = localStorage.key(i);
                                        const value = localStorage.getItem(key);
                                        // Set key-value pair in the object
                                        localStorageStates[key] = JSON.parse(value);
                                    }

                                    const localStorageStatesJson = JSON.stringify(localStorageStates);

                                    console.log(localStorageStatesJson);
                                    jsInterface.settings(localStorageStatesJson);
                                }
                            });
                        };
                        document.head.appendChild(script);
                    } else {
                        // If the script is already loaded, set up the web channel directly
                        var webChannel = new QWebChannel(qt.webChannelTransport, function(channel) {
                            const saveBtn = document.getElementById('save_btn');

                            // Remove any existing click event listener to avoid duplicates
                            saveBtn.removeEventListener('click', handleSaveBtnClick);

                            // Add click event listener to the save button
                            saveBtn.addEventListener('click', handleSaveBtnClick);

                            function handleSaveBtnClick() {
                                window.jsInterface = channel.objects.JsInterface;

                                let localStorageStates = {};
                                for (let i = 0; i < localStorage.length; i++) {
                                    const key = localStorage.key(i);
                                    const value = localStorage.getItem(key);
                                    // Set key-value pair in the object
                                    localStorageStates[key] = JSON.parse(value);
                                }

                                const localStorageStatesJson = JSON.stringify(localStorageStates);

                                console.log(localStorageStatesJson);
                                jsInterface.settings(localStorageStatesJson);
                            }
                        });
                    }
                })();
            """)
        return
