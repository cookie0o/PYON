from PyQt5 import QtWebEngineCore
from dep.func import log
import configparser
import requests
import ctypes
import os

# import ad block parser
from adblockparser import AdblockRules

# get and define dir´s
current_dir = os.path.dirname(os.path.realpath(__file__))

# init shared c
lib = ctypes.cdll.LoadLibrary(current_dir+'\\c\\file_reader.so')
# Declare the return type and argument types of the C function
lib.read_file.restype = ctypes.c_char_p
lib.read_file.argtypes = [ctypes.c_char_p]

RULES_AD = {
    "en": "https://easylist-downloads.adblockplus.org/easylist.txt",
    "de": "https://easylist.to/easylistgermany/easylistgermany.txt",
    "ko": "https://easylist-downloads.adblockplus.org/koreanlist+easylist.txt",
    "Youtube": "https://gh-pages.ewpratten.com/youtube_ad_blocklist/adblockplus.txt",
}
RULES_TRACKER = {
    "list1": "https://easylist.to/easylist/easyprivacy.txt",
}

RULES_AD_local = {
    "en": current_dir+"\\rules\\ADblockrules\\ADlist_DE.txt",
    "de": current_dir+"\\rules\\ADblockrules\\ADlist_EN.txt",
    "ko": current_dir+"\\rules\\ADblockrules\\ADlist_KO.txt",
    "Youtube": current_dir+"\\rules\\ADblockrules\\ADlist_YOUTUBE.txt",
}
RULES_TRACKER_local= {
    "list1": current_dir+"\\rules\\Trackerblockrules\\TR_LIST1.txt",
}

response = {}
text = {}

for key, value in RULES_AD.items():
    response[key] = requests.get(value)
    text[key] = response[key].text

for key, value in RULES_TRACKER.items():
    response[key] = requests.get(value)
    text[key] = response[key].text

# init config and select file
config = configparser.ConfigParser()
config_dir = os.path.join(current_dir, 'config', 'config.ini')


def UpdateRules():
    for key, value in RULES_AD.items():
        with open(os.path.join(current_dir, f"rules/ADblockrules/ADlist_{key.upper()}.txt"), 'w+', encoding="utf-8") as f:
            f.writelines(text[key])
            log("", f"Blocker: Rules for {key.upper()} updated")

    for key, value in RULES_TRACKER.items():
        with open(os.path.join(current_dir, f"rules/Trackerblockrules/TR_{key.upper()}.txt"), 'w+', encoding="utf-8") as f:
            f.writelines(text[key])
            log("", f"Blocker: Rules for {key.upper()} updated")

def ReadRules(path):
    return ""

class Block():
    log("", "Blocker Activated")

    # update rules
    UpdateRules()



# define rules
rules1        = AdblockRules(ReadRules(RULES_AD_local["de"]), use_re2=True, max_mem=512*1024*1024)
rules2        = AdblockRules(ReadRules(RULES_AD_local["en"]), use_re2=True, max_mem=512*1024*1024)
rules3        = AdblockRules(ReadRules(RULES_AD_local["ko"]), use_re2=True, max_mem=512*1024*1024)
rulesyt       = AdblockRules(ReadRules(RULES_AD_local["Youtube"]), use_re2=True, max_mem=512*1024*1024)
rulestracker  = AdblockRules(ReadRules(RULES_TRACKER_local["list1"]), use_re2=True, max_mem=512*1024*1024)


def checkBlock_ads(url):
    # check german rules
    if rules1.should_block(url):
        return True
    
    # check english rules
    if rules2.should_block(url):
        return True

    # check korean rules
    if rules3.should_block(url):
        return True
    
    # check youtube rules
    if rulesyt.should_block(url):
        return True

def checkBlock_trackers(url):
    # check tracker(1) rules
    if rulestracker.should_block(url):
        return True


class WebEngineUrlRequestInterceptor(QtWebEngineCore.QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        # get url as string
        url = info.requestUrl().toString()

        # read block count
        config.read(config_dir)

        #print (checkBlock_ads(url))

        # check if adblock is activated
        if config['settings']['adblocker'] == "True":
            # check if url should be blocked
            if checkBlock_ads(url) == True:
                # block url
                info.block(True)
                # add to total blocked count
                config["values"]["blocked_ads"] = str(int(config["values"]["blocked_ads"])+1)
                return

        # check if TrackerBlock is activated
        if config['settings']['trackerblocker'] == "True":
            # check if url should be blocked
            if checkBlock_trackers(url) == True:
                # block url
                info.block(True)
                # add to total blocked count
                config["values"]["blocked_trackers"] = str(int(config["values"]["blocked_trackers"])+1)
                return  

        # save to config
        with open(config_dir, 'w') as configfile:
            config.write(configfile)