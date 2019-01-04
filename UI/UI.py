# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Widget.LineEdits import *

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(964, 659)
        mainWindow.setStyleSheet("/* === Shared === */\n"
"QStackedWidget, QLabel, QPushButton, QRadioButton, QCheckBox, \n"
"QGroupBox, QStatusBar, QToolButton, QComboBox, QDialog {\n"
"    background-color: #222222;\n"
"    color: #BBBBBB;\n"
"    font-family: \"Segoe UI\";\n"
"}\n"
"\n"
"/* === QWidget === */\n"
"QWidget:window {\n"
"    background: #222222;\n"
"    color: #BBBBBB;\n"
"    font-family: \"Segoe UI\";\n"
"}\n"
"\n"
"/* === QToolTip === */\n"
"QToolTip {\n"
"    background-color: #000000;\n"
"    border: 2px solid #333333;\n"
"    color: yellow;\n"
"}\n"
"\n"
"/* === QPushButton === */\n"
"QPushButton {\n"
"    border: 1px solid #333333;\n"
"    padding: 4px;\n"
"    min-width: 65px;\n"
"    min-height: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"    border-color: #444444;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111111;\n"
"    border-color: #333333;\n"
"    color: yellow;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: #333333;\n"
"}\n"
"\n"
"/* === Checkable items === */\n"
"QCheckBox::indicator, QRadioButton::indicator, QTreeView::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    background-color: #111111;\n"
"    border: 1px solid #333333;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked, QRadioButton::indicator::checked, QTreeView::indicator::checked {\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, fx:0.25, fy:0.15, radius:0.3, stop:0 #BBBBBB, stop:1 #111111);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled, QTreeView::indicator:disabled {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"QCheckBox::indicator::checked:disabled, QRadioButton::indicator::checked:disabled, QTreeView::indicator::checked:disabled {\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, fx:0.25, fy:0.15, radius:0.3, stop:0 #BBBBBB, stop:1 #444444);\n"
"}\n"
"\n"
"/* === QComboBox === */\n"
"QComboBox {\n"
"    background-color: black;\n"
"    border: 1px solid #333333;\n"
"    color: white;\n"
"    padding:1px 2em 1px 3px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    border-left: 1px solid #333333;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    border: 2px solid #333333;\n"
"    width: 6px;\n"
"    height: 6px;\n"
"    background: #5f5f5f;\n"
"}\n"
"\n"
"/* === QGroupBox === */\n"
"QGroupBox {\n"
"    border: 2px solid #333333;\n"
"    margin-top: 2ex;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: yellow;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"/* === QTabWidget === */\n"
"QTabWidget::pane {\n"
"    background: #222222;\n"
"    border: 2px solid #333333;\n"
"}\n"
"\n"
"/* === QTabBar === */\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    border: 1px solid #333333;\n"
"    border-bottom: none;\n"
"    color: #BBBBBB;\n"
"    padding-left: 5px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #333333;\n"
"    border: 1px solid #444444;\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #111111;\n"
"    border: 1px solid #333333;\n"
"    border-top: 1px solid yellow;\n"
"    border-bottom: none;\n"
"    color: yellow\n"
"}\n"
"\n"
"/* === QToolBar === */\n"
"QToolBar {\n"
"    background-color: #222222;\n"
"    border: none;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QToolBar:handle {\n"
"    background: #222222;\n"
"    border-left: 1px dotted yellow;\n"
"    color: #BBBBBB;\n"
"}\n"
"\n"
"QToolBar::separator {\n"
"    width: 6px;\n"
"    background-color: #222222;\n"
"}\n"
"\n"
"/* === QToolButton === */\n"
"QToolButton {\n"
"    border: 1px solid #333333;\n"
"    margin: 1px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #333333;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
"    padding-right: 20px; /* make way for the popup button */\n"
"}\n"
"\n"
"QToolButton::menu-button {\n"
"    border-left: 1px solid #333333;\n"
"    background: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"    border-left: 1px solid #444444;\n"
"    background: transparent;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QToolButton:checked, QToolButton:pressed {\n"
"    background-color: #111111;\n"
"    color: yellow;\n"
"}\n"
"\n"
"/* === QMenu === */\n"
"QMenu {\n"
"    background-color: black;\n"
"    border: 1px solid gray;\n"
"    color: white;\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 2px 25px 2px 20px;\n"
"    border: 1px solid transparent;\n"
"}\n"
"\n"
"QMenu::item:disabled {\n"
"    color: #666666;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    border-color: gray;\n"
"    background: #222222;\n"
"}\n"
"\n"
"QMenu::icon:checked {\n"
"\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: #222222;\n"
"    margin-left: 10px;\n"
"    margin-right: 10px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"/* === QMenuBar === */\n"
"QMenuBar {\n"
"    background-color: black;\n"
"    color: white;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:disabled {\n"
"    color: gray;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background: #222222;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #444444;\n"
"}\n"
"\n"
"/* === QScrollBar:vertical === */\n"
"QScrollBar:vertical {\n"
"    background: #111111;\n"
"    width: 16px;\n"
"    margin: 16px 0 16px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #555555;\n"
"    min-height: 16px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background: #444444;\n"
"    height: 16px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #444444;\n"
"    height: 16px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:up-arrow:vertical, QScrollBar:down-arrow:vertical {\n"
"    border: 2px solid #333333;\n"
"    width: 6px;\n"
"    height: 6px;\n"
"    background: #5f5f5f;\n"
"}\n"
"\n"
"/* === QScrollBar:horizontal === */\n"
"QScrollBar:horizontal {\n"
"    background: #111111;\n"
"    height: 16px;\n"
"    margin: 0 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #555555;\n"
"    min-width: 16px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    background: #444444;\n"
"    width: 16px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: #444444;\n"
"    width: 16px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:left-arrow:horizontal, QScrollBar:right-arrow:horizontal {\n"
"    border: 2px solid #333333;\n"
"    width: 6px;\n"
"    height: 6px;\n"
"    background: #5f5f5f;\n"
"}\n"
"\n"
"/* =================== */\n"
"QLineEdit, QListView, QTreeView, QTableView, QAbstractSpinBox {\n"
"    background-color: black;\n"
"    color: #BBBBBB;\n"
"    border: 1px solid #333333;\n"
"}\n"
"\n"
"QAbstractScrollArea, QLineEdit, QTextEdit, QAbstractSpinBox, QComboBox {\n"
"    border-color: #333333;\n"
"    border: 1px solid #333333;\n"
"\n"
"}\n"
"\n"
"/* === QHeaderView === */\n"
"QHeaderView::section {\n"
"    background: #222222;\n"
"    border: 0;\n"
"    color: #BBBBBB;\n"
"    padding: 3px 0 3px 4px;\n"
"}\n"
"\n"
"/* === QListView === */\n"
"QListView::item:hover {\n"
"    background: #333333;\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background: #111111;\n"
"    color: yellow;\n"
"}\n"
"\n"
"/* === QTableView === */\n"
"QTableView::item:hover {\n"
"    background: #333333;\n"
"}\n"
"\n"
"QTableView::item:hover {\n"
"    background: #111111;\n"
"    color: yellow;\n"
"}\n"
"\n"
"/* === QTreeView === */\n"
"QTreeView::item {\n"
"    background: black;\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background: #333333;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    background: #111111;\n"
"    color: yellow;\n"
"}\n"
"\n"
"QTreeView::branch {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:adjoins-item {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:has-siblings:!adjoins-item {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings {\n"
"\n"
"}\n"
"\n"
"/* === Customizations === */\n"
"QFrame#infoLabel {\n"
"    border: 1px inset #333333;\n"
"}\n"
"2.\n"
".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"QToolBar {\n"
"    background-color: beige;\n"
"}\n"
"\n"
"QDialog, QFileDialog {\n"
"    background-color: beige;\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar, QTabWidget {\n"
"    background-color: beige;\n"
"}\n"
"QTabBar::tab {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"     border: 1px solid darkkhaki;\n"
"     border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 8ex;\n"
"     padding: 2px;\n"
" }\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                       stop:0 #616161, stop: 0.5 #505050,\n"
"                                       stop: 0.6 #434343, stop:1 #656565);\n"
"     color: white;\n"
"     padding-left: 4px;\n"
"     border: 1px solid #6c6c6c;\n"
" }\n"
"\n"
" QHeaderView::section:checked\n"
" {\n"
"     background-color: red;\n"
" }\n"
"/* === QHeaderView === */\n"
"QHeaderView::section {\n"
"    height: 20px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background: #666;\n"
"    border: 0;\n"
"    color: #000;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_87 = QtWidgets.QLabel(self.centralwidget)
        self.label_87.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_87.setObjectName("label_87")
        self.horizontalLayout.addWidget(self.label_87)
        self.editDtuIp_1 = IPEdit(self.centralwidget)
        self.editDtuIp_1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editDtuIp_1.setText("")
        self.editDtuIp_1.setObjectName("editDtuIp_1")
        self.horizontalLayout.addWidget(self.editDtuIp_1)
        self.editDtuIp_2 = IPEdit(self.centralwidget)
        self.editDtuIp_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editDtuIp_2.setText("")
        self.editDtuIp_2.setObjectName("editDtuIp_2")
        self.horizontalLayout.addWidget(self.editDtuIp_2)
        self.editDtuIp_3 = IPEdit(self.centralwidget)
        self.editDtuIp_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editDtuIp_3.setText("")
        self.editDtuIp_3.setObjectName("editDtuIp_3")
        self.horizontalLayout.addWidget(self.editDtuIp_3)
        self.editDtuIp_4 = IPEdit(self.centralwidget)
        self.editDtuIp_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editDtuIp_4.setText("")
        self.editDtuIp_4.setObjectName("editDtuIp_4")
        self.horizontalLayout.addWidget(self.editDtuIp_4)
        self.label_88 = QtWidgets.QLabel(self.centralwidget)
        self.label_88.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_88.setObjectName("label_88")
        self.horizontalLayout.addWidget(self.label_88)
        self.editDeviceAdr = AddressEdit(self.centralwidget)
        self.editDeviceAdr.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editDeviceAdr.setText("")
        self.editDeviceAdr.setObjectName("editDeviceAdr")
        self.horizontalLayout.addWidget(self.editDeviceAdr)
        self.label_89 = QtWidgets.QLabel(self.centralwidget)
        self.label_89.setObjectName("label_89")
        self.horizontalLayout.addWidget(self.label_89)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.editMqttAdr = IPEdit(self.centralwidget)
        self.editMqttAdr.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editMqttAdr.setObjectName("editMqttAdr")
        self.horizontalLayout.addWidget(self.editMqttAdr)
        self.editMqttAdr_2 = IPEdit(self.centralwidget)
        self.editMqttAdr_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editMqttAdr_2.setObjectName("editMqttAdr_2")
        self.horizontalLayout.addWidget(self.editMqttAdr_2)
        self.editMqttAdr_3 = IPEdit(self.centralwidget)
        self.editMqttAdr_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editMqttAdr_3.setObjectName("editMqttAdr_3")
        self.horizontalLayout.addWidget(self.editMqttAdr_3)
        self.editMqttAdr_4 = IPEdit(self.centralwidget)
        self.editMqttAdr_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.editMqttAdr_4.setObjectName("editMqttAdr_4")
        self.horizontalLayout.addWidget(self.editMqttAdr_4)
        self.label_86 = QtWidgets.QLabel(self.centralwidget)
        self.label_86.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_86.setObjectName("label_86")
        self.horizontalLayout.addWidget(self.label_86)
        self.editMqttPort = PortEdit(self.centralwidget)
        self.editMqttPort.setMaximumSize(QtCore.QSize(60, 16777215))
        self.editMqttPort.setObjectName("editMqttPort")
        self.horizontalLayout.addWidget(self.editMqttPort)
        self.btnMqttConnect = QtWidgets.QPushButton(self.centralwidget)
        self.btnMqttConnect.setMinimumSize(QtCore.QSize(75, 22))
        self.btnMqttConnect.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnMqttConnect.setObjectName("btnMqttConnect")
        self.horizontalLayout.addWidget(self.btnMqttConnect)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_49 = QtWidgets.QLabel(self.groupBox_12)
        self.label_49.setObjectName("label_49")
        self.gridLayout_15.addWidget(self.label_49, 0, 0, 1, 1)
        self.comBootStatus = QtWidgets.QComboBox(self.groupBox_12)
        self.comBootStatus.setObjectName("comBootStatus")
        self.comBootStatus.addItem("")
        self.comBootStatus.addItem("")
        self.gridLayout_15.addWidget(self.comBootStatus, 0, 1, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.groupBox_12)
        self.label_50.setObjectName("label_50")
        self.gridLayout_15.addWidget(self.label_50, 0, 2, 1, 1)
        self.comWorkMode = QtWidgets.QComboBox(self.groupBox_12)
        self.comWorkMode.setObjectName("comWorkMode")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.comWorkMode.addItem("")
        self.gridLayout_15.addWidget(self.comWorkMode, 0, 3, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.groupBox_12)
        self.label_51.setObjectName("label_51")
        self.gridLayout_15.addWidget(self.label_51, 1, 0, 1, 1)
        self.comSupplyHeat = QtWidgets.QComboBox(self.groupBox_12)
        self.comSupplyHeat.setObjectName("comSupplyHeat")
        self.comSupplyHeat.addItem("")
        self.comSupplyHeat.addItem("")
        self.gridLayout_15.addWidget(self.comSupplyHeat, 1, 1, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.groupBox_12)
        self.label_52.setObjectName("label_52")
        self.gridLayout_15.addWidget(self.label_52, 1, 2, 1, 1)
        self.comDayMode = QtWidgets.QComboBox(self.groupBox_12)
        self.comDayMode.setObjectName("comDayMode")
        self.comDayMode.addItem("")
        self.comDayMode.addItem("")
        self.gridLayout_15.addWidget(self.comDayMode, 1, 3, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.groupBox_12)
        self.label_53.setObjectName("label_53")
        self.gridLayout_15.addWidget(self.label_53, 2, 0, 1, 1)
        self.edtMinReft = MinReftEdit(self.groupBox_12)
        self.edtMinReft.setObjectName("edtMinReft")
        self.gridLayout_15.addWidget(self.edtMinReft, 2, 1, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.groupBox_12)
        self.label_54.setObjectName("label_54")
        self.gridLayout_15.addWidget(self.label_54, 2, 2, 1, 1)
        self.edtMaxRefT = MaxReftEdit(self.groupBox_12)
        self.edtMaxRefT.setObjectName("edtMaxRefT")
        self.gridLayout_15.addWidget(self.edtMaxRefT, 2, 3, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_hint_8 = QtWidgets.QLabel(self.groupBox_12)
        self.label_hint_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_hint_8.setText("")
        self.label_hint_8.setObjectName("label_hint_8")
        self.horizontalLayout_10.addWidget(self.label_hint_8)
        self.btnSetSysStatus = QtWidgets.QPushButton(self.groupBox_12)
        self.btnSetSysStatus.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSetSysStatus.setObjectName("btnSetSysStatus")
        self.horizontalLayout_10.addWidget(self.btnSetSysStatus)
        self.gridLayout_15.addLayout(self.horizontalLayout_10, 3, 0, 1, 4)
        self.verticalLayout_2.addWidget(self.groupBox_12)
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_55 = QtWidgets.QLabel(self.groupBox_13)
        self.label_55.setObjectName("label_55")
        self.gridLayout_16.addWidget(self.label_55, 0, 0, 1, 1)
        self.edtTimeTable1 = QtWidgets.QLineEdit(self.groupBox_13)
        self.edtTimeTable1.setObjectName("edtTimeTable1")
        self.gridLayout_16.addWidget(self.edtTimeTable1, 0, 1, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.groupBox_13)
        self.label_56.setObjectName("label_56")
        self.gridLayout_16.addWidget(self.label_56, 0, 2, 1, 1)
        self.edtTimeTable2 = QtWidgets.QLineEdit(self.groupBox_13)
        self.edtTimeTable2.setObjectName("edtTimeTable2")
        self.gridLayout_16.addWidget(self.edtTimeTable2, 0, 3, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.groupBox_13)
        self.label_57.setObjectName("label_57")
        self.gridLayout_16.addWidget(self.label_57, 1, 0, 1, 1)
        self.edtTimeTable3 = QtWidgets.QLineEdit(self.groupBox_13)
        self.edtTimeTable3.setObjectName("edtTimeTable3")
        self.gridLayout_16.addWidget(self.edtTimeTable3, 1, 1, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.groupBox_13)
        self.label_58.setObjectName("label_58")
        self.gridLayout_16.addWidget(self.label_58, 1, 2, 1, 1)
        self.edtTimeTable4 = QtWidgets.QLineEdit(self.groupBox_13)
        self.edtTimeTable4.setObjectName("edtTimeTable4")
        self.gridLayout_16.addWidget(self.edtTimeTable4, 1, 3, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.groupBox_13)
        self.label_59.setObjectName("label_59")
        self.gridLayout_16.addWidget(self.label_59, 2, 0, 1, 1)
        self.edtTimeTable5 = QtWidgets.QLineEdit(self.groupBox_13)
        self.edtTimeTable5.setObjectName("edtTimeTable5")
        self.gridLayout_16.addWidget(self.edtTimeTable5, 2, 1, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.groupBox_13)
        self.label_60.setObjectName("label_60")
        self.gridLayout_16.addWidget(self.label_60, 2, 2, 1, 1)
        self.edtTimeTable6 = QtWidgets.QLineEdit(self.groupBox_13)
        self.edtTimeTable6.setObjectName("edtTimeTable6")
        self.gridLayout_16.addWidget(self.edtTimeTable6, 2, 3, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.groupBox_13)
        self.label_61.setObjectName("label_61")
        self.gridLayout_16.addWidget(self.label_61, 3, 0, 1, 1)
        self.edtTimeTable7 = QtWidgets.QLineEdit(self.groupBox_13)
        self.edtTimeTable7.setObjectName("edtTimeTable7")
        self.gridLayout_16.addWidget(self.edtTimeTable7, 3, 1, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.groupBox_13)
        self.label_62.setObjectName("label_62")
        self.gridLayout_16.addWidget(self.label_62, 3, 2, 1, 1)
        self.edtTimeTable8 = QtWidgets.QLineEdit(self.groupBox_13)
        self.edtTimeTable8.setObjectName("edtTimeTable8")
        self.gridLayout_16.addWidget(self.edtTimeTable8, 3, 3, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.groupBox_13)
        self.label_63.setObjectName("label_63")
        self.gridLayout_16.addWidget(self.label_63, 4, 0, 1, 1)
        self.edtTimeTable9 = QtWidgets.QLineEdit(self.groupBox_13)
        self.edtTimeTable9.setObjectName("edtTimeTable9")
        self.gridLayout_16.addWidget(self.edtTimeTable9, 4, 1, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.groupBox_13)
        self.label_64.setObjectName("label_64")
        self.gridLayout_16.addWidget(self.label_64, 4, 2, 1, 1)
        self.edtTimeTable10 = QtWidgets.QLineEdit(self.groupBox_13)
        self.edtTimeTable10.setObjectName("edtTimeTable10")
        self.gridLayout_16.addWidget(self.edtTimeTable10, 4, 3, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.groupBox_13)
        self.label_65.setObjectName("label_65")
        self.gridLayout_16.addWidget(self.label_65, 5, 0, 1, 1)
        self.comTimeTableNum = QtWidgets.QComboBox(self.groupBox_13)
        self.comTimeTableNum.setObjectName("comTimeTableNum")
        self.comTimeTableNum.addItem("")
        self.comTimeTableNum.addItem("")
        self.comTimeTableNum.addItem("")
        self.comTimeTableNum.addItem("")
        self.comTimeTableNum.addItem("")
        self.comTimeTableNum.addItem("")
        self.comTimeTableNum.addItem("")
        self.comTimeTableNum.addItem("")
        self.comTimeTableNum.addItem("")
        self.comTimeTableNum.addItem("")
        self.gridLayout_16.addWidget(self.comTimeTableNum, 5, 1, 1, 1)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_hint_9 = QtWidgets.QLabel(self.groupBox_13)
        self.label_hint_9.setText("")
        self.label_hint_9.setObjectName("label_hint_9")
        self.horizontalLayout_11.addWidget(self.label_hint_9)
        self.btnSetTimeTable = QtWidgets.QPushButton(self.groupBox_13)
        self.btnSetTimeTable.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSetTimeTable.setObjectName("btnSetTimeTable")
        self.horizontalLayout_11.addWidget(self.btnSetTimeTable)
        self.gridLayout_16.addLayout(self.horizontalLayout_11, 5, 2, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox_13)
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_66 = QtWidgets.QLabel(self.groupBox_14)
        self.label_66.setObjectName("label_66")
        self.gridLayout_17.addWidget(self.label_66, 0, 0, 1, 1)
        self.edtPinterval = QtWidgets.QLineEdit(self.groupBox_14)
        self.edtPinterval.setObjectName("edtPinterval")
        self.gridLayout_17.addWidget(self.edtPinterval, 0, 1, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.groupBox_14)
        self.label_67.setObjectName("label_67")
        self.gridLayout_17.addWidget(self.label_67, 0, 2, 1, 1)
        self.edtFinterval = QtWidgets.QLineEdit(self.groupBox_14)
        self.edtFinterval.setText("")
        self.edtFinterval.setObjectName("edtFinterval")
        self.gridLayout_17.addWidget(self.edtFinterval, 0, 3, 1, 1)
        self.btnSetInterval = QtWidgets.QPushButton(self.groupBox_14)
        self.btnSetInterval.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSetInterval.setObjectName("btnSetInterval")
        self.gridLayout_17.addWidget(self.btnSetInterval, 0, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_14)
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBox_15)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_68 = QtWidgets.QLabel(self.groupBox_15)
        self.label_68.setObjectName("label_68")
        self.gridLayout_18.addWidget(self.label_68, 0, 0, 1, 1)
        self.edtLogicTemp1 = QtWidgets.QLineEdit(self.groupBox_15)
        self.edtLogicTemp1.setObjectName("edtLogicTemp1")
        self.gridLayout_18.addWidget(self.edtLogicTemp1, 0, 1, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.groupBox_15)
        self.label_69.setObjectName("label_69")
        self.gridLayout_18.addWidget(self.label_69, 0, 2, 1, 1)
        self.edtLogicTemp2 = QtWidgets.QLineEdit(self.groupBox_15)
        self.edtLogicTemp2.setObjectName("edtLogicTemp2")
        self.gridLayout_18.addWidget(self.edtLogicTemp2, 0, 3, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.groupBox_15)
        self.label_70.setObjectName("label_70")
        self.gridLayout_18.addWidget(self.label_70, 1, 0, 1, 1)
        self.edtLogicTemp = QtWidgets.QLineEdit(self.groupBox_15)
        self.edtLogicTemp.setObjectName("edtLogicTemp")
        self.gridLayout_18.addWidget(self.edtLogicTemp, 1, 1, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_hint_10 = QtWidgets.QLabel(self.groupBox_15)
        self.label_hint_10.setText("")
        self.label_hint_10.setObjectName("label_hint_10")
        self.horizontalLayout_12.addWidget(self.label_hint_10)
        self.btnSetLogicTemp = QtWidgets.QPushButton(self.groupBox_15)
        self.btnSetLogicTemp.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSetLogicTemp.setObjectName("btnSetLogicTemp")
        self.horizontalLayout_12.addWidget(self.btnSetLogicTemp)
        self.gridLayout_18.addLayout(self.horizontalLayout_12, 1, 2, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox_15)
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_16.setObjectName("groupBox_16")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.groupBox_16)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_71 = QtWidgets.QLabel(self.groupBox_16)
        self.label_71.setObjectName("label_71")
        self.gridLayout_19.addWidget(self.label_71, 0, 0, 1, 1)
        self.edtChangeModleNum = QtWidgets.QLineEdit(self.groupBox_16)
        self.edtChangeModleNum.setObjectName("edtChangeModleNum")
        self.gridLayout_19.addWidget(self.edtChangeModleNum, 0, 1, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.groupBox_16)
        self.label_72.setObjectName("label_72")
        self.gridLayout_19.addWidget(self.label_72, 0, 2, 1, 1)
        self.edtChangeModleValue = QtWidgets.QLineEdit(self.groupBox_16)
        self.edtChangeModleValue.setText("")
        self.edtChangeModleValue.setObjectName("edtChangeModleValue")
        self.gridLayout_19.addWidget(self.edtChangeModleValue, 0, 3, 1, 1)
        self.btnSetChangeModle = QtWidgets.QPushButton(self.groupBox_16)
        self.btnSetChangeModle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSetChangeModle.setObjectName("btnSetChangeModle")
        self.gridLayout_19.addWidget(self.btnSetChangeModle, 0, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_16)
        self.gridLayout_25.addLayout(self.verticalLayout_2, 0, 0, 4, 1)
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_11.setObjectName("groupBox_11")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_11)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_44 = QtWidgets.QLabel(self.groupBox_11)
        self.label_44.setObjectName("label_44")
        self.gridLayout_14.addWidget(self.label_44, 0, 0, 1, 1)
        self.edtAlarmPress1 = QtWidgets.QLineEdit(self.groupBox_11)
        self.edtAlarmPress1.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edtAlarmPress1.setObjectName("edtAlarmPress1")
        self.gridLayout_14.addWidget(self.edtAlarmPress1, 0, 1, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.groupBox_11)
        self.label_45.setObjectName("label_45")
        self.gridLayout_14.addWidget(self.label_45, 0, 2, 1, 1)
        self.edtAlarmPress2 = QtWidgets.QLineEdit(self.groupBox_11)
        self.edtAlarmPress2.setObjectName("edtAlarmPress2")
        self.gridLayout_14.addWidget(self.edtAlarmPress2, 0, 3, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.groupBox_11)
        self.label_46.setObjectName("label_46")
        self.gridLayout_14.addWidget(self.label_46, 1, 0, 1, 1)
        self.edtAlarmFlow1 = QtWidgets.QLineEdit(self.groupBox_11)
        self.edtAlarmFlow1.setObjectName("edtAlarmFlow1")
        self.gridLayout_14.addWidget(self.edtAlarmFlow1, 1, 1, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.groupBox_11)
        self.label_47.setObjectName("label_47")
        self.gridLayout_14.addWidget(self.label_47, 1, 2, 1, 1)
        self.edtAlarmFlow2 = QtWidgets.QLineEdit(self.groupBox_11)
        self.edtAlarmFlow2.setObjectName("edtAlarmFlow2")
        self.gridLayout_14.addWidget(self.edtAlarmFlow2, 1, 3, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.groupBox_11)
        self.label_48.setObjectName("label_48")
        self.gridLayout_14.addWidget(self.label_48, 2, 0, 1, 1)
        self.edtAlarmTemp = QtWidgets.QLineEdit(self.groupBox_11)
        self.edtAlarmTemp.setObjectName("edtAlarmTemp")
        self.gridLayout_14.addWidget(self.edtAlarmTemp, 2, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_hint_7 = QtWidgets.QLabel(self.groupBox_11)
        self.label_hint_7.setText("")
        self.label_hint_7.setObjectName("label_hint_7")
        self.horizontalLayout_9.addWidget(self.label_hint_7)
        self.btnSetAlarm = QtWidgets.QPushButton(self.groupBox_11)
        self.btnSetAlarm.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSetAlarm.setObjectName("btnSetAlarm")
        self.horizontalLayout_9.addWidget(self.btnSetAlarm)
        self.gridLayout_14.addLayout(self.horizontalLayout_9, 2, 2, 1, 2)
        self.gridLayout_25.addWidget(self.groupBox_11, 0, 1, 1, 1)
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_19.setObjectName("groupBox_19")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.groupBox_19)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.label_75 = QtWidgets.QLabel(self.groupBox_19)
        self.label_75.setObjectName("label_75")
        self.gridLayout_23.addWidget(self.label_75, 0, 0, 1, 1)
        self.edtSolarTemp1 = QtWidgets.QLineEdit(self.groupBox_19)
        self.edtSolarTemp1.setObjectName("edtSolarTemp1")
        self.gridLayout_23.addWidget(self.edtSolarTemp1, 0, 1, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.groupBox_19)
        self.label_76.setObjectName("label_76")
        self.gridLayout_23.addWidget(self.label_76, 0, 2, 1, 1)
        self.edtSolarTemp2 = QtWidgets.QLineEdit(self.groupBox_19)
        self.edtSolarTemp2.setObjectName("edtSolarTemp2")
        self.gridLayout_23.addWidget(self.edtSolarTemp2, 0, 3, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.groupBox_19)
        self.label_77.setObjectName("label_77")
        self.gridLayout_23.addWidget(self.label_77, 1, 0, 1, 1)
        self.edtSolarTemp3 = QtWidgets.QLineEdit(self.groupBox_19)
        self.edtSolarTemp3.setObjectName("edtSolarTemp3")
        self.gridLayout_23.addWidget(self.edtSolarTemp3, 1, 1, 1, 1)
        self.label_78 = QtWidgets.QLabel(self.groupBox_19)
        self.label_78.setObjectName("label_78")
        self.gridLayout_23.addWidget(self.label_78, 1, 2, 1, 1)
        self.edtSolarTemp4 = QtWidgets.QLineEdit(self.groupBox_19)
        self.edtSolarTemp4.setObjectName("edtSolarTemp4")
        self.gridLayout_23.addWidget(self.edtSolarTemp4, 1, 3, 1, 1)
        self.label_79 = QtWidgets.QLabel(self.groupBox_19)
        self.label_79.setObjectName("label_79")
        self.gridLayout_23.addWidget(self.label_79, 2, 0, 1, 1)
        self.edtJudgeTemp1 = QtWidgets.QLineEdit(self.groupBox_19)
        self.edtJudgeTemp1.setObjectName("edtJudgeTemp1")
        self.gridLayout_23.addWidget(self.edtJudgeTemp1, 2, 1, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.groupBox_19)
        self.label_80.setObjectName("label_80")
        self.gridLayout_23.addWidget(self.label_80, 2, 2, 1, 1)
        self.edtJudgeTemp2 = QtWidgets.QLineEdit(self.groupBox_19)
        self.edtJudgeTemp2.setObjectName("edtJudgeTemp2")
        self.gridLayout_23.addWidget(self.edtJudgeTemp2, 2, 3, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.groupBox_19)
        self.label_81.setObjectName("label_81")
        self.gridLayout_23.addWidget(self.label_81, 3, 0, 1, 1)
        self.edtJudgeTemp3 = QtWidgets.QLineEdit(self.groupBox_19)
        self.edtJudgeTemp3.setObjectName("edtJudgeTemp3")
        self.gridLayout_23.addWidget(self.edtJudgeTemp3, 3, 1, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_hint_11 = QtWidgets.QLabel(self.groupBox_19)
        self.label_hint_11.setText("")
        self.label_hint_11.setObjectName("label_hint_11")
        self.horizontalLayout_14.addWidget(self.label_hint_11)
        self.btnSetJudgeTemp = QtWidgets.QPushButton(self.groupBox_19)
        self.btnSetJudgeTemp.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSetJudgeTemp.setObjectName("btnSetJudgeTemp")
        self.horizontalLayout_14.addWidget(self.btnSetJudgeTemp)
        self.gridLayout_23.addLayout(self.horizontalLayout_14, 3, 2, 1, 2)
        self.gridLayout_25.addWidget(self.groupBox_19, 1, 1, 1, 1)
        self.groupBox_20 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.groupBox_20)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_82 = QtWidgets.QLabel(self.groupBox_20)
        self.label_82.setObjectName("label_82")
        self.gridLayout_24.addWidget(self.label_82, 0, 0, 1, 1)
        self.edtOtherSolar = QtWidgets.QLineEdit(self.groupBox_20)
        self.edtOtherSolar.setObjectName("edtOtherSolar")
        self.gridLayout_24.addWidget(self.edtOtherSolar, 0, 1, 1, 1)
        self.label_83 = QtWidgets.QLabel(self.groupBox_20)
        self.label_83.setObjectName("label_83")
        self.gridLayout_24.addWidget(self.label_83, 0, 2, 1, 1)
        self.edtOtherWaterOut = QtWidgets.QLineEdit(self.groupBox_20)
        self.edtOtherWaterOut.setObjectName("edtOtherWaterOut")
        self.gridLayout_24.addWidget(self.edtOtherWaterOut, 0, 3, 1, 1)
        self.label_84 = QtWidgets.QLabel(self.groupBox_20)
        self.label_84.setObjectName("label_84")
        self.gridLayout_24.addWidget(self.label_84, 1, 0, 1, 1)
        self.edtOtherTemp = QtWidgets.QLineEdit(self.groupBox_20)
        self.edtOtherTemp.setObjectName("edtOtherTemp")
        self.gridLayout_24.addWidget(self.edtOtherTemp, 1, 1, 1, 1)
        self.label_85 = QtWidgets.QLabel(self.groupBox_20)
        self.label_85.setObjectName("label_85")
        self.gridLayout_24.addWidget(self.label_85, 1, 2, 1, 1)
        self.edtOtherWaterIn = QtWidgets.QLineEdit(self.groupBox_20)
        self.edtOtherWaterIn.setObjectName("edtOtherWaterIn")
        self.gridLayout_24.addWidget(self.edtOtherWaterIn, 1, 3, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_hint_12 = QtWidgets.QLabel(self.groupBox_20)
        self.label_hint_12.setText("")
        self.label_hint_12.setObjectName("label_hint_12")
        self.horizontalLayout_15.addWidget(self.label_hint_12)
        self.btnSetOtherValue = QtWidgets.QPushButton(self.groupBox_20)
        self.btnSetOtherValue.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSetOtherValue.setObjectName("btnSetOtherValue")
        self.horizontalLayout_15.addWidget(self.btnSetOtherValue)
        self.gridLayout_24.addLayout(self.horizontalLayout_15, 2, 0, 1, 4)
        self.gridLayout_25.addWidget(self.groupBox_20, 2, 1, 1, 1)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.groupBox_17 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.groupBox_17)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_73 = QtWidgets.QLabel(self.groupBox_17)
        self.label_73.setObjectName("label_73")
        self.gridLayout_21.addWidget(self.label_73, 0, 2, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.groupBox_17)
        self.label_74.setObjectName("label_74")
        self.gridLayout_21.addWidget(self.label_74, 0, 0, 1, 1)
        self.timeEditWrok = QtWidgets.QTimeEdit(self.groupBox_17)
        self.timeEditWrok.setObjectName("timeEditWrok")
        self.gridLayout_21.addWidget(self.timeEditWrok, 0, 1, 1, 1)
        self.timeEditOffWork = QtWidgets.QTimeEdit(self.groupBox_17)
        self.timeEditOffWork.setObjectName("timeEditOffWork")
        self.gridLayout_21.addWidget(self.timeEditOffWork, 0, 3, 1, 1)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.rdoWorkday = QtWidgets.QRadioButton(self.groupBox_17)
        self.rdoWorkday.setChecked(True)
        self.rdoWorkday.setObjectName("rdoWorkday")
        self.horizontalLayout_13.addWidget(self.rdoWorkday)
        self.rdoWeekday = QtWidgets.QRadioButton(self.groupBox_17)
        self.rdoWeekday.setObjectName("rdoWeekday")
        self.horizontalLayout_13.addWidget(self.rdoWeekday)
        self.btnSetWorkTime = QtWidgets.QPushButton(self.groupBox_17)
        self.btnSetWorkTime.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnSetWorkTime.setObjectName("btnSetWorkTime")
        self.horizontalLayout_13.addWidget(self.btnSetWorkTime)
        self.gridLayout_21.addLayout(self.horizontalLayout_13, 2, 0, 1, 4)
        self.gridLayout_20.addWidget(self.groupBox_17, 0, 0, 1, 1)
        self.groupBox_18 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.groupBox_18)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.btnSetOtherTime = QtWidgets.QPushButton(self.groupBox_18)
        self.btnSetOtherTime.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnSetOtherTime.setObjectName("btnSetOtherTime")
        self.gridLayout_22.addWidget(self.btnSetOtherTime, 0, 0, 1, 1)
        self.btnSetCleanElc = QtWidgets.QPushButton(self.groupBox_18)
        self.btnSetCleanElc.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnSetCleanElc.setObjectName("btnSetCleanElc")
        self.gridLayout_22.addWidget(self.btnSetCleanElc, 0, 1, 1, 1)
        self.gridLayout_20.addWidget(self.groupBox_18, 0, 1, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_20, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_48 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_47 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_47.addWidget(self.label_2, 0, 0, 1, 1)
        self.edtShowBootStatus = QtWidgets.QLineEdit(self.groupBox)
        self.edtShowBootStatus.setReadOnly(True)
        self.edtShowBootStatus.setObjectName("edtShowBootStatus")
        self.gridLayout_47.addWidget(self.edtShowBootStatus, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_47.addWidget(self.label_3, 0, 2, 1, 1)
        self.edtShowWorkMode = QtWidgets.QLineEdit(self.groupBox)
        self.edtShowWorkMode.setReadOnly(True)
        self.edtShowWorkMode.setObjectName("edtShowWorkMode")
        self.gridLayout_47.addWidget(self.edtShowWorkMode, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_47.addWidget(self.label_4, 1, 0, 1, 1)
        self.edtShowSupplyHeat = QtWidgets.QLineEdit(self.groupBox)
        self.edtShowSupplyHeat.setReadOnly(True)
        self.edtShowSupplyHeat.setObjectName("edtShowSupplyHeat")
        self.gridLayout_47.addWidget(self.edtShowSupplyHeat, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_47.addWidget(self.label_5, 1, 2, 1, 1)
        self.edtShowDayMode = QtWidgets.QLineEdit(self.groupBox)
        self.edtShowDayMode.setReadOnly(True)
        self.edtShowDayMode.setObjectName("edtShowDayMode")
        self.gridLayout_47.addWidget(self.edtShowDayMode, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_47.addWidget(self.label_6, 2, 0, 1, 1)
        self.edtShowMinReft = QtWidgets.QLineEdit(self.groupBox)
        self.edtShowMinReft.setReadOnly(True)
        self.edtShowMinReft.setObjectName("edtShowMinReft")
        self.gridLayout_47.addWidget(self.edtShowMinReft, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_47.addWidget(self.label_7, 2, 2, 1, 1)
        self.edtShowMaxRefT = QtWidgets.QLineEdit(self.groupBox)
        self.edtShowMaxRefT.setReadOnly(True)
        self.edtShowMaxRefT.setObjectName("edtShowMaxRefT")
        self.gridLayout_47.addWidget(self.edtShowMaxRefT, 2, 3, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_hint_1 = QtWidgets.QLabel(self.groupBox)
        self.label_hint_1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_hint_1.setText("")
        self.label_hint_1.setObjectName("label_hint_1")
        self.horizontalLayout_2.addWidget(self.label_hint_1)
        self.btnReadSysStatus = QtWidgets.QPushButton(self.groupBox)
        self.btnReadSysStatus.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnReadSysStatus.setObjectName("btnReadSysStatus")
        self.horizontalLayout_2.addWidget(self.btnReadSysStatus)
        self.gridLayout_47.addLayout(self.horizontalLayout_2, 3, 0, 1, 4)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.edtReadTimeTable1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtReadTimeTable1.setReadOnly(True)
        self.edtReadTimeTable1.setObjectName("edtReadTimeTable1")
        self.gridLayout_3.addWidget(self.edtReadTimeTable1, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 0, 2, 1, 1)
        self.edtReadTimeTable1_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtReadTimeTable1_2.setReadOnly(True)
        self.edtReadTimeTable1_2.setObjectName("edtReadTimeTable1_2")
        self.gridLayout_3.addWidget(self.edtReadTimeTable1_2, 0, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)
        self.edtReadTimeTable3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtReadTimeTable3.setReadOnly(True)
        self.edtReadTimeTable3.setObjectName("edtReadTimeTable3")
        self.gridLayout_3.addWidget(self.edtReadTimeTable3, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 2, 1, 1)
        self.edtReadTimeTable4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtReadTimeTable4.setReadOnly(True)
        self.edtReadTimeTable4.setObjectName("edtReadTimeTable4")
        self.gridLayout_3.addWidget(self.edtReadTimeTable4, 1, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)
        self.edtReadTimeTable5 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtReadTimeTable5.setReadOnly(True)
        self.edtReadTimeTable5.setObjectName("edtReadTimeTable5")
        self.gridLayout_3.addWidget(self.edtReadTimeTable5, 2, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 2, 2, 1, 1)
        self.edtReadTimeTable6 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtReadTimeTable6.setReadOnly(True)
        self.edtReadTimeTable6.setObjectName("edtReadTimeTable6")
        self.gridLayout_3.addWidget(self.edtReadTimeTable6, 2, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 3, 0, 1, 1)
        self.edtReadTimeTable7 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtReadTimeTable7.setReadOnly(True)
        self.edtReadTimeTable7.setObjectName("edtReadTimeTable7")
        self.gridLayout_3.addWidget(self.edtReadTimeTable7, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 3, 2, 1, 1)
        self.edtReadTimeTable8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtReadTimeTable8.setReadOnly(True)
        self.edtReadTimeTable8.setObjectName("edtReadTimeTable8")
        self.gridLayout_3.addWidget(self.edtReadTimeTable8, 3, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 4, 0, 1, 1)
        self.edtReadTimeTable9 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtReadTimeTable9.setReadOnly(True)
        self.edtReadTimeTable9.setObjectName("edtReadTimeTable9")
        self.gridLayout_3.addWidget(self.edtReadTimeTable9, 4, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 4, 2, 1, 1)
        self.edtReadTimeTable10 = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtReadTimeTable10.setReadOnly(True)
        self.edtReadTimeTable10.setObjectName("edtReadTimeTable10")
        self.gridLayout_3.addWidget(self.edtReadTimeTable10, 4, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 5, 0, 1, 1)
        self.edtShowTimeTableNum = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtShowTimeTableNum.setReadOnly(True)
        self.edtShowTimeTableNum.setObjectName("edtShowTimeTableNum")
        self.gridLayout_3.addWidget(self.edtShowTimeTableNum, 5, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_hint_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_hint_3.setText("")
        self.label_hint_3.setObjectName("label_hint_3")
        self.horizontalLayout_4.addWidget(self.label_hint_3)
        self.btnReadTimeTable = QtWidgets.QPushButton(self.groupBox_3)
        self.btnReadTimeTable.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnReadTimeTable.setObjectName("btnReadTimeTable")
        self.horizontalLayout_4.addWidget(self.btnReadTimeTable)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 5, 2, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_37 = QtWidgets.QLabel(self.groupBox_8)
        self.label_37.setObjectName("label_37")
        self.gridLayout_8.addWidget(self.label_37, 0, 0, 1, 1)
        self.edtShowPinterval = QtWidgets.QLineEdit(self.groupBox_8)
        self.edtShowPinterval.setReadOnly(True)
        self.edtShowPinterval.setObjectName("edtShowPinterval")
        self.gridLayout_8.addWidget(self.edtShowPinterval, 0, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox_8)
        self.label_38.setObjectName("label_38")
        self.gridLayout_8.addWidget(self.label_38, 0, 2, 1, 1)
        self.edtShowFinterval = QtWidgets.QLineEdit(self.groupBox_8)
        self.edtShowFinterval.setText("")
        self.edtShowFinterval.setReadOnly(True)
        self.edtShowFinterval.setObjectName("edtShowFinterval")
        self.gridLayout_8.addWidget(self.edtShowFinterval, 0, 3, 1, 1)
        self.btnReadInterval = QtWidgets.QPushButton(self.groupBox_8)
        self.btnReadInterval.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnReadInterval.setObjectName("btnReadInterval")
        self.gridLayout_8.addWidget(self.btnReadInterval, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_39 = QtWidgets.QLabel(self.groupBox_9)
        self.label_39.setObjectName("label_39")
        self.gridLayout_9.addWidget(self.label_39, 0, 0, 1, 1)
        self.edtShowLogicTemp1 = QtWidgets.QLineEdit(self.groupBox_9)
        self.edtShowLogicTemp1.setReadOnly(True)
        self.edtShowLogicTemp1.setObjectName("edtShowLogicTemp1")
        self.gridLayout_9.addWidget(self.edtShowLogicTemp1, 0, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.groupBox_9)
        self.label_40.setObjectName("label_40")
        self.gridLayout_9.addWidget(self.label_40, 0, 2, 1, 1)
        self.edtShowLogicTemp2 = QtWidgets.QLineEdit(self.groupBox_9)
        self.edtShowLogicTemp2.setReadOnly(True)
        self.edtShowLogicTemp2.setObjectName("edtShowLogicTemp2")
        self.gridLayout_9.addWidget(self.edtShowLogicTemp2, 0, 3, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.groupBox_9)
        self.label_41.setObjectName("label_41")
        self.gridLayout_9.addWidget(self.label_41, 1, 0, 1, 1)
        self.edtShowLogicTemp = QtWidgets.QLineEdit(self.groupBox_9)
        self.edtShowLogicTemp.setReadOnly(True)
        self.edtShowLogicTemp.setObjectName("edtShowLogicTemp")
        self.gridLayout_9.addWidget(self.edtShowLogicTemp, 1, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_hint_6 = QtWidgets.QLabel(self.groupBox_9)
        self.label_hint_6.setText("")
        self.label_hint_6.setObjectName("label_hint_6")
        self.horizontalLayout_7.addWidget(self.label_hint_6)
        self.btnReadLogicTemp = QtWidgets.QPushButton(self.groupBox_9)
        self.btnReadLogicTemp.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnReadLogicTemp.setObjectName("btnReadLogicTemp")
        self.horizontalLayout_7.addWidget(self.btnReadLogicTemp)
        self.gridLayout_9.addLayout(self.horizontalLayout_7, 1, 2, 1, 2)
        self.verticalLayout.addWidget(self.groupBox_9)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_31 = QtWidgets.QLabel(self.groupBox_6)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 0, 0, 1, 1)
        self.edtShowChangeModleNum = QtWidgets.QLineEdit(self.groupBox_6)
        self.edtShowChangeModleNum.setReadOnly(True)
        self.edtShowChangeModleNum.setObjectName("edtShowChangeModleNum")
        self.gridLayout_6.addWidget(self.edtShowChangeModleNum, 0, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_6)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 0, 2, 1, 1)
        self.edtShowChangeModleValue = QtWidgets.QLineEdit(self.groupBox_6)
        self.edtShowChangeModleValue.setText("")
        self.edtShowChangeModleValue.setReadOnly(True)
        self.edtShowChangeModleValue.setObjectName("edtShowChangeModleValue")
        self.gridLayout_6.addWidget(self.edtShowChangeModleValue, 0, 3, 1, 1)
        self.btnReadChangeModle = QtWidgets.QPushButton(self.groupBox_6)
        self.btnReadChangeModle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnReadChangeModle.setObjectName("btnReadChangeModle")
        self.gridLayout_6.addWidget(self.btnReadChangeModle, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_6)
        self.gridLayout_48.addLayout(self.verticalLayout, 0, 0, 4, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.edtShowAlarmPress1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtShowAlarmPress1.setReadOnly(True)
        self.edtShowAlarmPress1.setObjectName("edtShowAlarmPress1")
        self.gridLayout_2.addWidget(self.edtShowAlarmPress1, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.edtShowAlarmPress2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtShowAlarmPress2.setReadOnly(True)
        self.edtShowAlarmPress2.setObjectName("edtShowAlarmPress2")
        self.gridLayout_2.addWidget(self.edtShowAlarmPress2, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.edtShowAlarmFlow1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtShowAlarmFlow1.setReadOnly(True)
        self.edtShowAlarmFlow1.setObjectName("edtShowAlarmFlow1")
        self.gridLayout_2.addWidget(self.edtShowAlarmFlow1, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 2, 1, 1)
        self.edtShowAlarmFlow2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtShowAlarmFlow2.setReadOnly(True)
        self.edtShowAlarmFlow2.setObjectName("edtShowAlarmFlow2")
        self.gridLayout_2.addWidget(self.edtShowAlarmFlow2, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)
        self.edtShowAlarmTemp = QtWidgets.QLineEdit(self.groupBox_2)
        self.edtShowAlarmTemp.setReadOnly(True)
        self.edtShowAlarmTemp.setObjectName("edtShowAlarmTemp")
        self.gridLayout_2.addWidget(self.edtShowAlarmTemp, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_hint_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_hint_2.setText("")
        self.label_hint_2.setObjectName("label_hint_2")
        self.horizontalLayout_3.addWidget(self.label_hint_2)
        self.btnReadAlarm = QtWidgets.QPushButton(self.groupBox_2)
        self.btnReadAlarm.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnReadAlarm.setObjectName("btnReadAlarm")
        self.horizontalLayout_3.addWidget(self.btnReadAlarm)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 2, 1, 2)
        self.gridLayout_48.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_24 = QtWidgets.QLabel(self.groupBox_5)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 0, 0, 1, 1)
        self.edtShowSolarTemp1 = QtWidgets.QLineEdit(self.groupBox_5)
        self.edtShowSolarTemp1.setReadOnly(True)
        self.edtShowSolarTemp1.setObjectName("edtShowSolarTemp1")
        self.gridLayout_5.addWidget(self.edtShowSolarTemp1, 0, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_5)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 0, 2, 1, 1)
        self.edtShowSolarTemp2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.edtShowSolarTemp2.setReadOnly(True)
        self.edtShowSolarTemp2.setObjectName("edtShowSolarTemp2")
        self.gridLayout_5.addWidget(self.edtShowSolarTemp2, 0, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_5)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 1, 0, 1, 1)
        self.edtShowSolarTemp3 = QtWidgets.QLineEdit(self.groupBox_5)
        self.edtShowSolarTemp3.setReadOnly(True)
        self.edtShowSolarTemp3.setObjectName("edtShowSolarTemp3")
        self.gridLayout_5.addWidget(self.edtShowSolarTemp3, 1, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_5)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 1, 2, 1, 1)
        self.edtShowSolarTemp4 = QtWidgets.QLineEdit(self.groupBox_5)
        self.edtShowSolarTemp4.setReadOnly(True)
        self.edtShowSolarTemp4.setObjectName("edtShowSolarTemp4")
        self.gridLayout_5.addWidget(self.edtShowSolarTemp4, 1, 3, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_5)
        self.label_28.setObjectName("label_28")
        self.gridLayout_5.addWidget(self.label_28, 2, 0, 1, 1)
        self.edtShowJudgeTemp1 = QtWidgets.QLineEdit(self.groupBox_5)
        self.edtShowJudgeTemp1.setReadOnly(True)
        self.edtShowJudgeTemp1.setObjectName("edtShowJudgeTemp1")
        self.gridLayout_5.addWidget(self.edtShowJudgeTemp1, 2, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.groupBox_5)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 2, 2, 1, 1)
        self.edtShowJudgeTemp2 = QtWidgets.QLineEdit(self.groupBox_5)
        self.edtShowJudgeTemp2.setReadOnly(True)
        self.edtShowJudgeTemp2.setObjectName("edtShowJudgeTemp2")
        self.gridLayout_5.addWidget(self.edtShowJudgeTemp2, 2, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_5)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 3, 0, 1, 1)
        self.edtShowJudgeTemp3 = QtWidgets.QLineEdit(self.groupBox_5)
        self.edtShowJudgeTemp3.setReadOnly(True)
        self.edtShowJudgeTemp3.setObjectName("edtShowJudgeTemp3")
        self.gridLayout_5.addWidget(self.edtShowJudgeTemp3, 3, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_hint_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_hint_4.setText("")
        self.label_hint_4.setObjectName("label_hint_4")
        self.horizontalLayout_5.addWidget(self.label_hint_4)
        self.btnReadJudgeTemp = QtWidgets.QPushButton(self.groupBox_5)
        self.btnReadJudgeTemp.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnReadJudgeTemp.setObjectName("btnReadJudgeTemp")
        self.horizontalLayout_5.addWidget(self.btnReadJudgeTemp)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 3, 2, 1, 2)
        self.gridLayout_48.addWidget(self.groupBox_5, 1, 1, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_33 = QtWidgets.QLabel(self.groupBox_7)
        self.label_33.setObjectName("label_33")
        self.gridLayout_7.addWidget(self.label_33, 0, 0, 1, 1)
        self.edtShowOtherSolar = QtWidgets.QLineEdit(self.groupBox_7)
        self.edtShowOtherSolar.setReadOnly(True)
        self.edtShowOtherSolar.setObjectName("edtShowOtherSolar")
        self.gridLayout_7.addWidget(self.edtShowOtherSolar, 0, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox_7)
        self.label_34.setObjectName("label_34")
        self.gridLayout_7.addWidget(self.label_34, 0, 2, 1, 1)
        self.edtShowOtherWaterOut = QtWidgets.QLineEdit(self.groupBox_7)
        self.edtShowOtherWaterOut.setReadOnly(True)
        self.edtShowOtherWaterOut.setObjectName("edtShowOtherWaterOut")
        self.gridLayout_7.addWidget(self.edtShowOtherWaterOut, 0, 3, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_7)
        self.label_35.setObjectName("label_35")
        self.gridLayout_7.addWidget(self.label_35, 1, 0, 1, 1)
        self.edtShowOtherTemp = QtWidgets.QLineEdit(self.groupBox_7)
        self.edtShowOtherTemp.setReadOnly(True)
        self.edtShowOtherTemp.setObjectName("edtShowOtherTemp")
        self.gridLayout_7.addWidget(self.edtShowOtherTemp, 1, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_7)
        self.label_36.setObjectName("label_36")
        self.gridLayout_7.addWidget(self.label_36, 1, 2, 1, 1)
        self.edtShowOtherWaterIn = QtWidgets.QLineEdit(self.groupBox_7)
        self.edtShowOtherWaterIn.setReadOnly(True)
        self.edtShowOtherWaterIn.setObjectName("edtShowOtherWaterIn")
        self.gridLayout_7.addWidget(self.edtShowOtherWaterIn, 1, 3, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_hint_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_hint_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_hint_5.setText("")
        self.label_hint_5.setObjectName("label_hint_5")
        self.horizontalLayout_6.addWidget(self.label_hint_5)
        self.btnReadOtherValue = QtWidgets.QPushButton(self.groupBox_7)
        self.btnReadOtherValue.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btnReadOtherValue.setObjectName("btnReadOtherValue")
        self.horizontalLayout_6.addWidget(self.btnReadOtherValue)
        self.gridLayout_7.addLayout(self.horizontalLayout_6, 2, 0, 1, 4)
        self.gridLayout_48.addWidget(self.groupBox_7, 2, 1, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_42 = QtWidgets.QLabel(self.groupBox_10)
        self.label_42.setObjectName("label_42")
        self.gridLayout_10.addWidget(self.label_42, 0, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_10)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_10.addWidget(self.timeEdit, 0, 1, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.groupBox_10)
        self.label_43.setObjectName("label_43")
        self.gridLayout_10.addWidget(self.label_43, 0, 2, 1, 1)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.groupBox_10)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.gridLayout_10.addWidget(self.timeEdit_2, 0, 3, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_10)
        self.radioButton_5.setCheckable(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_8.addWidget(self.radioButton_5)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_10)
        self.radioButton_2.setCheckable(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_8.addWidget(self.radioButton_2)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_12.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_8.addWidget(self.pushButton_12)
        self.gridLayout_10.addLayout(self.horizontalLayout_8, 1, 0, 1, 4)
        self.gridLayout_11.addWidget(self.groupBox_10, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnReadOtherTime = QtWidgets.QPushButton(self.groupBox_4)
        self.btnReadOtherTime.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnReadOtherTime.setObjectName("btnReadOtherTime")
        self.gridLayout_4.addWidget(self.btnReadOtherTime, 0, 0, 1, 1)
        self.lineEdit_153 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_153.setReadOnly(True)
        self.lineEdit_153.setObjectName("lineEdit_153")
        self.gridLayout_4.addWidget(self.lineEdit_153, 0, 1, 1, 1)
        self.btnReadCleanElc = QtWidgets.QPushButton(self.groupBox_4)
        self.btnReadCleanElc.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnReadCleanElc.setObjectName("btnReadCleanElc")
        self.gridLayout_4.addWidget(self.btnReadCleanElc, 1, 0, 1, 1)
        self.lineEdit_154 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_154.setReadOnly(True)
        self.lineEdit_154.setObjectName("lineEdit_154")
        self.gridLayout_4.addWidget(self.lineEdit_154, 1, 1, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.gridLayout_48.addLayout(self.gridLayout_11, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(mainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(mainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(mainWindow)
        self.action_3.setObjectName("action_3")
        self.action_DTU = QtWidgets.QAction(mainWindow)
        self.action_DTU.setObjectName("action_DTU")
        self.action_DTU_2 = QtWidgets.QAction(mainWindow)
        self.action_DTU_2.setObjectName("action_DTU_2")
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action)
        self.menu_3.addAction(self.action_DTU)
        self.menu_3.addAction(self.action_DTU_2)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "江苏星云物联科技有限公司"))
        self.label_87.setText(_translate("mainWindow", "DTU地址："))
        self.label_88.setText(_translate("mainWindow", "  设备地址："))
        self.label_89.setText(_translate("mainWindow", "    串口："))
        self.comboBox.setItemText(0, _translate("mainWindow", "COM2"))
        self.comboBox.setItemText(1, _translate("mainWindow", "COM3"))
        self.comboBox.setItemText(2, _translate("mainWindow", "COM4"))
        self.label.setText(_translate("mainWindow", "MQTT服务器："))
        self.label_86.setText(_translate("mainWindow", "   端口："))
        self.btnMqttConnect.setText(_translate("mainWindow", "连 接"))
        self.groupBox_12.setTitle(_translate("mainWindow", "系统状态"))
        self.label_49.setText(_translate("mainWindow", "开关机："))
        self.comBootStatus.setItemText(0, _translate("mainWindow", "关机"))
        self.comBootStatus.setItemText(1, _translate("mainWindow", "开机"))
        self.label_50.setText(_translate("mainWindow", "工作模式："))
        self.comWorkMode.setItemText(0, _translate("mainWindow", "预留"))
        self.comWorkMode.setItemText(1, _translate("mainWindow", "太阳能供暖并储能"))
        self.comWorkMode.setItemText(2, _translate("mainWindow", "太阳能供暖不储能"))
        self.comWorkMode.setItemText(3, _translate("mainWindow", "设备放热供暖"))
        self.comWorkMode.setItemText(4, _translate("mainWindow", "设备放热供暖-低温"))
        self.comWorkMode.setItemText(5, _translate("mainWindow", "锅炉供暖不储能"))
        self.comWorkMode.setItemText(6, _translate("mainWindow", "锅炉供暖不储能-低温"))
        self.comWorkMode.setItemText(7, _translate("mainWindow", "板换打开"))
        self.comWorkMode.setItemText(8, _translate("mainWindow", "调试"))
        self.comWorkMode.setItemText(9, _translate("mainWindow", "自动模式下太阳能供暖并储能"))
        self.comWorkMode.setItemText(10, _translate("mainWindow", "自动模式下太阳能供暖不储能"))
        self.comWorkMode.setItemText(11, _translate("mainWindow", "自动模式下设备放热供暖"))
        self.comWorkMode.setItemText(12, _translate("mainWindow", "自动模式下设备放热供暖-低温"))
        self.comWorkMode.setItemText(13, _translate("mainWindow", "自动模式下 锅炉供暖不储能"))
        self.comWorkMode.setItemText(14, _translate("mainWindow", "自动模式下锅炉供暖不储能-低温"))
        self.comWorkMode.setItemText(15, _translate("mainWindow", "自动模式下板换打开"))
        self.comWorkMode.setItemText(16, _translate("mainWindow", "自动模式下打开太阳能"))
        self.label_51.setText(_translate("mainWindow", "夜晚供暖："))
        self.comSupplyHeat.setItemText(0, _translate("mainWindow", "关闭"))
        self.comSupplyHeat.setItemText(1, _translate("mainWindow", "打开"))
        self.label_52.setText(_translate("mainWindow", "白天模式："))
        self.comDayMode.setItemText(0, _translate("mainWindow", "关闭"))
        self.comDayMode.setItemText(1, _translate("mainWindow", "打开"))
        self.label_53.setText(_translate("mainWindow", "MinRefT:"))
        self.label_54.setText(_translate("mainWindow", "MaxRefT:"))
        self.btnSetSysStatus.setText(_translate("mainWindow", "设置"))
        self.groupBox_13.setTitle(_translate("mainWindow", "时段相关设置"))
        self.label_55.setText(_translate("mainWindow", "时 段 表1 ："))
        self.label_56.setText(_translate("mainWindow", "时 段 表2 ："))
        self.label_57.setText(_translate("mainWindow", "时 段 表3 ："))
        self.label_58.setText(_translate("mainWindow", "时 段 表4 ："))
        self.label_59.setText(_translate("mainWindow", "时 段 表5 ："))
        self.label_60.setText(_translate("mainWindow", "时 段 表6 ："))
        self.label_61.setText(_translate("mainWindow", "时 段 表7 ："))
        self.label_62.setText(_translate("mainWindow", "时 段 表8 ："))
        self.label_63.setText(_translate("mainWindow", "时 段 表9 ："))
        self.label_64.setText(_translate("mainWindow", "时 段 表10："))
        self.label_65.setText(_translate("mainWindow", "时段表数量："))
        self.comTimeTableNum.setItemText(0, _translate("mainWindow", "1"))
        self.comTimeTableNum.setItemText(1, _translate("mainWindow", "2"))
        self.comTimeTableNum.setItemText(2, _translate("mainWindow", "3"))
        self.comTimeTableNum.setItemText(3, _translate("mainWindow", "4"))
        self.comTimeTableNum.setItemText(4, _translate("mainWindow", "5"))
        self.comTimeTableNum.setItemText(5, _translate("mainWindow", "6"))
        self.comTimeTableNum.setItemText(6, _translate("mainWindow", "7"))
        self.comTimeTableNum.setItemText(7, _translate("mainWindow", "8"))
        self.comTimeTableNum.setItemText(8, _translate("mainWindow", "9"))
        self.comTimeTableNum.setItemText(9, _translate("mainWindow", "10"))
        self.btnSetTimeTable.setText(_translate("mainWindow", "设置"))
        self.groupBox_14.setTitle(_translate("mainWindow", "阀门调节间隔设定"))
        self.label_66.setText(_translate("mainWindow", "P 阀调节时间："))
        self.label_67.setText(_translate("mainWindow", "F 阀调节时间："))
        self.btnSetInterval.setText(_translate("mainWindow", "设置"))
        self.groupBox_15.setTitle(_translate("mainWindow", "阀门逻辑设定温度"))
        self.label_68.setText(_translate("mainWindow", "末端温差设置温度1："))
        self.label_69.setText(_translate("mainWindow", "末端温差设置温度2："))
        self.label_70.setText(_translate("mainWindow", "电锅炉设定温度："))
        self.btnSetLogicTemp.setText(_translate("mainWindow", "设置"))
        self.groupBox_16.setTitle(_translate("mainWindow", "变形模组偏移值设定"))
        self.label_71.setText(_translate("mainWindow", "相变模组编号（1-80）："))
        self.label_72.setText(_translate("mainWindow", "偏移值："))
        self.btnSetChangeModle.setText(_translate("mainWindow", "设置"))
        self.groupBox_11.setTitle(_translate("mainWindow", "报警值阙值"))
        self.label_44.setText(_translate("mainWindow", "进水管温度报警值："))
        self.label_45.setText(_translate("mainWindow", "进水管压力报警值："))
        self.label_46.setText(_translate("mainWindow", "出水管压力报警值："))
        self.label_47.setText(_translate("mainWindow", "进水管流量报警值："))
        self.label_48.setText(_translate("mainWindow", "出水管流量报警值："))
        self.btnSetAlarm.setText(_translate("mainWindow", "设置"))
        self.groupBox_19.setTitle(_translate("mainWindow", "逻辑控制用设定温度"))
        self.label_75.setText(_translate("mainWindow", "太阳能出水设定温度1："))
        self.label_76.setText(_translate("mainWindow", "太阳能出水设定温度2："))
        self.label_77.setText(_translate("mainWindow", "太阳能出水设定温度3："))
        self.label_78.setText(_translate("mainWindow", "太阳能出水设定温度4："))
        self.label_79.setText(_translate("mainWindow", "末端回水温度低温判断1："))
        self.label_80.setText(_translate("mainWindow", "末端回水温度低温判断2："))
        self.label_81.setText(_translate("mainWindow", "末端回水温度低温判断3："))
        self.btnSetJudgeTemp.setText(_translate("mainWindow", "设置"))
        self.groupBox_20.setTitle(_translate("mainWindow", "其他偏移值设定"))
        self.label_82.setText(_translate("mainWindow", "太阳能温度偏移值："))
        self.label_83.setText(_translate("mainWindow", "末端回水偏移值："))
        self.label_84.setText(_translate("mainWindow", "室外温度偏移值："))
        self.label_85.setText(_translate("mainWindow", "末端进水偏移值："))
        self.btnSetOtherValue.setText(_translate("mainWindow", "设置"))
        self.groupBox_17.setTitle(_translate("mainWindow", "工作时间设定"))
        self.label_73.setText(_translate("mainWindow", "下班时间："))
        self.label_74.setText(_translate("mainWindow", "上班时间："))
        self.rdoWorkday.setText(_translate("mainWindow", "正常上班"))
        self.rdoWeekday.setText(_translate("mainWindow", "放假状态"))
        self.btnSetWorkTime.setText(_translate("mainWindow", "设置"))
        self.groupBox_18.setTitle(_translate("mainWindow", "其他"))
        self.btnSetOtherTime.setText(_translate("mainWindow", "时间设置"))
        self.btnSetCleanElc.setText(_translate("mainWindow", "费率电量清零"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "                                设 置 界 面                                 "))
        self.groupBox.setTitle(_translate("mainWindow", "系统状态"))
        self.label_2.setText(_translate("mainWindow", "开关机："))
        self.label_3.setText(_translate("mainWindow", "工作模式："))
        self.label_4.setText(_translate("mainWindow", "夜晚供暖："))
        self.label_5.setText(_translate("mainWindow", "白天模式："))
        self.label_6.setText(_translate("mainWindow", "MinRefT:"))
        self.label_7.setText(_translate("mainWindow", "MaxRefT:"))
        self.btnReadSysStatus.setText(_translate("mainWindow", "读取"))
        self.groupBox_3.setTitle(_translate("mainWindow", "时段相关设置"))
        self.label_13.setText(_translate("mainWindow", "时 段 表1 ："))
        self.label_14.setText(_translate("mainWindow", "时 段 表2 ："))
        self.label_15.setText(_translate("mainWindow", "时 段 表3 ："))
        self.label_16.setText(_translate("mainWindow", "时 段 表4 ："))
        self.label_17.setText(_translate("mainWindow", "时 段 表5 ："))
        self.label_18.setText(_translate("mainWindow", "时 段 表6 ："))
        self.label_19.setText(_translate("mainWindow", "时 段 表7 ："))
        self.label_20.setText(_translate("mainWindow", "时 段 表8 ："))
        self.label_21.setText(_translate("mainWindow", "时 段 表9 ："))
        self.label_22.setText(_translate("mainWindow", "时 段 表10："))
        self.label_23.setText(_translate("mainWindow", "时段表数量："))
        self.btnReadTimeTable.setText(_translate("mainWindow", "读取"))
        self.groupBox_8.setTitle(_translate("mainWindow", "阀门调节间隔设定"))
        self.label_37.setText(_translate("mainWindow", "P 阀调节时间："))
        self.label_38.setText(_translate("mainWindow", "F 阀调节时间："))
        self.btnReadInterval.setText(_translate("mainWindow", "读取"))
        self.groupBox_9.setTitle(_translate("mainWindow", "阀门逻辑设定温度"))
        self.label_39.setText(_translate("mainWindow", "末端温差设置温度1："))
        self.label_40.setText(_translate("mainWindow", "末端温差设置温度2："))
        self.label_41.setText(_translate("mainWindow", "电锅炉设定温度："))
        self.btnReadLogicTemp.setText(_translate("mainWindow", "读取"))
        self.groupBox_6.setTitle(_translate("mainWindow", "变形模组偏移值设定"))
        self.label_31.setText(_translate("mainWindow", "相变模组编号（1-80）："))
        self.label_32.setText(_translate("mainWindow", "偏移值："))
        self.btnReadChangeModle.setText(_translate("mainWindow", "读取"))
        self.groupBox_2.setTitle(_translate("mainWindow", "报警值阙值"))
        self.label_8.setText(_translate("mainWindow", "进水管温度报警值："))
        self.label_9.setText(_translate("mainWindow", "进水管压力报警值："))
        self.label_10.setText(_translate("mainWindow", "出水管压力报警值："))
        self.label_11.setText(_translate("mainWindow", "进水管流量报警值："))
        self.label_12.setText(_translate("mainWindow", "出水管流量报警值："))
        self.btnReadAlarm.setText(_translate("mainWindow", "读取"))
        self.groupBox_5.setTitle(_translate("mainWindow", "逻辑控制用设定温度"))
        self.label_24.setText(_translate("mainWindow", "太阳能出水设定温度1："))
        self.label_25.setText(_translate("mainWindow", "太阳能出水设定温度2："))
        self.label_26.setText(_translate("mainWindow", "太阳能出水设定温度3："))
        self.label_27.setText(_translate("mainWindow", "太阳能出水设定温度4："))
        self.label_28.setText(_translate("mainWindow", "末端回水温度低温判断1："))
        self.label_29.setText(_translate("mainWindow", "末端回水温度低温判断2："))
        self.label_30.setText(_translate("mainWindow", "末端回水温度低温判断3："))
        self.btnReadJudgeTemp.setText(_translate("mainWindow", "读取"))
        self.groupBox_7.setTitle(_translate("mainWindow", "其他偏移值设定"))
        self.label_33.setText(_translate("mainWindow", "太阳能温度偏移值："))
        self.label_34.setText(_translate("mainWindow", "末端回水偏移值："))
        self.label_35.setText(_translate("mainWindow", "室外温度偏移值："))
        self.label_36.setText(_translate("mainWindow", "末端进水偏移值："))
        self.btnReadOtherValue.setText(_translate("mainWindow", "读取"))
        self.groupBox_10.setTitle(_translate("mainWindow", "工作时间设定"))
        self.label_42.setText(_translate("mainWindow", "上班时间："))
        self.label_43.setText(_translate("mainWindow", "下班时间："))
        self.radioButton_5.setText(_translate("mainWindow", "正常上班"))
        self.radioButton_2.setText(_translate("mainWindow", "放假状态"))
        self.pushButton_12.setText(_translate("mainWindow", "读取"))
        self.groupBox_4.setTitle(_translate("mainWindow", "其他"))
        self.btnReadOtherTime.setText(_translate("mainWindow", "时间读取："))
        self.btnReadCleanElc.setText(_translate("mainWindow", "费率电量："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "                                读 取 界 面                                 "))
        self.menu.setTitle(_translate("mainWindow", "关于"))
        self.menu_2.setTitle(_translate("mainWindow", "文件"))
        self.menu_3.setTitle(_translate("mainWindow", "帮助"))
        self.action.setText(_translate("mainWindow", "退出"))
        self.action_2.setText(_translate("mainWindow", "软件信息"))
        self.action_3.setText(_translate("mainWindow", "导入服务器"))
        self.action_DTU.setText(_translate("mainWindow", "激活DTU"))
        self.action_DTU_2.setText(_translate("mainWindow", "去活DTU"))

