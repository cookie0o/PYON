from PyQt5.QtCore import QThread
import stem.process
import requests
import time
import os
import re

tor_dir = (os.path.abspath(os.path.join(os.path.realpath(__file__), '..', '..')).replace("\\", "/")) + "/tor"


class TorProxy(QThread):
    def __init__(self, self_, parent=None):
        super(TorProxy, self).__init__(parent)
        self.self_ = self_
    
    def run(self):        
        # update GeoIpFile
        GeoIpFilePath = TorProxy.updateGeoIpFile("https://gitlab.torproject.org/tpo/core/tor/-/raw/main/src/config/geoip")

        # retry launching 5 times
        tor_file = os.path.join(tor_dir, "tor.exe")
        for i in range(0, 5):
            try:
                # launch tor as proxy 
                stem.process.launch_tor_with_config(
                    config = {
                        'SocksPort': str(self.self_.socks_port),
                        'ControlPort': str(self.self_.control_port),
                        'CookieAuthentication': '1',
                        'GeoIPFile': GeoIpFilePath,
                    },
                    init_msg_handler = lambda line: print(line) if line and re.search('Bootstrapped', line) else False,
                    tor_cmd = tor_file
                )
                time.sleep(0.1)
            except Exception as e:
                print(f"Attempt {i+1} failed: {e}")
                time.sleep(1)
            else:
                break
        return

    
    @staticmethod
    def updateGeoIpFile(url):
        try:
            # Extract the file name from the URL
            file_name = os.path.join(tor_dir, url.split("/")[-1])
            # Make a GET request to the raw GitHub URL
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Save the content to a local file
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(response.text)
            else:
                print(f"Failed to download {url}. Status code: {response.status_code}")
            
            return (os.path.join(tor_dir, file_name))
        except Exception as e:
            pass