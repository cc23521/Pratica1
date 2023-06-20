# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FrmConexao.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_dlgConexao(object):
    def setupUi(self, dlgConexao):
        if not dlgConexao.objectName():
            dlgConexao.setObjectName(u"dlgConexao")
        dlgConexao.resize(497, 235)
        font = QFont()
        font.setPointSize(11)
        dlgConexao.setFont(font)
        self.gridLayout = QGridLayout(dlgConexao)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(dlgConexao)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.edServidor = QLineEdit(dlgConexao)
        self.edServidor.setObjectName(u"edServidor")

        self.gridLayout.addWidget(self.edServidor, 0, 1, 1, 2)

        self.label_2 = QLabel(dlgConexao)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.edBancoDeDados = QLineEdit(dlgConexao)
        self.edBancoDeDados.setObjectName(u"edBancoDeDados")

        self.gridLayout.addWidget(self.edBancoDeDados, 1, 2, 1, 1)

        self.label_3 = QLabel(dlgConexao)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.edUserId = QLineEdit(dlgConexao)
        self.edUserId.setObjectName(u"edUserId")
        font2 = QFont()
        font2.setPointSize(12)
        self.edUserId.setFont(font2)

        self.gridLayout.addWidget(self.edUserId, 2, 2, 1, 1)

        self.label_4 = QLabel(dlgConexao)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.edSenha = QLineEdit(dlgConexao)
        self.edSenha.setObjectName(u"edSenha")
        self.edSenha.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.edSenha, 3, 2, 1, 1)

        self.buttonBox = QDialogButtonBox(dlgConexao)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 3)


        self.retranslateUi(dlgConexao)
        self.buttonBox.accepted.connect(dlgConexao.accept)
        self.buttonBox.rejected.connect(dlgConexao.reject)

        QMetaObject.connectSlotsByName(dlgConexao)
    # setupUi

    def retranslateUi(self, dlgConexao):
        dlgConexao.setWindowTitle(QCoreApplication.translate("dlgConexao", u"Conex\u00e3o ao banco de Dados", None))
        self.label.setText(QCoreApplication.translate("dlgConexao", u"Endere\u00e7o do Servidor:", None))
        self.edServidor.setText(QCoreApplication.translate("dlgConexao", u"regulus.cotuca.unicamp.br", None))
        self.label_2.setText(QCoreApplication.translate("dlgConexao", u"Nome do banco de dados:", None))
        self.edBancoDeDados.setText("")
        self.label_3.setText(QCoreApplication.translate("dlgConexao", u"Nome de usu\u00e1rio:", None))
        self.edUserId.setText("")
        self.edUserId.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("dlgConexao", u"Senha:", None))
        self.edSenha.setText("")
        self.edSenha.setPlaceholderText(QCoreApplication.translate("dlgConexao", u"Digite sua senha:", None))
    # retranslateUi

