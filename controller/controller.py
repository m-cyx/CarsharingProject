import sys
import os
sys.path.append(os.path.join(r'C:\Users\User\Desktop\CARSHARING', r'C:\Users\User\Desktop\CARSHARING\view'))
sys.path.append(os.path.join(r'C:\Users\User\Desktop\CARSHARING', r'C:\Users\User\Desktop\CARSHARING\model'))
from menu import Menu
from models import Model

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

        def new_record(self, add_user_window):
                self.__send_view_mes_incor_ind_add_us(self.__model.add_record(add_user_window.return_data_list()), add_user_window)

        def __send_view_mes_incor_ind_add_us(self, val, add_user_window):
                add_user_window.get_incorrect_values(val)

        def show_delete_user_window(self, event):
                self.__menu.create_delete_user_window()

        def delete_record(self, delete_user_window):
                self.__send_view_mes_incor_id_del_us(self.__model.delete_record(delete_user_window.return_id_for_delete_record()), delete_user_window)

        def __send_view_mes_incor_id_del_us(self, mes, delete_user_window):
                delete_user_window.get_mes_incorrect_id(mes)

        def show_editing_user_window(self, event):
                self.__menu.create_editing_user_window()

        def editing_record(self, editing_user_window):
                ls = editing_user_window.return_data_list()
                self.__send_view_mes_incor_ind_edit_us(self.__model.change_record(ls[1:], ls[0]))

        def __send_view_mes_incor_ind_edit_us(self, val, editing_user_window):
                editing_user_window.get_incorrect_values(val)