import tk as tk
import tk.ttk as ttk
from time import sleep as sp
from sys import exit as exx
from /home/dolph/Документы/GitHub/CarsharingProject/Carsharing/models import *
class Model:
        """
        Реализация методов класса Model по получению данных с бд, занесению данных в бд,
        удалению некоторой записи из бд и редактированию некоторой записи в бд
        """
        def __init__(self):
                """

                Инициализация базы данных.

                """
                self.x = 1
        def get_users_table(self):
                """

                Необходимо реализовать метод, который вернёт кортеж кортежей с данными из бд через запрос (sqlite3 в помощь)
        
                """
                return ((2, 3), (1,1))
    
class Intro: #класс, инициализирующий окно заставки и методы взаимодействия с ним
        def __init__(self, master):
                self.__master = master
                self.__master.geometry('235x130')
                x = (root.winfo_screenwidth() - 235) / 2
                y = (root.winfo_screenheight() - 130) / 2
                self.__master.wm_geometry("+%d+%d" % (x, y))
                self.__Label1 = tk.Label(self.__master, text='KaRDeli', fg = 'blue', bg = 'peru', font = 'Calibri 20')
                self.__Label1.place(x = 71, y = 30)
                self.__Label2 = tk.Label(self.__master, text = 'КарДели', fg = 'blue', bg = 'peru', font = 'Calibri 20')
                self.__Label2.place(x = 65, y = 65)
                self.__master.configure(background = 'peru')
                self.__master.overrideredirect(1)

        def withdraw(self): #метод, закрывающий окно заставки спустя 2 секунды
                self.__master.after(2000, self.__master.withdraw)
                
