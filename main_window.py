# Файл с интерфейсом главного окна

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# ? Верхняя панель
btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Отдохнуть")
rest_spinbox = QSpinBox()
rest_spinbox.setValue(30)
lbl_minutes = QLabel(" минут")

top_panel_layout = QHBoxLayout()
top_panel_layout.addWidget(btn_menu)
top_panel_layout.addWidget(btn_rest)
top_panel_layout.addWidget(rest_spinbox)
top_panel_layout.addWidget(lbl_minutes)

# ? Виджет с вопросом
lbl_question = QLabel("ВОПРОС")

# ? Секция с вариантами ответа
answers_section = QGroupBox("Варианты ответов")
answers_layout = QVBoxLayout()
answer_buttons_group = QButtonGroup()

rbtn_ans1 = QRadioButton("Ответ 1")
rbtn_ans2 = QRadioButton("Ответ 2")
rbtn_ans3 = QRadioButton("Ответ 3")
rbtn_ans4 = QRadioButton("Ответ 4")

answer_buttons_group.addButton(rbtn_ans1)
answer_buttons_group.addButton(rbtn_ans2)
answer_buttons_group.addButton(rbtn_ans3)
answer_buttons_group.addButton(rbtn_ans4)

column1, column2 = QVBoxLayout(), QVBoxLayout()
answer_buttons_layout = QHBoxLayout()

column1.addWidget(rbtn_ans1)
column1.addWidget(rbtn_ans2)

column2.addWidget(rbtn_ans3)
column2.addWidget(rbtn_ans4)

answer_buttons_layout.addLayout(column1)
answer_buttons_layout.addLayout(column2)

answers_layout.addLayout(answer_buttons_layout)

answers_section.setLayout(answers_layout)

# ? Секция с результатами
result_section = QGroupBox("Результаты теста")
result_layout = QVBoxLayout()

lbl_result = QLabel("РЕЗУЛЬТАТ")
lbl_rightAnswer = QLabel("ПРАВИЛЬНЫЙ ОТВЕТ")

result_layout.addWidget(lbl_result)
result_layout.addWidget(lbl_rightAnswer)

result_section.setLayout(result_layout)

# ? Виджет кнопки ответа
answer_button = QPushButton("Ответить")

# ! Объединение всех частей интерфейса
main_window_layout = QVBoxLayout()

main_window_layout.addLayout(top_panel_layout)
main_window_layout.addWidget(lbl_question)
main_window_layout.addWidget(answers_section)
main_window_layout.addWidget(result_section)
main_window_layout.addWidget(answer_button)

