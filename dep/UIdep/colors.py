from PyQt5 import QtGui
import os

# get and define dir´s
current_dir = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")


def theme(self):
    try:
        # Light mode
        if self.theme_name == "Light":
            background_color              = "rgb(240, 240, 240)"
            color                         = "rgb(20, 20, 20)"
            hover                         = "rgba(100, 100, 100, 0.3)"
            selected                      = "rgba(150, 150, 150, 0.3)"
            border                        = "rgba(20, 20, 20, 0.5)"
            focus_border                  = "rgba(30, 100, 150, 0.6)"

            tab_background_color          = "rgb(160, 160, 160)"
            tab_selected_background_color = "rgb(150, 150, 150)"
            tab_hover_background_color    = "rgb(180, 180, 180)"

            qlineedit_background_color    = "rgb(240, 240, 240)"
            
            # images
            back_png                      = current_dir+'/UIres/light/arrow-left.png'
            forward_png                   = current_dir+'/UIres/light/arrow-right.png'
            reload_png                    = current_dir+'/UIres/light/refresh.png'
            home_png                      = current_dir+'/UIres/light/home.png'
            connection_png                = current_dir+'/UIres/light/connection.png'
            settings_png                  = current_dir+'/UIres/light/settings.png'
            close_png                     = current_dir+'/UIres/light/close.png'
            window_png                    = current_dir+'/UIres/light/window.png'
            minimize_png                  = current_dir+'/UIres/light/minimize.png'
            close_small_png               = current_dir+'/UIres/light/close_small.png'
            close_gray_small_png          = current_dir+'/UIres/light/close_gray_small.png'
            
        # default to Dark if none
        else:
            background_color              = "rgb(35, 34, 39)"
            color                         = "rgb(255, 255, 255)"
            hover                         = "rgba(210, 210, 210, 30)"
            selected                      = "rgba(144, 144, 144, 30)"
            border                        = "rgba(255, 255, 255, 50)"
            focus_border                  = "rgba(99, 173, 229, 150)"
            
            tab_background_color          = "rgb(30, 29, 34)"
            tab_selected_background_color = "rgb(27, 27, 27)"
            tab_hover_background_color    = "rgb(10, 10, 10)"
            
            qlineedit_background_color    = "rgb(27, 27, 27)"
            
            # images
            back_png                      = current_dir+'/UIres/dark/arrow-left.png'
            forward_png                   = current_dir+'/UIres/dark/arrow-right.png'
            reload_png                    = current_dir+'/UIres/dark/refresh.png'
            home_png                      = current_dir+'/UIres/dark/home.png'
            connection_png                = current_dir+'/UIres/dark/connection.png'
            settings_png                  = current_dir+'/UIres/dark/settings.png'
            close_png                     = current_dir+'/UIres/dark/close.png'
            window_png                    = current_dir+'/UIres/dark/window.png'
            minimize_png                  = current_dir+'/UIres/dark/minimize.png'
            close_small_png               = current_dir+'/UIres/dark/close_small.png'
            close_gray_small_png          = current_dir+'/UIres/dark/close_gray_small.png'

            
        return {
            "background_color": background_color,
            "color": color,
            "hover": hover,
            "selected": selected,
            "border": border,
            "focus_border": focus_border,
            "tab_background_color": tab_background_color,
            "tab_selected_background_color": tab_selected_background_color,
            "tab_hover_background_color": tab_hover_background_color,
            "qlineedit_background_color": qlineedit_background_color,
            
            # images
            "back_png": back_png,
            "forward_png": forward_png,
            "reload_png": reload_png,
            "home_png": home_png,
            "connection_png": connection_png,
            "settings_png": settings_png,
            "close_png": close_png,
            "window_png": window_png,
            "minimize_png": minimize_png,
            "close_small_png": close_small_png,
            "close_gray_small_png": close_gray_small_png,
        }
    except Exception as e:
        print ("Get Theme Colors Error: "+e)
    
        
def set_style(self):
    try:
        # tab
        self.tabs.setStyleSheet("""
            QTabBar::close-button {
                image: url("""+theme(self)["close_gray_small_png"]+"""); 
            }

            QTabBar::close-button:selected {
                image: url("""+theme(self)["close_small_png"]+"""); 
            }

            QTabBar::close-button:hover {
                background-color: """+theme(self)["hover"]+""";
            }

            QTabBar::close-button:hover:selected {
                background-color: """+theme(self)["selected"]+""";
                border-radius:5px;
            }
            
            QTabBar {
                background-color: """+theme(self)["background_color"]+""";
                color: """+theme(self)["color"]+""";
            }

            QTabBar::tab {
                background-color: """+theme(self)["tab_background_color"]+""";
                margin: 0;

                height: 20px;
                font-size: 12px;

                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }

            QTabBar::tab:selected {
                background-color: """+theme(self)["tab_selected_background_color"]+""";
                border-top: 0.5px solid """+theme(self)["border"]+""";
                border-right: 0.5px solid """+theme(self)["border"]+""";
                border-left: 0.5px solid """+theme(self)["border"]+""";
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }

            QTabBar::tab:hover {
                background-color: """+theme(self)["tab_hover_background_color"]+""";
            }
        """)
        
        # search bar
        self.wpWidget_3.setStyleSheet("""
            QWidget#wpWidget_3 {
                background-color: """+theme(self)["background_color"]+""";
            }
        """)
        self.urlbar.setStyleSheet("""\
            QLineEdit {
                padding-right: 10%;
                background-color: """+theme(self)["qlineedit_background_color"]+""";
                border-radius: 7px;
                color: """+theme(self)["color"]+""";
                padding-left: 15px;
                border: 1px solid """+theme(self)["border"]+""";
            }
            QLineEdit:focus {
                border: 1px solid """+theme(self)["focus_border"]+""";
            }
            
            QAbstractItemView#completerPopup {
                border: 2px solid rgb(81, 81, 81);
                padding: 1px;
                border-radius: 15px;
            }      
        """)
        self.wpWidget_2.setStyleSheet("""
            QPushButton{
                background-color: """+theme(self)["background_color"]+""";
                font-size:17px;
            }
            QPushButton:hover{
                background-color: """+theme(self)["hover"]+""";
                border-radius:5px;
            }
        """) 
        

        # icons
        self.back_PushButton.setIcon(QtGui.QIcon(theme(self)["back_png"]))
        self.forward_PushButton.setIcon(QtGui.QIcon(theme(self)["forward_png"]))
        self.reload_PushButton.setIcon(QtGui.QIcon(theme(self)["reload_png"]))
        self.home_PushButton.setIcon(QtGui.QIcon(theme(self)["home_png"]))
        self.settings_PushButton.setIcon(QtGui.QIcon(theme(self)["settings_png"]))
    except Exception as e:
        print ("Apply Theme Colors Error: "+e)