class Menu: #класс, инициализирующий окно меню и содержащий методы взаимодействия с ним
        def __init__(self, master):
                self.__number = 0
                self.__master = master
                self.__master.focus_force()
                self.__master.geometry('290x165')
                self.__master.configure(background = 'peru')
                self.__master.overrideredirect(1)
                x = (root.winfo_screenwidth() - 290) / 2
                y = (root.winfo_screenheight() - 165) / 2
                self.__master.wm_geometry("+%d+%d" % (x, y))
                self.__data_display_label = tk.Label(self.__master, text = 'Отобразить данные о клиентах', width = 30, fg = 'blue', bg = 'peru', font = 'Calibri 12')
                self.__data_display_label.place(x = 10, y = 10)
                self.__add_user_label = tk.Label(self.__master, text = 'Добавить клиента', width = 19, fg = 'blue', bg = 'peru', font = 'Calibri 12')
                self.__add_user_label.place(x = 10, y = 50)
                self.__delete_user_label = tk.Label(self.__master, text = 'Удалить данные о клиенте', width = 26, fg = 'blue', bg = 'peru', font = 'Calibri 12')
                self.__delete_user_label.place(x = 10, y = 90)
                self.__editing_user_data_label = tk.Label(self.__master, text = 'Редактировать данные о клиенте', width = 32, fg = 'blue', bg = 'peru', font = 'Calibri 12')
                self.__editing_user_data_label.place(x = 10, y = 130)

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
        
        def bind_menu_escape(self): #метод, осуществляющий доступ к окну меню для отлова события нажатия на ESCAPE
                self.__master.bind('<Escape>', self.__bind_menu_exit)
                
        def __data_display_label_enter(self, st = None, ev = None): #метод, изменяющий дизайн надписи ОТОБРАЗИТЬ ДАННЫЕ О КЛИЕНТАХ при наведении на неё курсором мыши
                if self.__number == 4:
                        self.editing_user_data_label_leave()
                elif self.__number == 2:
                        self.__add_user_label_leave()
                self.__data_display_label.place_forget()
                self.__data_display_label.place(x = 8, y = 10)
                self.__data_display_label.config(fg = 'blue', bg = 'peru', font = 'Calibri 14', width = 25, relief = 'ridge')
                self.__data_display_label.focus_force()
                if st != None:
                        self.__number = 1

        def __data_display_label_button1(self, ev, rows): #метод, открывающий окно для отображения данных из базы данных при нажатии левой кнопкой мыши надписи ОТОБРАЗИТЬ ДАННЫЕ О КЛИЕНТЕ
                self.__master.withdraw()
                self.__data_display_label_leave()
                self.__number = 0
                wind = tk.Tk()
                display_data_window = Table(wind)
                display_data_window.insert_values(rows)
                display_data_window.focus_force()
                display_data_window.bind_data_display_window(self)              

        def __data_display_label_leave(self, event = None): #метод, изменяющий дизайн надписи ОТОБРАЗИТЬ ДАННЫЕ О КЛИЕНТАХ в исходное состояние при покидании надписи курсором мыши
                self.__data_display_label.place_forget()
                self.__data_display_label.place(x = 10, y = 10)
                self.__data_display_label.config(fg = 'blue', bg = 'peru', font = 'Calibri 12', width = 30, relief = 'flat')

        def bind_data_display_label(self, st, rows = tuple()): #метод, осуществляющий доступ к надписи ОТОБРАЗИТЬ ДАННЫЕ О КЛИЕНТАХ для отлова разных событий
                if st == 'button1':
                        self.__data_display_label.bind('<Button-1>', lambda ev: self.__data_display_label_button1(ev, rows)) #нажатие левой кнопки мыши
                        pass
                if st == 'enter':
                        self.__data_display_label.bind('<Enter>', lambda ev: self.__data_display_label_enter(ev = ev)) #наведение курсором
                        pass
                if st == 'leave':
                        self.__data_display_label.bind('<Leave>', self.__data_display_label_leave) #покидание курсором
                        pass
                if st == 'return':
                        self.__data_display_label.bind('<Return>', lambda ev: self.__data_display_label_button1(ev, rows)) #нажатие левой кнопки мыши
                        pass
        
        def __add_user_label_enter(self, st = None, ev = None): #метод, изменяющий дизайн надписи ДОБАВИТЬ КЛИЕНТА при наведении на неё курсором мыши
                if st == 'Up':
                        self.delete_user_label_leave()
                        self.__number -= 1
                elif st == 'Down':
                        self.__data_display_label_leave()
                        self.__number += 1
                self.__add_user_label.place_forget()
                self.__add_user_label.place(x = 6, y = 50)
                self.__add_user_label.config(fg = 'blue', bg = 'peru', font = 'Calibri 14', width = 15, relief = 'ridge')
                self.__add_user_label.focus_force()

        def __add_user_label_button1(self, event): #метод, открывающий окно для добавления пользователя в базу данных при нажатии левой кнопкой мыши надписи ДОБАВИТЬ КЛИЕНТА
                self.__master.withdraw()
                self.__add_user_label_leave()
                self.__number = 0
                wind = tk.Tk()
                add_user_window = Add_user(wind)
                add_user_window.focus_force()
                add_user_window.bind_add_user(self)

        def __add_user_label_leave(self, event = None): #метод, изменяющий дизайн надписи ДОБАВИТЬ КЛИЕНТА в исходное состояние при покидании надписи курсором мыши
                self.__add_user_label.place_forget()
                self.__add_user_label.place(x = 10, y = 50)
                self.__add_user_label.config(fg = 'blue', bg = 'peru', font = 'Calibri 12', width = 19, relief = 'flat')

        def bind_add_user_label(self, st): #метод, осуществляющий доступ к надписи ДОБАВИТЬ КЛИЕНТА для отлова событий
                if st == 'button1':
                        self.__add_user_label.bind('<Button-1>', self.__add_user_label_button1)
                        pass
                if st == 'enter':
                        self.__add_user_label.bind('<Enter>', self.__add_user_label_enter)
                        pass
                if st == 'leave':
                        self.__add_user_label.bind('<Leave>', self.__add_user_label_leave)
                        pass
                if st == 'return':
                        self.__add_user_label.bind('<Return>', self.__add_user_label_button1)
                        pass

        def delete_user_label_enter(self, st = None, ev = None): #метод, изменяющий дизайн надписи УДАЛИТЬ ДАННЫЕ О КЛИЕНТЕ при наведении на неё курсором мыши
                if st == 'Up':
                        self.editing_user_data_label_leave()
                        self.__number -= 1
                elif st == 'Down':
                        self.__add_user_label_leave()
                        self.__number += 1
                self.__delete_user_label.place_forget()
                self.__delete_user_label.place(x = 6, y = 90)
                self.__delete_user_label.config(fg = 'blue', bg = 'peru', font = 'Calibri 14', width = 22, relief = 'ridge')

        def delete_user_label_button1(self, event): #метод, открывающий окно для удаления данных о заданном пользователе в базе данных при нажатии левой кнопкой мыши надписи УДАЛИТЬ ДАННЫЕ О КЛИЕНТЕ
                self.__master.withdraw()
                wind = tk.Tk()
                wind.withdraw()
                obj = Delete_user(wind)
                obj.deiconify()
                return obj

        def delete_user_label_leave(self, event = None): #метод, изменяющий дизайн надписи УДАЛИТЬ ДАННЫЕ О КЛИЕНТЕ в исходное состояние при покидании надписи курсором мыши
                self.__delete_user_label.place_forget()
                self.__delete_user_label.place(x = 10, y = 90)
                self.__delete_user_label.config(fg = 'blue', bg = 'peru', font = 'Calibri 12', width = 26, relief = 'flat')

        def bind_delete_user_label(self, st): #метод, осуществляющий доступ к надписи УДАЛИТЬ ДАННЫЕ О КЛИЕНТЕ для отлова событий
                if st == 'button1':
                        return self.__delete_user_label.bind('<Button-1>', self.delete_user_label_button1)
                        
                if st == 'enter':
                        self.__delete_user_label.bind('<Enter>', self.delete_user_label_enter)
                        pass
                
                if st == 'leave':
                        self.__delete_user_label.bind('<Leave>', self.delete_user_label_leave)
                        pass

        def editing_user_data_label_enter(self, st = None, ev = None): #метод, изменяющий дизайн надписи РЕДАКТИРОВАТЬ ДАННЫЕ О КЛИЕНТЕ при наведении на неё курсором мыши
                if st == 'Up':
                        self.__data_display_label_leave()
                        self.__number = 4
                elif st == 'Down':
                        self.delete_user_label_leave()
                        self.__number += 1
                self.__editing_user_data_label.place_forget()
                self.__editing_user_data_label.place(x = 6, y = 130)
                self.__editing_user_data_label.config(fg = 'blue', bg = 'peru', font = 'Calibri 14', width = 27, relief = 'ridge')

        def editing_user_data_label_button1(self, event): #метод, открывающий окно для редактирования данных о заданном пользователе в базе данных при нажатии левой кнопкой мыши надписи РЕДАКТИРОВАТЬ ДАННЫЕ О КЛИЕНТЕ
                self.__master.withdraw()
                wind = tk.Tk()
                wind.withdraw()
                obj = Editing_user_data(wind)
                obj.deiconify()
                return obj

        def editing_user_data_label_leave(self, event = None): #метод, изменяющий дизайн надписи РЕДАКТИРОВАТЬ ДАННЫЕ О КЛИЕНТЕ в исходное состояние при покидании надписи курсором мыши
                self.__editing_user_data_label.place_forget()
                self.__editing_user_data_label.place(x = 10, y = 130)
                self.__editing_user_data_label.config(fg = 'blue', bg = 'peru', font = 'Calibri 12', width = 32, relief = 'flat')

        def bind_editing_user_data_label(self, st): #метод, осуществляющий доступ к надписи РЕДАКТИРОВАТЬ ДАННЫЕ О КЛИЕНТЕ для отлова событий
                if st == 'button1':
                        return self.__editing_user_data_label.bind('<Button-1>', self.editing_user_data_label_button1)
                        
                if st == 'enter':
                        self.__editing_user_data_label.bind('<Enter>', self.editing_user_data_label_enter)
                        pass
                
                if st == 'leave':
                        self.__editing_user_data_label.bind('<Leave>', self.editing_user_data_label_leave)
                        pass

        def keypress(self, e): #метод, изменяющий дизайн надписей по нажатию  клавиш Up или Down
                key = e.keysym
                self.__master.bind('<Motion>', self.__leave_all_lab)
                if (key == 'Up' or key == 'Down') and self.__number == 0:
                        #self.__leave_all_lab()
                        self.__data_display_label_enter(st = key)
                        return
                if key == 'Up' and self.__number == 1:
                        self.editing_user_data_label_enter(st = key)
                        return
                if key == 'Down' and self.__number == 1:
                        self.__add_user_label_enter(st = key)
                        return
                if key == 'Up' and self.__number == 2:
                        self.__data_display_label_enter(st = key)
                        return
                if key == 'Down' and self.__number == 2:
                        self.delete_user_label_enter(st = key)
                        return
                if key == 'Up' and self.__number == 3:
                        self.__add_user_label_enter(st = key)
                        return
                if key == 'Down' and self.__number == 3:
                        self.editing_user_data_label_enter(st = key)
                        return
                if key == 'Up' and self.__number == 4:
                        self.delete_user_label_enter(st = key)
                        pass
                if key == 'Down' and self.__number == 4:
                        self.__data_display_label_enter(st = key)
                        return

        def __leave_all_lab(self, event = None): #метод, возвращающий все надписи в исходное состояние при движении курсора мыши
                        self.__data_display_label_leave()
                        self.__add_user_label_leave()
                        self.delete_user_label_leave()
                        self.editing_user_data_label_leave()
                        self.__master.unbind('<Motion>')
                        self.__number = 0

        def bind_up_down_buttons(self): #метод, предоставляющий доступ к окну меню для отлова событий нажатия клавиш клавиатуры
                self.__master.bind('<KeyPress>', self.keypress)
                self.__master.bind('<Motion>', self.__leave_all_lab)

