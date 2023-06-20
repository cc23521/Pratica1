from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_student = QtWidgets.QWidget()
        self.tab_student.setObjectName("tab_student")
        self.tab_apontamento = QtWidgets.QWidget()
        self.tab_apontamento.setObjectName("tab_apontamento")
        self.pushButton_insert_student = QtWidgets.QPushButton(self.tab_student)
        self.pushButton_insert_student.setGeometry(QtCore.QRect(50, 100, 150, 30))
        self.pushButton_insert_student.setObjectName("pushButton_insert_student")
        self.pushButton_delete_student = QtWidgets.QPushButton(self.tab_student)
        self.pushButton_delete_student.setGeometry(QtCore.QRect(200, 100, 150, 30))
        self.pushButton_delete_student.setObjectName("pushButton_delete_student")
        self.tabWidget.addTab(self.tab_student, "")
        self.tab_property = QtWidgets.QWidget()
        self.tab_property.setObjectName("tab_property")
        self.pushButton_insert_property = QtWidgets.QPushButton(self.tab_property)
        self.pushButton_insert_property.setGeometry(QtCore.QRect(50, 100, 150, 30))
        self.pushButton_insert_property.setObjectName("pushButton_insert_property")
        self.pushButton_delete_property = QtWidgets.QPushButton(self.tab_property)
        self.pushButton_delete_property.setGeometry(QtCore.QRect(200, 100, 150, 30))
        self.pushButton_delete_property.setObjectName("pushButton_delete_property")
        self.tabWidget.addTab(self.tab_property, "")
        self.pushButton_insert_apontamento = QtWidgets.QPushButton(self.tab_apontamento)
        self.pushButton_insert_apontamento.setGeometry(QtCore.QRect(50, 100, 150, 30))
        self.pushButton_insert_apontamento.setObjectName("pushButton_insert_apontamento")
        self.pushButton_delete_apontamento = QtWidgets.QPushButton(self.tab_apontamento)
        self.pushButton_delete_apontamento.setGeometry(QtCore.QRect(200, 100, 150, 30))
        self.pushButton_delete_apontamento.setObjectName("pushButton_delete_apontamento")
        self.tabWidget.addTab(self.tab_apontamento, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Window"))
        self.pushButton_insert_student.setText(_translate("MainWindow", "Insert Student"))
        self.pushButton_delete_student.setText(_translate("MainWindow", "Delete Student"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_student), _translate("MainWindow", "Estudante"))
        self.pushButton_insert_property.setText(_translate("MainWindow", "Insert Property"))
        self.pushButton_delete_property.setText(_translate("MainWindow", "Delete Property"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_property), _translate("MainWindow", "Imóvel"))
        self.pushButton_insert_apontamento.setText(_translate("MainWindow", "Insert Apontamento"))
        self.pushButton_delete_apontamento.setText(_translate("MainWindow", "Delete Apontamento"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_apontamento), _translate("Main Window", "Apontamento"))


class Ui_InsertStudentWindow(object):
    def setupUi(self, InsertStudentWindow):
        InsertStudentWindow.setObjectName("InsertStudentWindow")
        InsertStudentWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(InsertStudentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 240, 100, 30))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(250, 240, 100, 30))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(50, 30, 100, 30))
        self.label_name.setObjectName("label_name")
        self.label_ra = QtWidgets.QLabel(self.centralwidget)
        self.label_ra.setGeometry(QtCore.QRect(50, 70, 100, 30))
        self.label_ra.setObjectName("label_ra")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(50, 110, 100, 30))
        self.label_email.setObjectName("label_email")
        self.label_property_id = QtWidgets.QLabel(self.centralwidget)
        self.label_property_id.setGeometry(QtCore.QRect(50, 150, 100, 30))
        self.label_property_id.setObjectName("label_property_id")
        self.label_absent_days = QtWidgets.QLabel(self.centralwidget)
        self.label_absent_days.setGeometry(QtCore.QRect(50, 190, 100, 30))
        self.label_absent_days.setObjectName("label_absent_days")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(150, 30, 200, 30))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_ra = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ra.setGeometry(QtCore.QRect(150, 70, 200, 30))
        self.lineEdit_ra.setObjectName("lineEdit_ra")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(150, 110, 200, 30))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_property_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_property_id.setGeometry(QtCore.QRect(150, 150, 200, 30))
        self.lineEdit_property_id.setObjectName("lineEdit_property_id")
        self.lineEdit_absent_days = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_absent_days.setGeometry(QtCore.QRect(150, 190, 200, 30))
        self.lineEdit_absent_days.setObjectName("lineEdit_absent_days")
        InsertStudentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InsertStudentWindow)
        QtCore.QMetaObject.connectSlotsByName(InsertStudentWindow)

    def retranslateUi(self, InsertStudentWindow):
        _translate = QtCore.QCoreApplication.translate
        InsertStudentWindow.setWindowTitle(_translate("InsertStudentWindow", "Insert Student"))
        self.pushButton_back.setText(_translate("InsertStudentWindow", "Back"))
        self.pushButton_cancel.setText(_translate("InsertStudentWindow", "Cancel"))
        self.label_name.setText(_translate("InsertStudentWindow", "Name:"))
        self.label_ra.setText(_translate("InsertStudentWindow", "RA:"))
        self.label_email.setText(_translate("InsertStudentWindow", "Email:"))
        self.label_property_id.setText(_translate("InsertStudentWindow", "Property ID:"))
        self.label_absent_days.setText(_translate("InsertStudentWindow", "Absent Days:"))

