# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog/edit_employee_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditEmployee(object):
    def setupUi(self, EditEmployee):
        EditEmployee.setObjectName("EditEmployee")
        EditEmployee.resize(641, 435)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditEmployee)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list_seller = QtWidgets.QListWidget(EditEmployee)
        self.list_seller.setObjectName("list_seller")
        self.verticalLayout.addWidget(self.list_seller)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditEmployee)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditEmployee)
        self.buttonBox.accepted.connect(EditEmployee.accept) # type: ignore
        self.buttonBox.rejected.connect(EditEmployee.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(EditEmployee)

    def retranslateUi(self, EditEmployee):
        _translate = QtCore.QCoreApplication.translate
        EditEmployee.setWindowTitle(_translate("EditEmployee", "Редактирование сотрудника"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditEmployee = QtWidgets.QDialog()
    ui = Ui_EditEmployee()
    ui.setupUi(EditEmployee)
    EditEmployee.show()
    sys.exit(app.exec_())