class Data_display: #класс, инициализирующий окно отображения информации из базы данных и содержащий методы взаимодействия с ним
        def __init__(self, master):
                self.__master = master
                self.__master.geometry('800x200')
                self.__master.configure(background = 'peru')
                self.__master.overrideredirect(1)
                x = (root.winfo_screenwidth() - 800) / 2
                y = (root.winfo_screenheight() - 200) / 2
                self.__master.wm_geometry("+%d+%d" % (x, y))   

        def __data_display_window_escape(self, ev, window): #метод, закрывающий окно отображения информации из базы данных и открывающий окно меню
                self.__master.withdraw()
                self._Table__id = 0
                self._Table__iid = 0
                self._Table__tree.delete(*self._Table__tree.get_children())
                window.deiconify(delay = False)
                window.focus_force()
        
class Table(Data_display): #класс, наследованный от класса Data_display инициализирующий таблицу и методы взаимодействия с ней
        def __init__(self, master):
                Data_display.__init__(self, master)
                self.__tree = ttk.Treeview(master, columns = ('Name', 'ID'))
                self.__tree.heading('#0', text = 'Item')
                self.__tree.heading('#1', text = 'Name')
                self.__tree.heading('#2', text = 'Id')
                self.__tree.column('#0', stretch = tk.YES)
                self.__tree.column('#1', stretch = tk.YES)
                self.__tree.column('#2', stretch = tk.YES)
                self.__id = 0
                self.__iid = 0
                self.__scrolltable = tk.Scrollbar(self._Data_display__master, command = self.__tree.yview)
                self.__tree.configure(yscrollcommand = self.__scrolltable.set)
                self.__scrolltable.pack(side = tk.RIGHT, fill = tk.Y)
                self.__tree.pack(expand = tk.YES, fill = tk.BOTH)

        def bind_data_display_window(self, window): #метод, предоставляющий доступ к таблице для отлова события нажатия на ESCAPE
                self.__tree.bind('<Escape>', lambda ev: self._Data_display__data_display_window_escape(ev, window))

        def focus_force(self): #метод, устанавливающий фокус на окно таблицы
                self.__tree.lift()
                self.__tree.focus_force()
                
        def insert_values(self, rows): #метод, добавляющий данные в таблицу
                for row in rows:
                        self.__tree.insert('', tk.END, iid = self.__iid, text = str(self.__id), values = row)
                        self.__id += 1
                        self.__iid += 1
                
