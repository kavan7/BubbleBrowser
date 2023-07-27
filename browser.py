import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.browser.urlChanged.connect(self.update_urlbar)
   
        self.setCentralWidget(self.browser)


        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        self.httpsicon = QLabel()
        navtb.addWidget(self.httpsicon)

        self.show()

      
        self.setWindowTitle("Bubble Browser")



    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.browser.setUrl(q)

    def update_urlbar(self, q):
        if q.scheme() == 'https':
            self.httpsicon.setPixmap(QPixmap("images/lock-ssl.png"))
        else:
            self.httpsicon.setPixmap(QPixmap("images/lock-nossl.png"))
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Bubble Browser")

   
    app.setStyle("Fusion")

    window = MainWindow()
    window.resize(1024, 768) 
    sys.exit(app.exec_())
