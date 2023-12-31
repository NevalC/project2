# Form implementation generated from reading ui file 'fridge_opened.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from Fridge import *

class Ui_popup(object):
    def setupUi(self, Dialog, fridge: type[Fridge]) -> None:
        '''
        Function creates the window.
        :param Dialog: Creates the window.
        :param fridge: Calls back to Fridge.
        '''
        self.fridge = fridge
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 165)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(165)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(351, 165))
        Dialog.setMaximumSize(QtCore.QSize(351, 165))
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 113, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(113, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.item = self.lineEdit.text()

        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.take_clicked)

        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.deposit_clicked)

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(250, 60, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        for i in range(9):
            self.comboBox.addItem(str(i))

        self.comboBox_2 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(250, 90, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        for i in range(9):
            self.comboBox_2.addItem(str(i))

        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 120, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.fridge.check)

        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 20, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 20, 91, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog) -> None:
        '''
        Function creates text for gui.
        :param Dialog: Dialog is the window.
        '''
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Take"))
        self.pushButton_2.setText(_translate("Dialog", "Deposit"))
        self.comboBox.setItemText(0, _translate("Dialog", "0"))
        self.comboBox.setItemText(1, _translate("Dialog", "1"))
        self.comboBox.setItemText(2, _translate("Dialog", "2"))
        self.comboBox.setItemText(3, _translate("Dialog", "3"))
        self.comboBox.setItemText(4, _translate("Dialog", "4"))
        self.comboBox.setItemText(5, _translate("Dialog", "5"))
        self.comboBox.setItemText(6, _translate("Dialog", "6"))
        self.comboBox.setItemText(7, _translate("Dialog", "7"))
        self.comboBox.setItemText(8, _translate("Dialog", "8"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "0"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "1"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "2"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "3"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "4"))
        self.comboBox_2.setItemText(5, _translate("Dialog", "5"))
        self.comboBox_2.setItemText(6, _translate("Dialog", "6"))
        self.comboBox_2.setItemText(7, _translate("Dialog", "7"))
        self.comboBox_2.setItemText(8, _translate("Dialog", "8"))
        self.pushButton_3.setText(_translate("Dialog", "Check"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Option</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Food</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Number</span></p></body></html>"))

    def take_clicked(self) -> None:
        '''
        Function sends all information from take to Fridge.py.
        '''
        self.take_lineEdit = self.lineEdit.text()
        self.take_value_comboBox_index = self.comboBox.currentIndex()
        self.take_value_comboBox_text = self.comboBox.itemText(self.take_value_comboBox_index)
        self.take_comboBox = self.take_value_comboBox_text
        self.fridge.take(self.take_lineEdit, self.take_comboBox)

    def deposit_clicked(self) -> None:
        '''
        Function sends all information from deposit to Fridge.py.
        '''
        self.deposit_lineEdit_2 = self.lineEdit_2.text()
        self.deposit_value_comboBox_2_index = self.comboBox_2.currentIndex()
        self.deposit_value_comboBox_2_text = self.comboBox_2.itemText(self.deposit_value_comboBox_2_index)
        self.deposit_comboBox_2 = self.deposit_value_comboBox_2_text
        self.fridge.deposit(self.deposit_lineEdit_2, self.deposit_comboBox_2)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fridge_instance = Fridge()
    Dialog = QtWidgets.QDialog()
    ui = Ui_popup()
    ui.setupUi(Dialog, fridge_instance)
    Dialog.show()
    sys.exit(app.exec())
