#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

import datetime
import os
from wireless import Wireless
from alsaaudio import Mixer

currentDT = datetime.datetime.now()

class Dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setFixedSize(400, 600)
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #020202")
        layout = QVBoxLayout()

        label_time = QLabel(self)
        label_time.setText(str(currentDT.hour)+":"+str(currentDT.minute))
        label_time.setFont(QFont('Pontano Sans', 40))
        label_time.setAlignment(Qt.AlignCenter)
        label_time.setStyleSheet("color: #efefef")
        layout.addWidget(label_time)

        label_date = QLabel(self)
        label_date.setText(str(currentDT.day)+"/"+str(currentDT.month)+"/"+str(currentDT.year))
        label_date.setFont(QFont('Pontano Sans', 30))
        label_date.setAlignment(Qt.AlignCenter)
        label_date.setStyleSheet("color: #efefef")
        layout.addWidget(label_date)

        wire = Wireless()
        connected_ESSID = wire.current()

        grid = QGridLayout()
        label_network_icon = QLabel(self)
        temp = QPixmap('icons/wifi.svg')
        pixmap = temp.scaled(32, 32, QtCore.Qt.KeepAspectRatio)
        label_network_icon.setPixmap(pixmap)
        layout.addWidget(label_network_icon)

        label_connected_ESSID = QLabel(self)
        label_connected_ESSID.setText(connected_ESSID)
        label_connected_ESSID.setFont(QFont('Pontano Sans', 20))
        label_connected_ESSID.setAlignment(Qt.AlignCenter)
        label_connected_ESSID.setStyleSheet("color: #efefef")
        label_connected_ESSID.top = 10
        layout.addWidget(label_connected_ESSID)

        m = Mixer()
        muted = m.getmute()[0]
        vol = m.getvolume()[0]
        label_volume = QLabel(self)
        if muted:
            label_volume.setText("Volume:\t\t"+"muted")
        else:
            label_volume.setText("Volume:\t\t"+str(vol))
        label_volume.setFont(QFont('Pontano Sans', 20))
        label_volume.setAlignment(Qt.AlignCenter)
        label_volume.setStyleSheet("color: #efefef")
        label_volume.top = 10
        layout.addWidget(label_volume)

        button = QPushButton(self, text="Connect bluetooth")
        layout.addWidget(button);

        self.setLayout(layout);

if __name__ == "__main__":
    app = QApplication([])
    dialog = Dialog()
    dialog.show()
    app.exec_()
