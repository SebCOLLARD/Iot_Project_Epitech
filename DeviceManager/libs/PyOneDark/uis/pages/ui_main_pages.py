# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesGMRTIy.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from ...qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
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
        self.page_fluid.setStyleSheet(u"; background: lightblue;")
        self.page_fluid_layout = QVBoxLayout(self.page_fluid)
        self.page_fluid_layout.setObjectName(u"page_fluid_layout")
        self.pages.addWidget(self.page_fluid)

        self.main_pages_layout.addWidget(self.pages)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainPages)

    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))

    # retranslateUi
