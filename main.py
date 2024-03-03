# Главный запускающий файл

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from app import app
from main_window import *
from menu_window import *
from memo_data import *
from windows import *

main_window = QWidget()
main_window.resize(1000, 750)
main_window.setWindowTitle("Memory Card")
# ! Список стандартніх вопросов в программе
questions = [
    Question("Вопрос1", "Ответ", "Непр1", "Непр2", "Непр3"),
    Question("Вопрос2", "Ответ", "Непр1", "Непр2", "Непр3"),
    Question("Вопрос3", "Ответ", "Непр1", "Непр2", "Непр3"),
    Question("Вопрос4", "Ответ", "Непр1", "Непр2", "Непр3"),
    Question("Вопрос5", "Ответ", "Непр1", "Непр2", "Непр3"),
    Question("Вопрос6", "Ответ", "Непр1", "Непр2", "Непр3"),
    Question("Вопрос7", "Ответ", "Непр1", "Непр2", "Непр3")
]

# ! Создали ViewModel (храним информацию про нужные виджеты, модель вопроса пока что -1)
question_viewmodel = QuestionView(-1, lbl_question, rbtn_ans1, rbtn_ans2, rbtn_ans3, rbtn_ans4, lbl_result, lbl_rightAnswer)

# ! Создали Controller (хранит в себе созданную ViewModel и список вопросов), говорим отобразить случайный вопрос
question_controller = QuestionController(question_viewmodel)
question_controller.add_questions(questions)
question_controller.show_random_question()

def show_menu():
    menu_widget.show()
    main_widget.hide()
    
def show_main():
    menu_widget.hide()
    main_widget.show()

btn_menu.clicked.connect(show_menu)
btn_back_to_main.clicked.connect(show_main)

show_main()
main_window.setLayout(window_layout)
main_window.show()
app.exec()