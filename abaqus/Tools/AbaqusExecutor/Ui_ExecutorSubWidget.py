# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExecutorSubWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExecutorSubWidget(object):
    def setupUi(self, ExecutorSubWidget):
        ExecutorSubWidget.setObjectName("ExecutorSubWidget")
        ExecutorSubWidget.resize(1398, 650)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ExecutorSubWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dockWidget = QtWidgets.QDockWidget(ExecutorSubWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(250, 0))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 257, 630))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 24, 0, 1, 1)
        self.browseCwd = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseCwd.sizePolicy().hasHeightForWidth())
        self.browseCwd.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.browseCwd.setPalette(palette)
        self.browseCwd.setObjectName("browseCwd")
        self.gridLayout.addWidget(self.browseCwd, 0, 2, 1, 1)
        self.browseOdb = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseOdb.sizePolicy().hasHeightForWidth())
        self.browseOdb.setSizePolicy(sizePolicy)
        self.browseOdb.setObjectName("browseOdb")
        self.gridLayout.addWidget(self.browseOdb, 19, 2, 1, 1)
        self.cwd = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cwd.sizePolicy().hasHeightForWidth())
        self.cwd.setSizePolicy(sizePolicy)
        self.cwd.setMaximumSize(QtCore.QSize(16777215, 60))
        self.cwd.setReadOnly(True)
        self.cwd.setObjectName("cwd")
        self.gridLayout.addWidget(self.cwd, 2, 0, 1, 3)
        self.xlabel = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.xlabel.setObjectName("xlabel")
        self.gridLayout.addWidget(self.xlabel, 28, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 25, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 1, 0, 1, 3)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 10))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 21, 0, 1, 3)
        self.addY = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addY.sizePolicy().hasHeightForWidth())
        self.addY.setSizePolicy(sizePolicy)
        self.addY.setObjectName("addY")
        self.gridLayout.addWidget(self.addY, 26, 2, 1, 1)
        self.browseModelScript = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseModelScript.sizePolicy().hasHeightForWidth())
        self.browseModelScript.setSizePolicy(sizePolicy)
        self.browseModelScript.setObjectName("browseModelScript")
        self.gridLayout.addWidget(self.browseModelScript, 7, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 29, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 13, 0, 1, 1)
        self.ylabel = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.ylabel.setObjectName("ylabel")
        self.gridLayout.addWidget(self.ylabel, 29, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 31, 0, 1, 3)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 30, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)
        self.y = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.y.setObjectName("y")
        self.gridLayout.addWidget(self.y, 26, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 16, 0, 1, 2)
        self.outputScript = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.outputScript.setReadOnly(True)
        self.outputScript.setObjectName("outputScript")
        self.gridLayout.addWidget(self.outputScript, 20, 1, 1, 1)
        self.data = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.data.setReadOnly(True)
        self.data.setObjectName("data")
        self.gridLayout.addWidget(self.data, 24, 1, 1, 1)
        self.ys = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.ys.setObjectName("ys")
        self.gridLayout.addWidget(self.ys, 27, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 28, 0, 1, 1)
        self.input = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.input.setReadOnly(True)
        self.input.setObjectName("input")
        self.gridLayout.addWidget(self.input, 13, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 23, 0, 1, 3)
        self.browseOutputScript = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseOutputScript.sizePolicy().hasHeightForWidth())
        self.browseOutputScript.setSizePolicy(sizePolicy)
        self.browseOutputScript.setObjectName("browseOutputScript")
        self.gridLayout.addWidget(self.browseOutputScript, 20, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 26, 0, 1, 1)
        self.browseData = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseData.sizePolicy().hasHeightForWidth())
        self.browseData.setSizePolicy(sizePolicy)
        self.browseData.setObjectName("browseData")
        self.gridLayout.addWidget(self.browseData, 24, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 20, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_13.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 22, 0, 1, 2)
        self.modelScript = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.modelScript.setReadOnly(True)
        self.modelScript.setObjectName("modelScript")
        self.gridLayout.addWidget(self.modelScript, 7, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 18, 0, 1, 3)
        self.title = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 30, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_16.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 2)
        self.browseUser = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseUser.sizePolicy().hasHeightForWidth())
        self.browseUser.setSizePolicy(sizePolicy)
        self.browseUser.setObjectName("browseUser")
        self.gridLayout.addWidget(self.browseUser, 14, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 14, 0, 1, 1)
        self.x = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.x.setObjectName("x")
        self.gridLayout.addWidget(self.x, 25, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 10))
        self.widget_3.setObjectName("widget_3")
        self.gridLayout.addWidget(self.widget_3, 8, 0, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 19, 0, 1, 1)
        self.odb = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.odb.setReadOnly(True)
        self.odb.setObjectName("odb")
        self.gridLayout.addWidget(self.odb, 19, 1, 1, 1)
        self.user = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.user.setReadOnly(True)
        self.user.setObjectName("user")
        self.gridLayout.addWidget(self.user, 14, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setMinimumSize(QtCore.QSize(0, 10))
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 15, 0, 1, 3)
        self.browseInput = QtWidgets.QToolButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseInput.sizePolicy().hasHeightForWidth())
        self.browseInput.setSizePolicy(sizePolicy)
        self.browseInput.setObjectName("browseInput")
        self.gridLayout.addWidget(self.browseInput, 13, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 3)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 12, 0, 1, 3)
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 10))
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 3, 0, 1, 3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dockWidget)
        self.tabWidget = QtWidgets.QTabWidget(ExecutorSubWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.terminal = QtWidgets.QWidget()
        self.terminal.setObjectName("terminal")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.terminal)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.cmd = PlainTextEditor(self.terminal)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.cmd.setFont(font)
        self.cmd.setReadOnly(True)
        self.cmd.setObjectName("cmd")
        self.verticalLayout_4.addWidget(self.cmd)
        self.tabWidget.addTab(self.terminal, "")
        self.status = QtWidgets.QWidget()
        self.status.setObjectName("status")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.status)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sta = PlainTextEditor(self.status)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.sta.setFont(font)
        self.sta.setReadOnly(True)
        self.sta.setObjectName("sta")
        self.verticalLayout_5.addWidget(self.sta)
        self.tabWidget.addTab(self.status, "")
        self.message = QtWidgets.QWidget()
        self.message.setObjectName("message")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.message)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.msg = PlainTextEditor(self.message)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.msg.setFont(font)
        self.msg.setReadOnly(True)
        self.msg.setObjectName("msg")
        self.verticalLayout_6.addWidget(self.msg)
        self.tabWidget.addTab(self.message, "")
        self.figure = QtWidgets.QWidget()
        self.figure.setObjectName("figure")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.figure)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fig = MatplotlibWidget(self.figure)
        self.fig.setObjectName("fig")
        self.verticalLayout_2.addWidget(self.fig)
        self.tabWidget.addTab(self.figure, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(ExecutorSubWidget)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(ExecutorSubWidget)

    def retranslateUi(self, ExecutorSubWidget):
        _translate = QtCore.QCoreApplication.translate
        ExecutorSubWidget.setWindowTitle(_translate("ExecutorSubWidget", "Form"))
        self.dockWidget.setWindowTitle(_translate("ExecutorSubWidget", "Settings"))
        self.label_3.setText(_translate("ExecutorSubWidget", "Data"))
        self.browseCwd.setText(_translate("ExecutorSubWidget", "Browse"))
        self.browseOdb.setText(_translate("ExecutorSubWidget", "Browse"))
        self.label_5.setText(_translate("ExecutorSubWidget", "X"))
        self.addY.setText(_translate("ExecutorSubWidget", "Add"))
        self.browseModelScript.setText(_translate("ExecutorSubWidget", "Browse"))
        self.label_2.setText(_translate("ExecutorSubWidget", "Script"))
        self.label_14.setText(_translate("ExecutorSubWidget", "YLabel"))
        self.label_4.setText(_translate("ExecutorSubWidget", "Input"))
        self.label_6.setText(_translate("ExecutorSubWidget", "Execution"))
        self.label_15.setText(_translate("ExecutorSubWidget", "Title"))
        self.label.setText(_translate("ExecutorSubWidget", "Modeling"))
        self.label_10.setText(_translate("ExecutorSubWidget", "Extract Output Data"))
        self.label_12.setText(_translate("ExecutorSubWidget", "XLabel"))
        self.browseOutputScript.setText(_translate("ExecutorSubWidget", "Browse"))
        self.label_9.setText(_translate("ExecutorSubWidget", "Y"))
        self.browseData.setText(_translate("ExecutorSubWidget", "Browse"))
        self.label_11.setText(_translate("ExecutorSubWidget", "Script"))
        self.label_13.setText(_translate("ExecutorSubWidget", "Draw Figures"))
        self.label_16.setText(_translate("ExecutorSubWidget", "Work Directory"))
        self.browseUser.setText(_translate("ExecutorSubWidget", "Browse"))
        self.label_8.setText(_translate("ExecutorSubWidget", "User"))
        self.label_7.setText(_translate("ExecutorSubWidget", "Odb"))
        self.browseInput.setText(_translate("ExecutorSubWidget", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.terminal), _translate("ExecutorSubWidget", "Terminal"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.status), _translate("ExecutorSubWidget", "Status File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.message), _translate("ExecutorSubWidget", "Message File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.figure), _translate("ExecutorSubWidget", "Figure"))
from ..Widgets import MatplotlibWidget, PlainTextEditor
