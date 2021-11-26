# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesaQdTaY.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(814, 525)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_light = QWidget()
        self.page_light.setObjectName(u"page_light")
        self.page_light.setStyleSheet(u"font-size: 14pt; background: lightgreen;")
        self.page_light_layout = QVBoxLayout(self.page_light)
        self.page_light_layout.setSpacing(5)
        self.page_light_layout.setObjectName(u"page_light_layout")
        self.page_light_layout.setContentsMargins(5, 5, 5, 5)
        self.pages.addWidget(self.page_light)
        self.page_temperature = QWidget()
        self.page_temperature.setObjectName(u"page_temperature")
        self.page_temperature.setStyleSheet(u"; background: orange;")
        self.page_temperature_layout = QVBoxLayout(self.page_temperature)
        self.page_temperature_layout.setSpacing(5)
        self.page_temperature_layout.setObjectName(u"page_temperature_layout")
        self.page_temperature_layout.setContentsMargins(5, 5, 5, 5)
        self.pages.addWidget(self.page_temperature)
        self.page_fluid = QWidget()
        self.page_fluid.setObjectName(u"page_fluid")
        self.page_fluid.setStyleSheet(u"")
        self.page_fluid_layout = QVBoxLayout(self.page_fluid)
        self.page_fluid_layout.setObjectName(u"page_fluid_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.page_fluid)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.page_fluid)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout.addWidget(self.label_4)

        self.ink_color = QComboBox(self.page_fluid)
        self.ink_color.addItem("")
        self.ink_color.addItem("")
        self.ink_color.addItem("")
        self.ink_color.addItem("")
        self.ink_color.setObjectName(u"ink_color")

        self.verticalLayout.addWidget(self.ink_color)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.resetInkButton = QPushButton(self.page_fluid)
        self.resetInkButton.setObjectName(u"resetInkButton")

        self.verticalLayout.addWidget(self.resetInkButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line_sep_fluid_0 = QFrame(self.page_fluid)
        self.line_sep_fluid_0.setObjectName(u"line_sep_fluid_0")
        self.line_sep_fluid_0.setFrameShape(QFrame.VLine)
        self.line_sep_fluid_0.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_sep_fluid_0)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_fluid)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_7 = QLabel(self.page_fluid)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalSlider = QSlider(self.page_fluid)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMinimum(-200)
        self.verticalSlider.setMaximum(1500)
        self.verticalSlider.setSingleStep(10)
        self.verticalSlider.setPageStep(100)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(False)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setTickPosition(QSlider.TicksAbove)
        self.verticalSlider.setTickInterval(100)

        self.horizontalLayout_2.addWidget(self.verticalSlider)

        self.label_5 = QLabel(self.page_fluid)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_fluid)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_8 = QLabel(self.page_fluid)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.resetFlowButton = QPushButton(self.page_fluid)
        self.resetFlowButton.setObjectName(u"resetFlowButton")

        self.verticalLayout_2.addWidget(self.resetFlowButton)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.line = QFrame(self.page_fluid)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.page_fluid)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_9 = QLabel(self.page_fluid)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_3.addWidget(self.label_9)

        self.comboBox = QComboBox(self.page_fluid)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.resetSubstanceButton = QPushButton(self.page_fluid)
        self.resetSubstanceButton.setObjectName(u"resetSubstanceButton")

        self.verticalLayout_3.addWidget(self.resetSubstanceButton)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.page_fluid_layout.addLayout(self.horizontalLayout)

        self.pages.addWidget(self.page_fluid)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Ink", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Choose a color:", None))
        self.ink_color.setItemText(0, QCoreApplication.translate("MainPages", u"cyan", None))
        self.ink_color.setItemText(1, QCoreApplication.translate("MainPages", u"yellow", None))
        self.ink_color.setItemText(2, QCoreApplication.translate("MainPages", u"magenta", None))
        self.ink_color.setItemText(3, QCoreApplication.translate("MainPages", u"black", None))

        self.resetInkButton.setText(QCoreApplication.translate("MainPages", u"Set to random", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Flow", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"1500", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Flow in ml/s:", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"<value>", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"-200", None))
        self.resetFlowButton.setText(QCoreApplication.translate("MainPages", u"Set to random", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Substance", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"Choose a substance type:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainPages", u"water", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainPages", u"alcohol", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainPages", u"oil", None))

        self.resetSubstanceButton.setText(QCoreApplication.translate("MainPages", u"Set to random", None))
    # retranslateUi

