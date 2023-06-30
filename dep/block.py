from PyQt5 import QtWebEngineCore#
from dep.func import log
import configparser
import requests
import os

# import ad block parser
from adblockparser import AdblockRules

# get and define dir´s
current_dir = os.path.dirname(os.path.realpath(__file__))

AdblockRules_paths = []

RULES_AD = {
    "easylist_en": "https://easylist-downloads.adblockplus.org/easylist.txt",
    "easylist_ko": "https://easylist-downloads.adblockplus.org/koreanlist+easylist.txt",
    "adblockplus": "https://gh-pages.ewpratten.com/youtube_ad_blocklist/adblockplus.txt",
    "easylist_thirdparty": "https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_thirdparty.txt",
    "easylist_adservers": "https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt",
}   
RULES_TRACKER = {
    "easyprivacy": "https://easylist.to/easylist/easyprivacy.txt",
}

RULES_AD_local = {
    "easylist_en": [current_dir+"\\rules\\ADblockrules\\ADlist_EASYLIST_EN.txt", "0"],                 # index 0
    "easylist_ko": [current_dir+"\\rules\\ADblockrules\\ADlist_EASYLIST_KO.txt", "1"],                 # index 1
    "adblockplus": [current_dir+"\\rules\\ADblockrules\\ADlist_ADBLOCKPLUS.txt", "2"],                 # index 2
    "easylist_thirdparty": [current_dir+"\\rules\\ADblockrules\\ADlist_EASYLIST_THIRDPARTY.txt", "3"], # index 3
    "easylist_adservers": [current_dir+"\\rules\\ADblockrules\\ADlist_EASYLIST_ADSERVERS.txt", "4"],   # index 4
}
RULES_TRACKER_local = {
    "easyprivacy": [current_dir+"\\rules\\Trackerblockrules\\TR_EASYPRIVACY.txt", "0"],     # index 0
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
    return
    for key, value in RULES_AD.items():
        with open(os.path.join(current_dir, f"rules/ADblockrules/ADlist_{key.upper()}.txt"), 'w+', encoding="utf-8") as f:
            f.writelines(text[key])
            log("", f"Blocker: Rules for {key.upper()} updated")

    for key, value in RULES_TRACKER.items():
        with open(os.path.join(current_dir, f"rules/Trackerblockrules/TR_{key.upper()}.txt"), 'w+', encoding="utf-8") as f:
            f.writelines(text[key])
            log("", f"Blocker: Rules for {key.upper()} updated")

def ReadRules(path):
    # read content in chunks
    with open(path, 'r', encoding="utf_8") as file:
        lines = [line.strip().replace(',', '') for line in file]
        file.close()

    print (str(lines))
    return [str(lines)]


class Block():
    log("", "Blocker Activated")

    # update rules
    UpdateRules()



# define rules
rules1        = AdblockRules(ReadRules(RULES_AD_local["easylist_en"][0]))
rules2        = AdblockRules(ReadRules(RULES_AD_local["easylist_ko"][0]))
rules3        = AdblockRules(ReadRules(RULES_AD_local["easylist_thirdparty"][0]))
rules4        = AdblockRules(ReadRules(RULES_AD_local["easylist_adservers"][0]))
rulesyt       = AdblockRules(ReadRules(RULES_AD_local["adblockplus"][0]))
rulestracker  = AdblockRules(ReadRules(RULES_TRACKER_local["easyprivacy"][0]))
options = {'script': True, 'third-party': True}

def checkBlock_ads(url):
    # check english rules
    easylist_en_Checked = config["lists"]["easylist_en"]
    if easylist_en_Checked == "True":
        if rules1.should_block(url, options):
            return True

    # check korean rules
    easylist_ko_Checked = config["lists"]["easylist_ko"]
    if easylist_ko_Checked == "True":
        if rules2.should_block(url, options):
            return True
    
    # check thirdparty rules
    easylist_thirdparty_Checked = config["lists"]["easylist_thirdparty"]
    if easylist_thirdparty_Checked == "True":
        if rules3.should_block(url, options):
            return True
        
    # check adservers rules
    easylist_adservers_Checked = config["lists"]["easylist_adservers"]
    if easylist_adservers_Checked == "True":
        if rules4.should_block(url, options):
            return True

    # check youtube rules
    adblockplus_Checked = config["lists"]["adblockplus"]
    if adblockplus_Checked == "True":
        if rulesyt.should_block(url, options):
            return True

def checkBlock_trackers(url):
    # check tracker(1) rules
    if rulestracker.should_block(url, options):
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
                print (url)
                # block url
                info.block(True)
                # add to total blocked count
                config["values"]["blocked_ads"] = str(int(config["values"]["blocked_ads"])+1)
                return

        # check if TrackerBlock is activated
        if config['settings']['trackerblocker'] == "True":
            # check if url should be blocked
            if checkBlock_trackers(url) == True:
                print (url)
                # block url
                info.block(True)
                # add to total blocked count
                config["values"]["blocked_trackers"] = str(int(config["values"]["blocked_trackers"])+1)
                return  

        # save to config
        with open(config_dir, 'w') as configfile:
            config.write(configfile)