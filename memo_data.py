# Файл с классами программы

from random import randint, shuffle, choice

# ! ШАБЛОН ПРОЕКТИРОВАНИЯ MVC

# ? Класс, хранящий информацию про каждый вопрос (модель вопроса)
class Question:
    def __init__(self, question, answer, wrong1, wrong2, wrong3):
        self.question = question
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

# ? Он отвечает за все элементы интерфейса, которые меняются во время ответов на вопросы
class QuestionView:
    # ? Сохраняем модель вопроса (объект класса Question) и все виджеты, в которых надо отобразить информацию из вопроса
    def __init__(self, question_model, question_widget, answer_widget, wrong1_widget, wrong2_widget, wrong3_widget, result_widget, reult_answer_widget):
        self.question_model = question_model
        self.question_widget = question_widget
        
        self.answer_buttons = [answer_widget, wrong1_widget, wrong2_widget, wrong3_widget]

        self.result_widget = result_widget
        self.result_answer_widget = reult_answer_widget
    # ? Отображает в сохраненных ранее виджетах программы информацию из модели вопроса
    def show(self):
        self.question_widget.setText(self.question_model.question)
        
        shuffle(self.answer_buttons)
        
        self.answer_buttons[0].setText(self.question_model.answer)
        self.answer_buttons[1].setText(self.question_model.wrong1)
        self.answer_buttons[2].setText(self.question_model.wrong2)
        self.answer_buttons[3].setText(self.question_model.wrong3)
        
    # ? Изменить модель вопроса
    def change_model(self, question_model):
        self.question_model = question_model

# ? Класс, занимающийся работой с вопросами, их переключением, дает команды в ViewModel
class QuestionController:
    def __init__(self, viewmodel):
        
        self.questions = []
        self.viewmodel = viewmodel
        
    def show_random_question(self):
        new_question = choice(self.questions) # 1. случайній вопрос из списка
        self.viewmodel.change_model(new_question) # 2. информацию о вопросы отослать в ViewModel (виджеты)
        
        self.viewmodel.show() # 3. ViewModel отображает информацию о вопросе на виджетах
        
    def add_questions(self, questions):
        for question in questions:
            self.questions.append(question)
        
        