# Интерфейс меню

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# ? Главный лейаут окна
menu_window_layout = QVBoxLayout()

# ? Форма для ввода информации про новый вопрос
new_question_form = QFormLayout()

# ? 5 полей для ввода информации про новій вопрос
question_line = QLineEdit()
answer_line = QLineEdit()
wrong1_line = QLineEdit()
wrong2_line = QLineEdit()
wrong3_line = QLineEdit()

# ? Добавили в форму окна настроек наши поля с подписями
new_question_form.addRow("Введите вопрос:", question_line)
new_question_form.addRow("Введите ответ:", answer_line)
new_question_form.addRow("Введите неправильный ответ 1:", wrong1_line)
new_question_form.addRow("Введите неправильный ответ 2:", wrong2_line)
new_question_form.addRow("Введите неправильный ответ 3:", wrong3_line)

# ? Горизонтальный лейаут под кнопки "новый вопрос" и "очистить поля"
# ? Добавили эти кнопки в него
buttons_layout = QHBoxLayout()

btn_new_question = QPushButton("Создать вопрос")
btn_clear_inputs = QPushButton("Очистить поля")

buttons_layout.addWidget(btn_new_question)
buttons_layout.addWidget(btn_clear_inputs)

# ? Кнопка для возвращения в главное меню
btn_back_to_main = QPushButton("Назад")

# ? Объединили все в один лейаут
menu_window_layout.addLayout(new_question_form)
menu_window_layout.addLayout(buttons_layout)
menu_window_layout.addWidget(btn_back_to_main)
