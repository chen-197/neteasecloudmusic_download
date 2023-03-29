# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

import sys

class Ui_NeteaseCloudMusic_Download(object):
    def setupUi(self, NeteaseCloudMusic_Download):
        if not NeteaseCloudMusic_Download.objectName():
            NeteaseCloudMusic_Download.setObjectName(u"NeteaseCloudMusic_Download")
        NeteaseCloudMusic_Download.resize(850, 674)
        self.centralwidget = QWidget(NeteaseCloudMusic_Download)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 31, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 51, 17))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 170, 67, 17))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 50, 281, 31))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(80, 110, 281, 31))
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(80, 170, 281, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(410, 60, 171, 51))
        self.pushButton.clicked.connect(slotone)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(410, 120, 171, 31))
        self.pushButton_2.clicked.connect(slotfour)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(410, 160, 171, 31))
        self.pushButton_3.clicked.connect(slotfive)
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(10, 230, 831, 381))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(670, 90, 112, 23))
        self.radioButton.clicked.connect(slottwo)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(670, 140, 112, 23))
        self.radioButton_2.clicked.connect(slotthree)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 10, 521, 31))
        self.label_4.setAlignment(Qt.AlignCenter)
        NeteaseCloudMusic_Download.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(NeteaseCloudMusic_Download)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 27))
        NeteaseCloudMusic_Download.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(NeteaseCloudMusic_Download)
        self.statusbar.setObjectName(u"statusbar")
        NeteaseCloudMusic_Download.setStatusBar(self.statusbar)

        self.retranslateUi(NeteaseCloudMusic_Download)

        QMetaObject.connectSlotsByName(NeteaseCloudMusic_Download)
    # setupUi

    def retranslateUi(self, NeteaseCloudMusic_Download):
        NeteaseCloudMusic_Download.setWindowTitle(QCoreApplication.translate("NeteaseCloudMusic_Download", u"NeteaseCloudMusic_Download", None))
        self.label.setText(QCoreApplication.translate("NeteaseCloudMusic_Download", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("NeteaseCloudMusic_Download", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("NeteaseCloudMusic_Download", u"Number:", None))
        self.pushButton.setText(QCoreApplication.translate("NeteaseCloudMusic_Download", u"\u5f00\u59cb\u4e0b\u8f7d", None))
        self.pushButton_2.setText(QCoreApplication.translate("NeteaseCloudMusic_Download", u"\u6e05\u7a7a\u4e0b\u8f7d\u5185\u5bb9", None))
        self.pushButton_3.setText(QCoreApplication.translate("NeteaseCloudMusic_Download", u"\u6e05\u7a7a\u6267\u884c\u5185\u5bb9", None))
        self.radioButton.setText(QCoreApplication.translate("NeteaseCloudMusic_Download", u"\u6279\u91cf\u4e0b\u8f7d", None))
        self.radioButton_2.setText(QCoreApplication.translate("NeteaseCloudMusic_Download", u"\u5355\u66f2\u4e0b\u8f7d", None))
        self.label_4.setText(QCoreApplication.translate("NeteaseCloudMusic_Download", u"Qt & Python", None))
    # retranslateUi

@Slot()
def slotone():
    global xuanze
    ui.pushButton.setEnabled(False)
    ui.pushButton_2.setEnabled(False)
    ui.pushButton_3.setEnabled(False)
    ui.textEdit_4.setEnabled(False)
    ui.pushButton.setText("已完成0%")
    strone = ui.textEdit.toPlainText()
    strtwo = ui.textEdit_2.toPlainText()
    strthree = ui.textEdit_3.toPlainText()
    import requests
    from bs4 import BeautifulSoup
    header={
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'Referer': 'https://music.163.com/',
    }


    if xuanze == "1" :
       #print("看到歌单所在网址的链接了吗，它的格式类似于“https://music.163.com/#/LIST?id=ID”")
       LIST=strtwo
       ID=strone
       choicelimit=int(strthree)
       link = "http://music.163.com/" + LIST + "?id=" + ID
       r = requests.get(link, headers=header)
       html = r.content
       soup = BeautifulSoup(html, "html.parser")
       songs = soup.find("ul", class_="f-hide").select("a", limit=choicelimit)

       i = 1

       for s in songs:
           song_id = s['href'][9:]
           song_name = s.text
           song_down_link = "http://music.163.com/song/media/outer/url?id=" + song_id + ".mp3"
           ui.textEdit_4.insertPlainText("第 " + str(i) + " 首歌曲：" + song_down_link + "\n")
           print("第 " + str(i) + " 首歌曲：" + song_down_link)
           ui.textEdit_4.insertPlainText("正在下载...\n")
           print("正在下载...")
           QApplication.processEvents()



           response = requests.get(song_down_link, headers=header).content
           f = open(song_name + ".mp3", 'wb')
           f.write(response)
           f.close()
           ui.textEdit_4.insertPlainText("下载完成.\n")
           ui.pushButton.setText("已完成{:.2f}%".format(i*100/choicelimit))
           print("下载完成.\n")
           QApplication.processEvents()
           i = i + 1



    elif xuanze == "2" :
       song_name=strtwo
       song_id=strone
       song_down_link = "http://music.163.com/song/media/outer/url?id=" + song_id + ".mp3"
       ui.textEdit_4.insertPlainText("正在下载...\n")
       print("正在下载...")
       QApplication.processEvents()



       response = requests.get(song_down_link, headers=header).content
       f = open(song_name + ".mp3", 'wb')
       f.write(response)
       f.close()
       ui.textEdit_4.insertPlainText("下载完成.\n")
       print("下载完成.\n")
       QApplication.processEvents()

    else:
        ui.textEdit_4.setText("ERROR!")
        ui.pushButton.setEnabled(True)
        ui.pushButton_2.setEnabled(True)
        ui.pushButton_3.setEnabled(True)
        ui.textEdit_4.setEnabled(True)
        ui.pushButton.setText("开始下载")
        return

    ui.pushButton.setEnabled(True)
    ui.pushButton_2.setEnabled(True)
    ui.pushButton_3.setEnabled(True)
    ui.textEdit_4.setEnabled(True)
    ui.pushButton.setText("开始下载")

@Slot()
def slottwo():
    global xuanze
    xuanze = "1"

@Slot()
def slotthree():
    global xuanze
    xuanze = "2"
    ui.textEdit_3.setText("1")

@Slot()
def slotfour():
    ui.textEdit.setText("")
    ui.textEdit_2.setText("")
    ui.textEdit_3.setText("")

@Slot()
def slotfive():
    ui.textEdit_4.setText("")





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_NeteaseCloudMusic_Download()
    ui.setupUi(window)
    xuanze = "-1"
    window.show()
    sys.exit(app.exec())