class Ui_InsertPropertyWindow(object):
    def setupUi(self, InsertPropertyWindow):
        InsertPropertyWindow.setObjectName("InsertPropertyWindow")
        InsertPropertyWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(InsertPropertyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(50, 240, 100, 30))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(250, 240, 100, 30))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label_Idimovel = QtWidgets.QLabel(self.centralwidget)
        self.label_Idimovel.setGeometry(QtCore.QRect(50, 30, 100, 30))
        self.label_Idimovel.setObjectName("label_Idimovel")
        self.lineEdit_Idimovel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Idimovel.setGeometry(QtCore.QRect(150, 30, 200, 30))
        self.lineEdit_Idimovel.setObjectName("lineEdit_Idimovel")
        self.label_bloco = QtWidgets.QLabel(self.centralwidget)
        self.label_bloco.setGeometry(QtCore.QRect(50, 100, 100, 30))
        self.label_bloco.setObjectName("label_bloco")
        self.lineEdit_bloco = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_bloco.setGeometry(QtCore.QRect(150, 100, 200, 30))
        self.lineEdit_bloco.setObjectName("lineEdit_bloco")
        InsertPropertyWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InsertPropertyWindow)
        QtCore.QMetaObject.connectSlotsByName(InsertPropertyWindow)

    def retranslateUi(self, InsertPropertyWindow):
        _translate = QtCore.QCoreApplication.translate
        InsertPropertyWindow.setWindowTitle(_translate("InsertPropertyWindow", "Insert Property"))
        self.pushButton_back.setText(_translate("InsertPropertyWindow", "Back"))
        self.pushButton_cancel.setText(_translate("InsertPropertyWindow", "Cancel"))
        self.label_Idimovel.setText(_translate("InsertPropertyWindow", "Id_imovel:"))
        self.label_bloco.setText(_translate("InsertPropertyWindow", "Bloco:"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.pushButton_insert_student.clicked.connect(self.open_insert_student_window)
        self.pushButton_delete_student.clicked.connect(self.delete_student)
        self.pushButton_insert_property.clicked.connect(self.open_insert_property_window)
        self.pushButton_delete_property.clicked.connect(self.delete_property)

    def open_insert_student_window(self):
        self.insert_student_window = QtWidgets.QMainWindow()
        self.ui = Ui_InsertStudentWindow()
        self.ui.setupUi(self.insert_student_window)
        self.insert_student_window.show()
        self.ui.pushButton_back.clicked.connect(self.close_insert_student_window)
        self.ui.pushButton_cancel.clicked.connect(self.clear_insert_student_fields)

    def close_insert_student_window(self):
        self.insert_student_window.close()

    def clear_insert_student_fields(self):
        self.ui.lineEdit_name.clear()
        self.ui.lineEdit_ra.clear()
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_property_id.clear()
        self.ui.lineEdit_absent_days.clear()

    def delete_student(self):
        ra, ok = QtWidgets.QInputDialog.getText(self, "Delete Student", "Enter RA:")
        if ok and ra:
            print("Student deleted:", ra)

    def open_insert_property_window(self):
        self.insert_property_window = QtWidgets.QMainWindow()
        self.ui = Ui_InsertPropertyWindow()
        self.ui.setupUi(self.insert_property_window)
        self.insert_property_window.show()
        self.ui.pushButton_back.clicked.connect(self.close_insert_property_window)
        self.ui.pushButton_cancel.clicked.connect(self.clear_insert_property_fields)

    def close_insert_property_window(self):
        self.insert_property_window.close()

    def delete_property(self):
        id_imovel, ok = QtWidgets.QInputDialog.getText(self, "Delete Property", "Enter Id_imovel:")
        if ok and id_imovel:
            print("Property deleted:", id_imovel)

    def clear_insert_property_fields(self):
        self.ui.lineEdit_Idimovel.clear()
        self.ui.lineEdit_bloco.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

