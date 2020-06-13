from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 404)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(36)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 60, 351, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light Condensed")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnstart = QtWidgets.QPushButton(self.centralwidget)
        self.btnstart.setGeometry(QtCore.QRect(210, 240, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.btnstart.setFont(font)
        self.btnstart.setObjectName("btnstart")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "글씨 인식 시스템"))
        self.btnstart.setText(_translate("MainWindow", "시작"))
        self.btnstart.clicked.connect(self.main)

    def main(self):
        import subprocess
        from glob import glob
        filelist = glob("main.py")

        for file in filelist:
            subprocess.call(['python', file])

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
