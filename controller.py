from Model.models import Model
from menu import Menu
from intro import Intro
from table import Table
from add_user import Add_user
import tkinter as tk

class Controller: #класс-контроллер, в котором реализованы методы проверки корректности заполненных данных и отправки 'сообщений' определённых задач View или Model
    def __init__(self, root):
        self.__menu = Menu(self, root, True)
        self.__model = Model()

    def get_users_table(self): #метод, отправляющий 'сообщение' Model, чтобы тот отправил информацию из базы данных классу-контроллеру
        return self.__model.get_all_tuples()

    def get_records(self, event): #метод, отправляющий 'сообщение' View, чтобы тот вывел информацию о пользователях на экран
        self.__menu.create_users_table(self.get_users_table())

    def show_add_user_window(self, event): #метод, который отображает окно для занесения данных
        self.__menu.create_add_user_window()

    def new_record(self, ev, add_user_window):
        self.__model.add_record(add_user_window.return_data_list())


if __name__ == '__main__':
    carsharing = Controller()
    carsharing.mainloop()
    