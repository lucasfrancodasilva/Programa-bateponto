# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LCreates.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import smtplib

from time import sleep

class Ui_LCreates(object):
    def check_login(self):
        email = self.email.text()
        senha = self.senha.text()
        enviado = self.resumo.text()
        rec_email = "lucaslcreates@gmail.com"
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        while(True):
            if email == 'lucaslcreates@gmail.com' and senha == '040506ok':
                self.enviado.show()
                server.login(email, senha)
                server.sendmail(email, rec_email, enviado)
                email = ""
            elif email == 'laurinha.coelho16@gmail.com' and senha == 'arteeminhavida':
                print('enviado de laura')
                self.enviado.show()
                server.login(email, senha)
                server.sendmail(email, rec_email, enviado, data)
                break
            elif email == 'gustavo.de.carvalho.cypriano@gmail.com' and senha == 'bodeloiro123':
                self.enviado.show()
                server.login(email, senha)
                server.sendmail(email, rec_email, enviado, data)
                break
            elif email == 'gustavo.de.carvalho.cypriano@gmail.com' and senha == 'bodeloiro123':
                self.enviado.show()
                server.login(email, senha)
                server.sendmail(email, rec_email, enviado, data)
                break
            else:
                self.erro_2.show()
                break




    def setupUi(self, LCreates):
        LCreates.setObjectName("LCreates")
        LCreates.resize(500, 720)
        LCreates.setMinimumSize(QtCore.QSize(500, 720))
        LCreates.setMaximumSize(QtCore.QSize(500, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/lc png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LCreates.setWindowIcon(icon)
        LCreates.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(LCreates)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 700))
        self.centralwidget.setObjectName("centralwidget")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setGeometry(QtCore.QRect(0, 0, 501, 31))
        self.top_bar.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.erro_2 = QtWidgets.QFrame(self.top_bar)
        self.erro_2.setGeometry(QtCore.QRect(90, 0, 321, 31))
        self.erro_2.setMinimumSize(QtCore.QSize(50, 0))
        self.erro_2.setStyleSheet("background-color: rgb(255, 79, 82);\n"
"border-radius: 10px;")
        self.erro_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.erro_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.erro_2.setObjectName("erro_2")
        self.erro = QtWidgets.QLabel(self.erro_2)
        self.erro.setGeometry(QtCore.QRect(150, 0, 21, 31))
        self.erro.setStyleSheet("text-size: 10px;")
        self.erro.setObjectName("erro")
        self.closepopup1 = QtWidgets.QPushButton(self.erro_2)
        self.closepopup1.setGeometry(QtCore.QRect(290, 0, 21, 31))
        self.closepopup1.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(77, 77, 77);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.closepopup1.setObjectName("closepopup1")
        self.pagina_principal = QtWidgets.QFrame(self.centralwidget)
        self.pagina_principal.setGeometry(QtCore.QRect(0, 30, 500, 750))
        self.pagina_principal.setMinimumSize(QtCore.QSize(500, 750))
        self.pagina_principal.setMaximumSize(QtCore.QSize(500, 720))
        self.pagina_principal.setStyleSheet("background-color: rgb(52, 52, 52);")
        self.pagina_principal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pagina_principal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pagina_principal.setObjectName("pagina_principal")
        self.frame_2 = QtWidgets.QFrame(self.pagina_principal)
        self.frame_2.setGeometry(QtCore.QRect(200, 100, 100, 100))
        self.frame_2.setMinimumSize(QtCore.QSize(100, 100))
        self.frame_2.setMaximumSize(QtCore.QSize(100, 100))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-image: url(:/logo/imagens/lc png.png);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.email = QtWidgets.QLineEdit(self.pagina_principal)
        self.email.setGeometry(QtCore.QRect(140, 240, 231, 41))
        self.email.setStyleSheet("QLineEdit{\n"
"    border: 0px solid;\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgba(150, 150, 150, 150);\n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLineEdit\" name=\"lineEdit\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>140</x>\n"
"     <y>240</y>\n"
"     <width>231</width>\n"
"     <height>41</height>\n"
"    </rect>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.email.setObjectName("email")
        self.senha = QtWidgets.QLineEdit(self.pagina_principal)
        self.senha.setGeometry(QtCore.QRect(140, 290, 231, 41))
        self.senha.setStyleSheet("QLineEdit{\n"
"    border: 0px solid;\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgba(150, 150, 150, 150);\n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLineEdit\" name=\"lineEdit\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>140</x>\n"
"     <y>240</y>\n"
"     <width>231</width>\n"
"     <height>41</height>\n"
"    </rect>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha.setObjectName("senha")
        self.resumo = QtWidgets.QLineEdit(self.pagina_principal)
        self.resumo.setGeometry(QtCore.QRect(140, 350, 231, 81))
        self.resumo.setStyleSheet("QLineEdit{\n"
"    border: 0px solid;\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgba(150, 150, 150, 150);\n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLineEdit\" name=\"lineEdit\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>140</x>\n"
"     <y>240</y>\n"
"     <width>231</width>\n"
"     <height>41</height>\n"
"    </rect>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.resumo.setText("")
        self.resumo.setMaxLength(5000)
        self.resumo.setCursorPosition(0)
        self.resumo.setObjectName("resumo")
        self.enviar = QtWidgets.QPushButton(self.pagina_principal)
        self.enviar.setGeometry(QtCore.QRect(140, 500, 231, 51))
        self.enviar.setStyleSheet("QPushButton{\n"
"    color: rgb(144, 144, 144);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(62, 62, 62);\n"
"}")
        self.enviar.setObjectName("enviar")
        self.enviado = QtWidgets.QFrame(self.pagina_principal)
        self.enviado.setGeometry(QtCore.QRect(90, 50, 321, 31))
        self.enviado.setMinimumSize(QtCore.QSize(50, 0))
        self.enviado.setStyleSheet("background-color: rgb(0, 198, 13);\n"
"border-radius: 10px;")
        self.enviado.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.enviado.setFrameShadow(QtWidgets.QFrame.Raised)
        self.enviado.setObjectName("enviado")
        self.enviado_2 = QtWidgets.QLabel(self.enviado)
        self.enviado_2.setGeometry(QtCore.QRect(140, 0, 51, 31))
        self.enviado_2.setStyleSheet("text-size: 10px;")
        self.enviado_2.setObjectName("enviado_2")
        self.closepopup = QtWidgets.QPushButton(self.enviado)
        self.closepopup.setGeometry(QtCore.QRect(290, 0, 21, 31))
        self.closepopup.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgb(77, 77, 77);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.closepopup.setObjectName("closepopup")
        self.data = QtWidgets.QLineEdit(self.pagina_principal)
        self.data.setGeometry(QtCore.QRect(140, 440, 111, 41))
        self.data.setStyleSheet("QLineEdit{\n"
"    border: 0px solid;\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgba(150, 150, 150, 150);\n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QLineEdit\" name=\"lineEdit\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>140</x>\n"
"     <y>240</y>\n"
"     <width>231</width>\n"
"     <height>41</height>\n"
"    </rect>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.data.setObjectName("data")
        LCreates.setCentralWidget(self.centralwidget)



        #
        #   Functions
        #
        self.closepopup1.clicked.connect(lambda: self.erro_2.hide())
        self.closepopup.clicked.connect(lambda: self.enviado.hide())

        # hide popup
        self.erro_2.hide()
        self.enviado.hide()

        # login

        self.enviar.clicked.connect(self.check_login)

        self.retranslateUi(LCreates)
        QtCore.QMetaObject.connectSlotsByName(LCreates)

    def retranslateUi(self, LCreates):
        _translate = QtCore.QCoreApplication.translate
        LCreates.setWindowTitle(_translate("LCreates", "LCreates"))
        self.erro.setText(_translate("LCreates", "Erro"))
        self.closepopup1.setText(_translate("LCreates", "X"))
        self.email.setPlaceholderText(_translate("LCreates", "E-MAIL"))
        self.senha.setPlaceholderText(_translate("LCreates", "SENHA"))
        self.resumo.setPlaceholderText(_translate("LCreates", "Trabalho de hoje"))
        self.enviar.setText(_translate("LCreates", "ENVIAR"))
        self.enviado_2.setText(_translate("LCreates", "ENVIADO"))
        self.closepopup.setText(_translate("LCreates", "X"))
        self.data.setPlaceholderText(_translate("LCreates", "DATA"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LCreates = QtWidgets.QMainWindow()
    ui = Ui_LCreates()
    ui.setupUi(LCreates)
    LCreates.show()
    sys.exit(app.exec_())