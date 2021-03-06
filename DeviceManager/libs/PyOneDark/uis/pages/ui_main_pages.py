# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesJNRoHB.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

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
        self.pages.setLayoutDirection(Qt.LeftToRight)
        self.page_light = QWidget()
        self.page_light.setObjectName(u"page_light")
        self.page_light.setStyleSheet(u"")
        self.page_light_layout = QVBoxLayout(self.page_light)
        self.page_light_layout.setSpacing(5)
        self.page_light_layout.setObjectName(u"page_light_layout")
        self.page_light_layout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.page_light)
        self.page_temperature = QWidget()
        self.page_temperature.setObjectName(u"page_temperature")
        self.page_temperature.setStyleSheet(u"")
        self.page_temperature_layout = QVBoxLayout(self.page_temperature)
        self.page_temperature_layout.setSpacing(5)
        self.page_temperature_layout.setObjectName(u"page_temperature_layout")
        self.page_temperature_layout.setContentsMargins(0, 0, 0, 0)
        self.pages.addWidget(self.page_temperature)
        self.page_fluid = QWidget()
        self.page_fluid.setObjectName(u"page_fluid")
        self.page_fluid.setStyleSheet(u"")
        self.page_fluid_layout = QVBoxLayout(self.page_fluid)
        self.page_fluid_layout.setObjectName(u"page_fluid_layout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.InkLayout = QVBoxLayout()
        self.InkLayout.setObjectName(u"InkLayout")
        self.label = QLabel(self.page_fluid)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.InkLayout.addWidget(self.label)

        self.ink_toggle = QCheckBox(self.page_fluid)
        self.ink_toggle.setObjectName(u"ink_toggle")
        self.ink_toggle.setLayoutDirection(Qt.RightToLeft)
        self.ink_toggle.setChecked(True)

        self.InkLayout.addWidget(self.ink_toggle)

        self.label_4 = QLabel(self.page_fluid)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.InkLayout.addWidget(self.label_4)

        self.ink_color = QComboBox(self.page_fluid)
        self.ink_color.addItem("")
        self.ink_color.addItem("")
        self.ink_color.addItem("")
        self.ink_color.addItem("")
        self.ink_color.addItem("")
        self.ink_color.addItem("")
        self.ink_color.addItem("")
        self.ink_color.addItem("")
        self.ink_color.setObjectName(u"ink_color")

        self.InkLayout.addWidget(self.ink_color)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.InkLayout.addItem(self.verticalSpacer)

        self.resetInkButton = QPushButton(self.page_fluid)
        self.resetInkButton.setObjectName(u"resetInkButton")

        self.InkLayout.addWidget(self.resetInkButton)


        self.horizontalLayout.addLayout(self.InkLayout)

        self.line_sep_fluid_0 = QFrame(self.page_fluid)
        self.line_sep_fluid_0.setObjectName(u"line_sep_fluid_0")
        self.line_sep_fluid_0.setFrameShape(QFrame.VLine)
        self.line_sep_fluid_0.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_sep_fluid_0)

        self.FlowLayout = QVBoxLayout()
        self.FlowLayout.setObjectName(u"FlowLayout")
        self.label_2 = QLabel(self.page_fluid)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.FlowLayout.addWidget(self.label_2)

        self.flow_toggle = QCheckBox(self.page_fluid)
        self.flow_toggle.setObjectName(u"flow_toggle")
        self.flow_toggle.setLayoutDirection(Qt.RightToLeft)
        self.flow_toggle.setChecked(True)

        self.FlowLayout.addWidget(self.flow_toggle)

        self.label_7 = QLabel(self.page_fluid)
        self.label_7.setObjectName(u"label_7")

        self.FlowLayout.addWidget(self.label_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.flow_slider = QSlider(self.page_fluid)
        self.flow_slider.setObjectName(u"flow_slider")
        self.flow_slider.setMinimum(-10)
        self.flow_slider.setMaximum(150)
        self.flow_slider.setSingleStep(5)
        self.flow_slider.setPageStep(10)
        self.flow_slider.setOrientation(Qt.Vertical)
        self.flow_slider.setInvertedAppearance(False)
        self.flow_slider.setInvertedControls(False)
        self.flow_slider.setTickPosition(QSlider.TicksAbove)
        self.flow_slider.setTickInterval(10)

        self.horizontalLayout_2.addWidget(self.flow_slider)

        self.label_5 = QLabel(self.page_fluid)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_flow_value = QLabel(self.page_fluid)
        self.label_flow_value.setObjectName(u"label_flow_value")

        self.horizontalLayout_2.addWidget(self.label_flow_value)


        self.FlowLayout.addLayout(self.horizontalLayout_2)

        self.label_8 = QLabel(self.page_fluid)
        self.label_8.setObjectName(u"label_8")

        self.FlowLayout.addWidget(self.label_8)

        self.resetFlowButton = QPushButton(self.page_fluid)
        self.resetFlowButton.setObjectName(u"resetFlowButton")

        self.FlowLayout.addWidget(self.resetFlowButton)


        self.horizontalLayout.addLayout(self.FlowLayout)

        self.line = QFrame(self.page_fluid)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.SubstanceLayout = QVBoxLayout()
        self.SubstanceLayout.setObjectName(u"SubstanceLayout")
        self.label_3 = QLabel(self.page_fluid)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.SubstanceLayout.addWidget(self.label_3)

        self.substance_toggle = QCheckBox(self.page_fluid)
        self.substance_toggle.setObjectName(u"substance_toggle")
        self.substance_toggle.setLayoutDirection(Qt.RightToLeft)
        self.substance_toggle.setChecked(True)

        self.SubstanceLayout.addWidget(self.substance_toggle)

        self.label_9 = QLabel(self.page_fluid)
        self.label_9.setObjectName(u"label_9")

        self.SubstanceLayout.addWidget(self.label_9)

        self.substance_combo = QComboBox(self.page_fluid)
        self.substance_combo.addItem("")
        self.substance_combo.addItem("")
        self.substance_combo.addItem("")
        self.substance_combo.addItem("")
        self.substance_combo.setObjectName(u"substance_combo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.substance_combo.sizePolicy().hasHeightForWidth())
        self.substance_combo.setSizePolicy(sizePolicy)

        self.SubstanceLayout.addWidget(self.substance_combo)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.SubstanceLayout.addItem(self.verticalSpacer_2)

        self.resetSubstanceButton = QPushButton(self.page_fluid)
        self.resetSubstanceButton.setObjectName(u"resetSubstanceButton")

        self.SubstanceLayout.addWidget(self.resetSubstanceButton)


        self.horizontalLayout.addLayout(self.SubstanceLayout)


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
        self.ink_toggle.setText(QCoreApplication.translate("MainPages", u"Enabled", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Choose a color:", None))
        self.ink_color.setItemText(0, "")
        self.ink_color.setItemText(1, QCoreApplication.translate("MainPages", u"cyan", None))
        self.ink_color.setItemText(2, QCoreApplication.translate("MainPages", u"yellow", None))
        self.ink_color.setItemText(3, QCoreApplication.translate("MainPages", u"magenta", None))
        self.ink_color.setItemText(4, QCoreApplication.translate("MainPages", u"black", None))
        self.ink_color.setItemText(5, QCoreApplication.translate("MainPages", u"red", None))
        self.ink_color.setItemText(6, QCoreApplication.translate("MainPages", u"blue", None))
        self.ink_color.setItemText(7, QCoreApplication.translate("MainPages", u"green", None))

        self.resetInkButton.setText(QCoreApplication.translate("MainPages", u"Set to random", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Flow", None))
        self.flow_toggle.setText(QCoreApplication.translate("MainPages", u"Enabled", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"150", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"Flow in ml/s:", None))
        self.label_flow_value.setText(QCoreApplication.translate("MainPages", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"-10", None))
        self.resetFlowButton.setText(QCoreApplication.translate("MainPages", u"Set to random", None))
        self.label_3.setText(QCoreApplication.translate("MainPages", u"Substance", None))
        self.substance_toggle.setText(QCoreApplication.translate("MainPages", u"Enabled", None))
        self.label_9.setText(QCoreApplication.translate("MainPages", u"Choose a substance type:", None))
        self.substance_combo.setItemText(0, "")
        self.substance_combo.setItemText(1, QCoreApplication.translate("MainPages", u"water", None))
        self.substance_combo.setItemText(2, QCoreApplication.translate("MainPages", u"alcohol", None))
        self.substance_combo.setItemText(3, QCoreApplication.translate("MainPages", u"oil", None))

        self.resetSubstanceButton.setText(QCoreApplication.translate("MainPages", u"Set to random", None))
    # retranslateUi

