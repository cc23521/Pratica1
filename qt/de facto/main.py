import sys 
from PySide6.QtCore import QtMsgType 
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow, QStatusBar,  QTableWidgetItem

from FrmMoni_ui import Ui_FrmMoni
from FrmConexao_ui import Ui_dlgConexao 
from datetime import datetime 
import pyodbc as bd

global conexao, meuCursor

class FormPrincipal(QMainWindow, Ui_FrmMoni):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.show()        

class DialogoConexao(QDialog, Ui_dlgConexao):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)

if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    dlgCon = DialogoConexao()
    if dlgCon.exec() == QDialog.Accepted:
        try:
            conexao = bd.connect(driver="SQL Server",
                                server=f"{dlgCon.edServidor.text()}", 
                                database=f"{dlgCon.edBancoDeDados.text()}", 
                                uid=f"{dlgCon.edUserId.text()}", 
                                pwd=f"{dlgCon.edSenha.text()}") 
            print("Conexão bem sucedida!")
            meuCursor = conexao.cursor()
            janela = FormPrincipal() 
            aplicacao.exec() 
        except: 
            print("Não foi possível conectar ao banco de dados")
