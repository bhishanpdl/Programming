#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 17, 2017 Thu
# Last update :
# Est time    :

# Imports
from PyQt5 import Qt
import sys
app = Qt.QApplication(sys.argv)
systemtray_icon = Qt.QSystemTrayIcon(app, Qt.QIcon('/path/to/image'))
systemtray_icon.show()
systemtray_icon.showMessage('Title', 'Content')
