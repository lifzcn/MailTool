# -*- coding : utf-8 -*-
# @File   : main.py
# @Time   : 2022/3/13
# @Author : Leonard
# @Email  : li.fz@foxmail.com

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from PyQt5.QtWidgets import QApplication, QWidget
from interface import Ui_Form


class mainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.lineEdit_1.setText("smtp-mail.outlook.com")
        self.lineEdit_2.setText("leoleechn@outlook.com")
        self.lineEdit_3.setText("LeoLee091801")
        self.pushButton_2.clicked.connect(self.sendMail)

    def sendMail(self, parent=None):
        mailServer = "smtp-mail.outlook.com"
        mailPort = 587
        senderAccount = "leoleechn@outlook.com"
        senderPassword = "LeoLee091801"
        receiverAccount = self.lineEdit_4.text()
        topicText = self.lineEdit_5.text()
        mainText = self.plainTextEdit.toPlainText()

        # senderName = "Leonard"
        # receiverName = "Gloria"

        msg = MIMEText(mainText, "plain", "utf-8")
        msg["Subject:"] = topicText
        msg["From:"] = senderAccount
        msg["To:"] = receiverAccount

        try:
            smtpObj = smtplib.SMTP(mailServer, mailPort)
            smtpObj.starttls()
            smtpObj.login(senderAccount, senderPassword)
            smtpObj.sendmail(senderAccount, receiverAccount, msg.as_string())
            self.lineEdit_7.setText("Successful")
        except smtplib.SMTPException:
            self.lineEdit_7.setText("Failed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec_())
