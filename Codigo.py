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
        
        
        self.closepopup1.clicked.connect(lambda: self.erro_2.hide())
        self.closepopup.clicked.connect(lambda: self.enviado.hide())

        # hide popup
        self.erro_2.hide()
        self.enviado.hide()

        # login

        self.enviar.clicked.connect(self.check_login)
