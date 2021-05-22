from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser =  QWebEngineView()
        back = QAction("👈 back please",self)

        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        #nav bar
        navBar = QToolBar()
        self.addToolBar(navBar)

        back.triggered.connect(self.browser.back)
        navBar.addAction(back)

        forward = QAction("forward 👉",self)
        forward.triggered.connect(self.browser.forward)
        navBar.addAction(forward)

        Reload = QAction("reload ", self)
        Reload.triggered.connect(self.browser.reload)
        navBar.addAction(Reload)

        home = QAction("home sweet home 🏠🏠 ", self)
        home.triggered.connect(self.navigate_home)
        navBar.addAction(home)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navBar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def update_url(self,q):
        self.url_bar.setText(q.toString())

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))


    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))



app = QApplication(sys.argv)
QApplication.setApplicationName("MY chrome killer")
window = MainWindow()
app.exec_()