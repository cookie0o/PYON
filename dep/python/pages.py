from PyQt5.QtCore import *
import os



# dir
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
config_pages_dir = (os.path.abspath(os.path.join(os.path.realpath(__file__), '../..')).replace("\\", "/") + "/config_pages/")


close_png = current_dir+'/UIres/close.png'
info_png = current_dir+'/UIres/info.png'

height = 2



class pages_vars():
    def vars(self):
        self.settings_page = os.path.join(config_pages_dir, "settings/index.html")
        self.file_pages = {
            "settings": self.settings_page
        }

        self.pages_paths = [
            self.settings_page
        ]


    def pages(self, pages_url):
        # remove prefix if there
        if self.prefix in pages_url:
            pages_url = (pages_url.replace(self.prefix, ""))

        # return
        return QUrl(str("file://"+(self.file_pages[pages_url])))
        


