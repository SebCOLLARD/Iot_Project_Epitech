# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
# import sys
# import os

# from ....widgets.py_table_widget.py_table_widget import PyTableWidget

from .functions_main_window import *

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from ....qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from ....core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from ....core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from ....widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from .ui_main import *

# MAIN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from .functions_main_window import *

from ......config import (
    LIGHT_DASHBOARD_URL,
    TEMPERATURE_DASHBOARD_URL,
    # FLUIDS_DASHBOARD_URL,
)

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_light.svg",
            "btn_id": "btn_light",
            "btn_text": "Light sensors",
            "btn_tooltip": "Light sensors",
            "show_top": True,
            "is_active": True,
        },
        {
            "btn_icon": "icon_temperature.svg",
            "btn_id": "btn_temperature",
            "btn_text": "Temperature sensors",
            "btn_tooltip": "Temperature sensors",
            "show_top": True,
            "is_active": False,
        },
        {
            "btn_icon": "icon_fluid.svg",
            "btn_id": "btn_fluid",
            "btn_text": "Fluid sensors",
            "btn_tooltip": "Fluid sensors",
            "show_top": True,
            "is_active": False,
        },
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon": "icon_search.svg",
            "btn_id": "btn_search",
            "btn_tooltip": "Search",
            "is_active": False,
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_top_settings",
            "btn_tooltip": "Top settings",
            "is_active": False,
        },
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        # self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # REMOVE MARGINS IN TEMP & LIGHT PAGES
        # self.ui.load_pages.page_temperature_layout.setContentsMargins(0, 0, 0, 0)
        # self.ui.load_pages.page_light_layout.setContentsMargins(0, 0, 0, 0)

        # ADD WEBVIEWS MANUALLY BECAUSE DESIGNER CRASHES...
        # ////////////////////////////////////////////////////////////////
        self.dashboard_light = QWebEngineView()
        self.dashboard_light.load(LIGHT_DASHBOARD_URL)
        self.dashboard_light.setFixedSize(1600, 900)
        self.ui.load_pages.page_light_layout.addChildWidget(self.dashboard_light)

        self.dashboard_temperature = QWebEngineView()
        self.dashboard_temperature.load(TEMPERATURE_DASHBOARD_URL)
        self.dashboard_temperature.setFixedSize(1600, 900)
        self.ui.load_pages.page_temperature_layout.addChildWidget(
            self.dashboard_temperature
        )

        # self.dashboard_fluid = QWebEngineView()
        # self.dashboard_fluid.load(FLUIDS_DASHBOARD_URL)
        # self.dashboard_fluid.setFixedSize(1600, 900)
        # self.ui.load_pages.fluid_dashboard_frame.addChildWidget(self.dashboard_fluid)

        # CONNECT FLOW SLIDER TO VALUE TEXT
        def slider_updated():
            self.ui.load_pages.label_flow_value.setText(
                str(self.ui.load_pages.flow_slider.value())
            )

        self.ui.load_pages.flow_slider.valueChanged.connect(slider_updated)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_light)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg"),
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(
                self.width() - 20, self.height() - 20, 15, 15
            )