class Delete_user: #класс, инициализирующий окно для удаления данных о заданном пользователе из базы данных и методы взаимодействия с ним
        pass

class Editing_user_data: #класс, инициализирующий окно для редактирования данных о заданном пользователе из базы данных и методы взаимодействия с ним
        pass

class Add_user: #класс, инициализирующий окно для добавления пользователя в базу данных и методы взаимодействия с ним
        def __init__(self, master):
                self.__master = master
                self.__entry_name = tk.Entry(self.__master, fg = 'grey', bg = 'white')
                self.__entry_name.insert(0, 'Имя пользователя')
                self.__entry_surname = tk.Entry(self.__master, fg = 'grey', bg = 'white', text = 'Фамилия пользователя')
                self.__entry_surname.insert(0, 'Фамилия пользователя')
                self.__master.geometry('400x200')
                self.__master.configure(background = 'peru')
                self.__master.overrideredirect(1)
                x = (root.winfo_screenwidth() - 400) / 2
                y = (root.winfo_screenheight() - 200) / 2
                self.__master.wm_geometry("+%d+%d" % (x, y))
                self.__entry_name.place(x = 100, y = 100)
                self.__entry_surname.place(x = 100, y = 150)

        def foc_in(self, ev, ent): #метод, фокусирующий заданное поле ввода и скрывающий placeholder
                if ent['fg'] == 'grey':
                        ent.delete('0', 'end')
                        ent['fg'] = 'blue'

        def foc_out(self, ev, ent, string): #метод, проявляющий placeholder заданного поля ввода
                if not ent.get():
                        ent.insert(0, string)
                        ent['fg'] = 'grey'

        def bind_add_user(self, menu): #метод, предоставляющий доступ к полям ввода и окну для отлова событий нажатия на разные клавиши
                self.__entry_name.bind('<FocusIn>', lambda ev: self.foc_in(ev, self.__entry_name))
                self.__entry_name.bind('<FocusOut>', lambda ev: self.foc_out(ev, self.__entry_name, 'Имя пользователя'))
                self.__entry_surname.bind('<FocusIn>', lambda ev: self.foc_in(ev, self.__entry_surname))
                self.__entry_surname.bind('<FocusOut>', lambda ev: self.foc_out(ev, self.__entry_surname, 'Фамилия пользователя'))
                self.__master.bind('<Escape>', lambda ev: self.add_user_escape(ev, menu))

        def add_user_escape(self, ev, menu): #метод, скрывающий окно добавления пользователя после нажатия ESCAPE
                self.__master.withdraw()
                menu.deiconify(delay = False)
                menu.focus_force()


        def focus_force(self): #метод, устанавливающий фокус на окно ввода пользователя
                self.__master.focus_force()


