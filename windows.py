# Файл, в котором мы создали единый лейаут (объединили меню и главную страницу)

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from menu_window import menu_window_layout
from main_window import main_window_layout

main_widget = QWidget()
main_widget.setLayout(main_window_layout)

menu_widget = QWidget()
menu_widget.setLayout(menu_window_layout)

window_layout = QVBoxLayout()
window_layout.addWidget(main_widget)
window_layout.addWidget(menu_widget)
