# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmMoni.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_FrmMoni(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 491, 281))
        self.tab_estudante = QWidget()
        self.tab_estudante.setObjectName(u"tab_estudante")
        self.ra = QLineEdit(self.tab_estudante)
        self.ra.setObjectName(u"ra")
        self.ra.setGeometry(QRect(50, 60, 113, 20))
        self.label = QLabel(self.tab_estudante)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 47, 13))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.email = QLineEdit(self.tab_estudante)
        self.email.setObjectName(u"email")
        self.email.setGeometry(QRect(60, 100, 113, 20))
        self.label_2 = QLabel(self.tab_estudante)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 47, 13))
        self.label_2.setFont(font)
        self.nome_social = QLineEdit(self.tab_estudante)
        self.nome_social.setObjectName(u"nome_social")
        self.nome_social.setGeometry(QRect(100, 140, 113, 20))
        self.label_3 = QLabel(self.tab_estudante)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 140, 81, 16))
        self.label_3.setFont(font)
        self.id_imovel_fk = QLineEdit(self.tab_estudante)
        self.id_imovel_fk.setObjectName(u"id_imovel_fk")
        self.id_imovel_fk.setGeometry(QRect(80, 180, 113, 20))
        self.label_4 = QLabel(self.tab_estudante)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 180, 71, 16))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.tab_estudante)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 20, 81, 16))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.tab_estudante)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 20, 81, 16))
        self.label_6.setFont(font1)
        self.ra_del = QLineEdit(self.tab_estudante)
        self.ra_del.setObjectName(u"ra_del")
        self.ra_del.setGeometry(QRect(280, 60, 113, 20))
        self.label_7 = QLabel(self.tab_estudante)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 60, 47, 13))
        self.label_7.setFont(font)
        self.cadastrar_estudante = QPushButton(self.tab_estudante)
        self.cadastrar_estudante.setObjectName(u"cadastrar_estudante")
        self.cadastrar_estudante.setGeometry(QRect(20, 210, 75, 23))
        self.cadastrar_estudante.setFont(font)
        self.deletar_estudante = QPushButton(self.tab_estudante)
        self.deletar_estudante.setObjectName(u"deletar_estudante")
        self.deletar_estudante.setGeometry(QRect(260, 90, 75, 23))
        self.deletar_estudante.setFont(font)
        self.cancelar_estudante = QPushButton(self.tab_estudante)
        self.cancelar_estudante.setObjectName(u"cancelar_estudante")
        self.cancelar_estudante.setGeometry(QRect(400, 220, 75, 23))
        self.cancelar_estudante.setFont(font)
        self.tabWidget.addTab(self.tab_estudante, "")
        self.tab_imovel = QWidget()
        self.tab_imovel.setObjectName(u"tab_imovel")
        self.label_8 = QLabel(self.tab_imovel)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 20, 81, 16))
        self.label_8.setFont(font1)
        self.label_9 = QLabel(self.tab_imovel)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, 20, 81, 16))
        self.label_9.setFont(font1)
        self.cancelar_imovel = QPushButton(self.tab_imovel)
        self.cancelar_imovel.setObjectName(u"cancelar_imovel")
        self.cancelar_imovel.setGeometry(QRect(400, 220, 75, 23))
        self.cancelar_imovel.setFont(font)
        self.cadastrar_imovel = QPushButton(self.tab_imovel)
        self.cadastrar_imovel.setObjectName(u"cadastrar_imovel")
        self.cadastrar_imovel.setGeometry(QRect(20, 130, 75, 23))
        self.cadastrar_imovel.setFont(font)
        self.label_10 = QLabel(self.tab_imovel)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 100, 47, 13))
        self.label_10.setFont(font)
        self.id_imovel = QLineEdit(self.tab_imovel)
        self.id_imovel.setObjectName(u"id_imovel")
        self.id_imovel.setGeometry(QRect(80, 60, 113, 20))
        self.bloco = QLineEdit(self.tab_imovel)
        self.bloco.setObjectName(u"bloco")
        self.bloco.setGeometry(QRect(60, 100, 113, 20))
        self.label_11 = QLabel(self.tab_imovel)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 60, 61, 16))
        self.label_11.setFont(font)
        self.deletar_imovel = QPushButton(self.tab_imovel)
        self.deletar_imovel.setObjectName(u"deletar_imovel")
        self.deletar_imovel.setGeometry(QRect(260, 90, 75, 23))
        self.deletar_imovel.setFont(font)
        self.label_12 = QLabel(self.tab_imovel)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(260, 60, 61, 16))
        self.label_12.setFont(font)
        self.id_imovel_del = QLineEdit(self.tab_imovel)
        self.id_imovel_del.setObjectName(u"id_imovel_del")
        self.id_imovel_del.setGeometry(QRect(320, 60, 113, 20))
        self.tabWidget.addTab(self.tab_imovel, "")
        self.tab_apontamento = QWidget()
        self.tab_apontamento.setObjectName(u"tab_apontamento")
        self.label_13 = QLabel(self.tab_apontamento)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 20, 81, 16))
        self.label_13.setFont(font1)
        self.label_14 = QLabel(self.tab_apontamento)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(260, 20, 81, 16))
        self.label_14.setFont(font1)
        self.label_15 = QLabel(self.tab_apontamento)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 60, 101, 16))
        self.label_15.setFont(font)
        self.id_apontamento = QLineEdit(self.tab_apontamento)
        self.id_apontamento.setObjectName(u"id_apontamento")
        self.id_apontamento.setGeometry(QRect(120, 60, 113, 20))
        self.ra_fk = QLineEdit(self.tab_apontamento)
        self.ra_fk.setObjectName(u"ra_fk")
        self.ra_fk.setGeometry(QRect(50, 100, 113, 20))
        self.label_16 = QLabel(self.tab_apontamento)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 100, 47, 13))
        self.label_16.setFont(font)
        self.label_17 = QLabel(self.tab_apontamento)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 140, 47, 13))
        self.label_17.setFont(font)
        self.entrada = QLineEdit(self.tab_apontamento)
        self.entrada.setObjectName(u"entrada")
        self.entrada.setGeometry(QRect(70, 140, 113, 20))
        self.cadastrar_apont = QPushButton(self.tab_apontamento)
        self.cadastrar_apont.setObjectName(u"cadastrar_apont")
        self.cadastrar_apont.setGeometry(QRect(20, 170, 75, 23))
        self.cadastrar_apont.setFont(font)
        self.id_apontamento_del = QLineEdit(self.tab_apontamento)
        self.id_apontamento_del.setObjectName(u"id_apontamento_del")
        self.id_apontamento_del.setGeometry(QRect(360, 60, 113, 20))
        self.label_18 = QLabel(self.tab_apontamento)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(260, 60, 101, 16))
        self.label_18.setFont(font)
        self.deletar_apont = QPushButton(self.tab_apontamento)
        self.deletar_apont.setObjectName(u"deletar_apont")
        self.deletar_apont.setGeometry(QRect(260, 90, 75, 23))
        self.deletar_apont.setFont(font)
        self.cancelar_apont = QPushButton(self.tab_apontamento)
        self.cancelar_apont.setObjectName(u"cancelar_apont")
        self.cancelar_apont.setGeometry(QRect(400, 220, 75, 23))
        self.cancelar_apont.setFont(font)
        self.tabWidget.addTab(self.tab_apontamento, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RA:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nome social:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Id Im\u00f3vel:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Dele\u00e7\u00e3o", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"RA:", None))
        self.cadastrar_estudante.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.deletar_estudante.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.cancelar_estudante.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_estudante), QCoreApplication.translate("MainWindow", u"Estudante", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Dele\u00e7\u00e3o", None))
        self.cancelar_imovel.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.cadastrar_imovel.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Bloco:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Id Im\u00f3vel:", None))
        self.deletar_imovel.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Id Im\u00f3vel:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_imovel), QCoreApplication.translate("MainWindow", u"Im\u00f3vel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Dele\u00e7\u00e3o", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Id Apontamento:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"RA:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Entrada:", None))
        self.cadastrar_apont.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Id Apontamento:", None))
        self.deletar_apont.setText(QCoreApplication.translate("MainWindow", u"Deletar", None))
        self.cancelar_apont.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_apontamento), QCoreApplication.translate("MainWindow", u"Apontamento", None))
    # retranslateUi
