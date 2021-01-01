# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle

def darkMode():
        if ui.checkBox.isChecked():
            dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
            app.setStyleSheet(dark_stylesheet)
            ui.checkBox.setText("Light Mode")
        else:
            app.setStyleSheet("")
            ui.checkBox.setText("Dark Mode")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(756, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(100)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.developerLabel = QtWidgets.QLabel()
        self.developerLabel.setText("Designed & Developed by")
        self.gridLayout.addWidget(self.developerLabel, 0, 0, 1, 1, QtCore.Qt.AlignCenter)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.stateChanged.connect(darkMode)
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee Data Record"))
        self.pushButton_2.setText(_translate("MainWindow", "Search 🔍"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Employee ID"))
        self.pushButton.setText(_translate("MainWindow", "View Analytics"))
        self.pushButton_4.setText(_translate("MainWindow", "Edit Employee Record"))
        self.pushButton_3.setText(_translate("MainWindow", "Delete Record"))
        self.checkBox.setText(_translate("MainWindow", "Dark Mode"))

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    

    MainWindow.show()
    sys.exit(app.exec_())
