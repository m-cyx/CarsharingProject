import tkinter as tk
from sys import exit as exx
from table import Table
from add_user import Add_user
class Menu: #класс, инициализирующий окно меню и содержащий методы взаимодействия с ним
        def __init__(self, controller, master, delay):
                self.__number = 0
                self.__controller = controller
                self.__master = master
                self.deiconify(delay)
                self.__master.focus_force()
                self.__master.geometry('290x165')
                self.__master.configure(background = 'black')
                self.__master.overrideredirect(1)
                x = (root.winfo_screenwidth() - 290) / 2
                y = (root.winfo_screenheight() - 165) / 2
                self.__master.wm_geometry("+%d+%d" % (x, y))
                self.__data_display_label = tk.Label(self.__master, text = 'Отобразить данные о клиентах', width = 30, fg = 'blue', bg = 'black', font = 'Calibri 12')
                self.__data_display_label.place(x = 10, y = 10)
                self.__add_user_label = tk.Label(self.__master, text = 'Добавить клиента', width = 19, fg = 'blue', bg = 'black', font = 'Calibri 12')
                self.__add_user_label.place(x = 10, y = 50)
                self.__delete_user_label = tk.Label(self.__master, text = 'Удалить данные о клиенте', width = 26, fg = 'blue', bg = 'black', font = 'Calibri 12')
                self.__delete_user_label.place(x = 10, y = 90)
                self.__editing_user_data_label = tk.Label(self.__master, text = 'Редактировать данные о клиенте', width = 32, fg = 'blue', bg = 'black', font = 'Calibri 12')
                self.__editing_user_data_label.place(x = 10, y = 130)
                self.__data_display_label.bind('<Button-1>',controller.get_records) #нажатие левой кнопки мыши
                self.__add_user_label.bind('<Button-1>', controller.show_add_user_window)
                self.__delete_user_label.bind('<Button-1>', controller.delete_user)
                self.__editing_user_data_label.bind('<Button-1>', controller.editing_user)
                self.__add_user_label.bind('<Enter>', self.__add_user_label_enter)
                self.__data_display_label.bind('<Enter>', lambda ev: self.__data_display_label_enter(ev = ev)) #наведение курсором
                self.__delete_user_label.bind('<Enter>', self.__delete_user_label_enter)
                self.__editing_user_data_label.bind('<Enter>', self.__editing_user_data_label_enter)
                self.__add_user_label.bind('<Leave>', self.__add_user_label_leave)
                self.__data_display_label.bind('<Leave>', self.__data_display_label_leave) #покидание курсором
                self.__delete_user_label.bind('<Leave>', self.__delete_user_label_leave)
                self.__editing_user_data_label.bind('<Leave>', self.__editing_user_data_label_leave)
                self.__data_display_label.bind('<Return>', controller.get_records) #нажатие левой кнопки мыши
                self.__add_user_label.bind('<Return>', controller.show_add_user_window)
                self.__delete_user_label.bind('<Return>', controller.delete_user)
                self.__editing_user_data_label.bind('<Return>', controller.editing_user)
                self.__master.bind('<KeyPress>', self.__keypress)
                self.__master.bind('<Motion>', self.__leave_all_lab)
                self.__master.bind('<Escape>', self.__bind_menu_exit)


        def focus_force(self): #метод, устанавливающий фокус и отодвигающий окно меню на передний план
                self.__master.lift()
                self.__master.attributes("-topmost", True)
                self.__master.focus_force()

        def deiconify(self, delay = False): #метод, отображающий окно меню через 2 секунды (заставка висит 2 секунды и появляется окно меню)
                if delay == True:
                        self.__master.after(2000, self.__master.deiconify)
                else:
                        self.__master.deiconify()
                
        def __bind_menu_exit(self, event): #метод, который уничтожает окно меню (срабатывает при нажатии клавиши ESCAPE) 
                self.__master.destroy()
                exx()
                
        def __data_display_label_enter(self, st = None, ev = None): #метод, изменяющий дизайн надписи ОТОБРАЗИТЬ ДАННЫЕ О КЛИЕНТАХ при наведении на неё курсором мыши
                if self.__number == 4:
                        self.__editing_user_data_label_leave()
                elif self.__number == 2:
                        self.__add_user_label_leave()
                self.__data_display_label.place_forget()
                self.__data_display_label.place(x = 8, y = 10)
                self.__data_display_label.config(fg = 'blue', bg = 'black', font = 'Calibri 14', width = 25, relief = 'ridge')
                self.__data_display_label.focus_force()
                if st != None:
                        self.__number = 1

        def create_users_table(self, rows): #метод, открывающий окно для отображения данных из базы данных при нажатии левой кнопкой мыши надписи ОТОБРАЗИТЬ ДАННЫЕ О КЛИЕНТЕ
                self.__master.withdraw()
                self.__data_display_label_leave()
                self.__number = 0
                wind = tk.Toplevel()
                display_data_window = Table(wind, self)
                display_data_window.insert_values(rows)
                display_data_window.focus_force()

        def __data_display_label_leave(self, event = None): #метод, изменяющий дизайн надписи ОТОБРАЗИТЬ ДАННЫЕ О КЛИЕНТАХ в исходное состояние при покидании надписи курсором мыши
                self.__data_display_label.place_forget()
                self.__data_display_label.place(x = 10, y = 10)
                self.__data_display_label.config(fg = 'blue', bg = 'black', font = 'Calibri 12', width = 30, relief = 'flat')
        
        def __add_user_label_enter(self, st = None, ev = None): #метод, изменяющий дизайн надписи ДОБАВИТЬ КЛИЕНТА при наведении на неё курсором мыши
                if st == 'Up':
                        self.__delete_user_label_leave()
                        self.__number -= 1
                elif st == 'Down':
                        self.__data_display_label_leave()
                        self.__number += 1
                self.__add_user_label.place_forget()
                self.__add_user_label.place(x = 6, y = 50)
                self.__add_user_label.config(fg = 'blue', bg = 'black', font = 'Calibri 14', width = 15, relief = 'ridge')
                self.__add_user_label.focus_force()

        def create_add_user_window(self): #метод, открывающий окно для добавления пользователя в базу данных при нажатии левой кнопкой мыши надписи ДОБАВИТЬ КЛИЕНТА
                self.__master.withdraw()
                self.__add_user_label_leave()
                self.__number = 0
                wind = tk.Toplevel()
                wind.configure(bd=0)
                add_user_window = Add_user(wind, self, self.__controller)
                add_user_window.focus_force()

        def __add_user_label_leave(self, event = None): #метод, изменяющий дизайн надписи ДОБАВИТЬ КЛИЕНТА в исходное состояние при покидании надписи курсором мыши
                self.__add_user_label.place_forget()
                self.__add_user_label.place(x = 10, y = 50)
                self.__add_user_label.config(fg = 'blue', bg = 'black', font = 'Calibri 12', width = 19, relief = 'flat')

        def __delete_user_label_enter(self, st = None, ev = None): #метод, изменяющий дизайн надписи УДАЛИТЬ ДАННЫЕ О КЛИЕНТЕ при наведении на неё курсором мыши
                if st == 'Up':
                        self.__editing_user_data_label_leave()
                        self.__number -= 1
                elif st == 'Down':
                        self.__add_user_label_leave()
                        self.__number += 1
                self.__delete_user_label.place_forget()
                self.__delete_user_label.place(x = 6, y = 90)
                self.__delete_user_label.config(fg = 'blue', bg = 'black', font = 'Calibri 14', width = 22, relief = 'ridge')

        def create_delete_user_window(self): #метод, открывающий окно для удаления данных о заданном пользователе в базе данных при нажатии левой кнопкой мыши надписи УДАЛИТЬ ДАННЫЕ О КЛИЕНТЕ
                self.__master.withdraw()
                self.__delete_user_label_leave()
                self.__number = 0
                wind = tk.Toplevel()
                wind.configure(bd = 0)
                delete_user_window = Delete_user(wind, self, self.__controller)
                delete_user_window.focus_force()

        def __delete_user_label_leave(self, event = None): #метод, изменяющий дизайн надписи УДАЛИТЬ ДАННЫЕ О КЛИЕНТЕ в исходное состояние при покидании надписи курсором мыши
                self.__delete_user_label.place_forget()
                self.__delete_user_label.place(x = 10, y = 90)
                self.__delete_user_label.config(fg = 'blue', bg = 'black', font = 'Calibri 12', width = 26, relief = 'flat')

        def __editing_user_data_label_enter(self, st = None, ev = None): #метод, изменяющий дизайн надписи РЕДАКТИРОВАТЬ ДАННЫЕ О КЛИЕНТЕ при наведении на неё курсором мыши
                if st == 'Up':
                        self.__data_display_label_leave()
                        self.__number = 4
                elif st == 'Down':
                        self.__delete_user_label_leave()
                        self.__number += 1
                self.__editing_user_data_label.place_forget()
                self.__editing_user_data_label.place(x = 6, y = 130)
                self.__editing_user_data_label.config(fg = 'blue', bg = 'black', font = 'Calibri 14', width = 27, relief = 'ridge')

        def create_editing_user_window(self): #метод, открывающий окно для редактирования данных о заданном пользователе в базе данных при нажатии левой кнопкой мыши надписи РЕДАКТИРОВАТЬ ДАННЫЕ О КЛИЕНТЕ
                self.__master.withdraw()
                self.__editing_user_data_label_leave()
                self.__number = 0
                wind = tk.Toplevel()
                wind.configure(bd = 0)
                editing_user_window = Editing_user(wind, self, self.__controller)
                editing_user_window.focus_force()

        def __editing_user_data_label_leave(self, event = None): #метод, изменяющий дизайн надписи РЕДАКТИРОВАТЬ ДАННЫЕ О КЛИЕНТЕ в исходное состояние при покидании надписи курсором мыши
                self.__editing_user_data_label.place_forget()
                self.__editing_user_data_label.place(x = 10, y = 130)
                self.__editing_user_data_label.config(fg = 'blue', bg = 'black', font = 'Calibri 12', width = 32, relief = 'flat')

        def __keypress(self, e): #метод, изменяющий дизайн надписей по нажатию  клавиш Up или Down
                key = e.keysym
                self.__master.bind('<Motion>', self.__leave_all_lab)
                if (key == 'Up' or key == 'Down') and self.__number == 0:
                        #self.__leave_all_lab()
                        self.__data_display_label_enter(st = key)
                        return
                if key == 'Up' and self.__number == 1:
                        self.__editing_user_data_label_enter(st = key)
                        return
                if key == 'Down' and self.__number == 1:
                        self.__add_user_label_enter(st = key)
                        return
                if key == 'Up' and self.__number == 2:
                        self.__data_display_label_enter(st = key)
                        return
                if key == 'Down' and self.__number == 2:
                        self.__delete_user_label_enter(st = key)
                        return
                if key == 'Up' and self.__number == 3:
                        self.__add_user_label_enter(st = key)
                        return
                if key == 'Down' and self.__number == 3:
                        self.__editing_user_data_label_enter(st = key)
                        return
                if key == 'Up' and self.__number == 4:
                        self.__delete_user_label_enter(st = key)
                        pass
                if key == 'Down' and self.__number == 4:
                        self.__data_display_label_enter(st = key)
                        return
                        
        def __leave_all_lab(self, event = None): #метод, возвращающий все надписи в исходное состояние при движении курсора мыши
                        self.__data_display_label_leave()
                        self.__add_user_label_leave()
                        self.__delete_user_label_leave()
                        self.__editing_user_data_label_leave()
                        self.__master.unbind('<Motion>')
                        self.__number = 0