class Controller: #класс-контроллер, в котором реализованы методы проверки корректности заполненных данных и отправки 'сообщений' определённых задач View или Model
        def __init__(self, root):
                self.__menu = Menu(root)
                self.__menu.deiconify(delay = True)
                self.__model = Model()
                self.show_users_table()
                self.add_user()
                self.__menu.bind_data_display_label('enter')
                self.__menu.bind_up_down_buttons()
                self.__menu.bind_menu_escape()
                self.__menu.bind_data_display_label('leave')
                self.__menu.bind_add_user_label('enter')
                self.__menu.bind_add_user_label('leave')
                self.__delete_user = self.__menu.bind_delete_user_label('button1')
                self.__menu.bind_delete_user_label('enter')
                self.__menu.bind_delete_user_label('leave')
                self.__editing_user_data = self.__menu.bind_editing_user_data_label('button1')
                self.__menu.bind_editing_user_data_label('enter')
                self.__menu.bind_editing_user_data_label('leave')
                
        def get_users_table(self): #метод, отправляющий 'сообщение' Model, чтобы тот отправил информацию из базы данных классу-контроллеру
                return self.__model.get_users_table()

        def show_users_table(self): #метод, отправляющий 'сообщение' View, чтобы тот вывел информацию о пользователях на экран
                self.__menu.bind_data_display_label('button1', self.get_users_table())
                self.__menu.bind_data_display_label('return', self.get_users_table())

        def add_user(self):
                self.__menu.bind_add_user_label('button1')
                self.__menu.bind_add_user_label('return')
                
if __name__ == '__main__': 
        root = tk.Tk()
        root.withdraw()
        intro = Intro(tk.Tk()) #создание объекта класса окна заставки
        intro.withdraw() #вызов метода, который скроет окно заставки через 2 секунды
        app = Controller(root) #создание объекта класса-контроллера
        root.mainloop() #запуск бесконечного цикла, который будет выполнять инструкции только до этой строки кода, но не после неё