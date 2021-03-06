# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_magnetAppStartup.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_magnetAppStartup(object):
    def setupUi(self, magnetAppStartup):
        magnetAppStartup.setObjectName(_fromUtf8("magnetAppStartup"))
        magnetAppStartup.resize(1014, 734)
        self.centralwidget = QtGui.QWidget(magnetAppStartup)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(370, 380, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(500, 380, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.machineAreaSelection = QtGui.QGroupBox(self.centralwidget)
        self.machineAreaSelection.setGeometry(QtCore.QRect(360, 140, 193, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.machineAreaSelection.setFont(font)
        self.machineAreaSelection.setAlignment(QtCore.Qt.AlignCenter)
        self.machineAreaSelection.setObjectName(_fromUtf8("machineAreaSelection"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.machineAreaSelection)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.VELA_INJ = QtGui.QRadioButton(self.machineAreaSelection)
        self.VELA_INJ.setObjectName(_fromUtf8("VELA_INJ"))
        self.verticalLayout_3.addWidget(self.VELA_INJ)
        self.VELA_BA1 = QtGui.QRadioButton(self.machineAreaSelection)
        self.VELA_BA1.setObjectName(_fromUtf8("VELA_BA1"))
        self.verticalLayout_3.addWidget(self.VELA_BA1)
        self.VELA_BA2 = QtGui.QRadioButton(self.machineAreaSelection)
        self.VELA_BA2.setObjectName(_fromUtf8("VELA_BA2"))
        self.verticalLayout_3.addWidget(self.VELA_BA2)
        self.CLARA_PHASE_1 = QtGui.QRadioButton(self.machineAreaSelection)
        self.CLARA_PHASE_1.setObjectName(_fromUtf8("CLARA_PHASE_1"))
        self.verticalLayout_3.addWidget(self.CLARA_PHASE_1)
        self.CLARA_2_VELA = QtGui.QRadioButton(self.machineAreaSelection)
        self.CLARA_2_VELA.setObjectName(_fromUtf8("CLARA_2_VELA"))
        self.verticalLayout_3.addWidget(self.CLARA_2_VELA)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.CLARA_PHASE_1.raise_()
        self.VELA_BA2.raise_()
        self.VELA_BA1.raise_()
        self.VELA_INJ.raise_()
        self.CLARA_2_VELA.raise_()
        self.modeSelection = QtGui.QGroupBox(self.centralwidget)
        self.modeSelection.setGeometry(QtCore.QRect(580, 140, 301, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modeSelection.setFont(font)
        self.modeSelection.setObjectName(_fromUtf8("modeSelection"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.modeSelection)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.offlineMode = QtGui.QRadioButton(self.modeSelection)
        self.offlineMode.setObjectName(_fromUtf8("offlineMode"))
        self.verticalLayout_2.addWidget(self.offlineMode)
        self.virtualMode = QtGui.QRadioButton(self.modeSelection)
        self.virtualMode.setObjectName(_fromUtf8("virtualMode"))
        self.verticalLayout_2.addWidget(self.virtualMode)
        self.physicalMode = QtGui.QRadioButton(self.modeSelection)
        self.physicalMode.setObjectName(_fromUtf8("physicalMode"))
        self.verticalLayout_2.addWidget(self.physicalMode)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.instructionLabel = QtGui.QLabel(self.centralwidget)
        self.instructionLabel.setGeometry(QtCore.QRect(350, 50, 611, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instructionLabel.setFont(font)
        self.instructionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.instructionLabel.setObjectName(_fromUtf8("instructionLabel"))
        self.iconLabel = QtGui.QLabel(self.centralwidget)
        self.iconLabel.setGeometry(QtCore.QRect(30, 100, 221, 261))
        self.iconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.iconLabel.setObjectName(_fromUtf8("iconLabel"))
        self.waitMessageLabel = QtGui.QLabel(self.centralwidget)
        self.waitMessageLabel.setGeometry(QtCore.QRect(100, 460, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.waitMessageLabel.setFont(font)
        self.waitMessageLabel.setObjectName(_fromUtf8("waitMessageLabel"))
        self.logoLabel = QtGui.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(30, 550, 951, 111))
        self.logoLabel.setObjectName(_fromUtf8("logoLabel"))
        magnetAppStartup.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(magnetAppStartup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1014, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        magnetAppStartup.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(magnetAppStartup)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        magnetAppStartup.setStatusBar(self.statusbar)

        self.retranslateUi(magnetAppStartup)
        QtCore.QMetaObject.connectSlotsByName(magnetAppStartup)

    def retranslateUi(self, magnetAppStartup):
        magnetAppStartup.setWindowTitle(_translate("magnetAppStartup", "MainWindow", None))
        self.startButton.setText(_translate("magnetAppStartup", "START", None))
        self.cancelButton.setText(_translate("magnetAppStartup", "CANCEL", None))
        self.machineAreaSelection.setTitle(_translate("magnetAppStartup", "Machine Area", None))
        self.VELA_INJ.setText(_translate("magnetAppStartup", "VELA  INJ Magnets", None))
        self.VELA_BA1.setText(_translate("magnetAppStartup", "VELA  BA1 Magnets", None))
        self.VELA_BA2.setText(_translate("magnetAppStartup", "VELA  BA2 Magnets", None))
        self.CLARA_PHASE_1.setText(_translate("magnetAppStartup", "CLARA PHASE 1 Magnets", None))
        self.CLARA_2_VELA.setText(_translate("magnetAppStartup", "CLARA 2 VELA", None))
        self.modeSelection.setTitle(_translate("magnetAppStartup", "Mode Selection", None))
        self.offlineMode.setText(_translate("magnetAppStartup", "Offline   (No EPICS)", None))
        self.virtualMode.setText(_translate("magnetAppStartup", "Virtual   (Connect to Virtual Machine)", None))
        self.physicalMode.setText(_translate("magnetAppStartup", "Physical (Connect to Real Machine)", None))
        self.instructionLabel.setText(_translate("magnetAppStartup", "Welcome to the VELA-CLARA Magnet Application \n"
"Please Choose a Machine Area and an Operating Mode \n"
"Then Press START ", None))
        self.iconLabel.setText(_translate("magnetAppStartup", "Icon Label ", None))
        self.waitMessageLabel.setText(_translate("magnetAppStartup", "placeholder", None))
        self.logoLabel.setText(_translate("magnetAppStartup", "TextLabel", None))

