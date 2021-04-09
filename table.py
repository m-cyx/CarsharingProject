class Data_display: #класс, инициализирующий окно отображения информации из базы данных и содержащий методы взаимодействия с ним
        def __init__(self, master, menu = None):
                self.__master = master
                self.__master.geometry('1400x500')
                self.__master.configure(background = 'black')
                self.__master.overrideredirect(1)
                x = (root.winfo_screenwidth() - 1400) / 2
                y = (root.winfo_screenheight() - 800) / 2
                self.__master.wm_geometry("+%d+%d" % (x, y))   

        def __data_display_window_escape(self, ev, window): #метод, закрывающий окно отображения информации из базы данных и открывающий окно меню
                self.__master.withdraw()
                self._Table__id = 0
                self._Table__iid = 0
                self._Table__tree.delete(*self._Table__tree.get_children())
                window.deiconify(delay = False)
                window.focus_force()
        
class Table(Data_display): #класс, наследованный от класса Data_display инициализирующий таблицу и методы взаимодействия с ней
        def __init__(self, master, menu):
                Data_display.__init__(self, master, menu)
                self.__tree = ttk.Treeview(master, columns = ('ID', 'Name', 'Surname', 'Gender', 'PhoneNumber', 'BirthDate', 'DriverLicenseNumber', 'DrivingExperience', 'Status', 'Tariff', 'DistanceToCar', 'OrderDate', 'TripStartTime', 'TripEndTime', 'CarNumber'))
                self.__tree.heading('#0', text = 'ID')
                self.__tree.heading('#1', text = 'Name')
                self.__tree.heading('#2', text = 'Surname')
                self.__tree.heading('#3', text = 'Gender')
                self.__tree.heading('#4', text = 'PhoneNumber')
                self.__tree.heading('#5', text = 'BirthDate')
                self.__tree.heading('#6', text = 'DriverLicenseNumber')
                self.__tree.heading('#7', text = 'DrivingExperience')
                self.__tree.heading('#8', text = 'Status')
                self.__tree.heading('#9', text = 'Tariff')
                self.__tree.heading('#10', text = 'DistanceToCar')
                self.__tree.heading('#11', text = 'OrderDate')
                self.__tree.heading('#12', text = 'TripStartTime')
                self.__tree.heading('#13', text = 'TripEndTime')
                self.__tree.heading('#14', text = 'CarNumber')
                self.__tree.column('#0', stretch = tk.YES)
                self.__tree.column('#1', stretch = tk.YES)
                self.__tree.column('#2', stretch = tk.YES)
                self.__tree.column('#3', stretch = tk.YES)
                self.__tree.column('#4', stretch = tk.YES)
                self.__tree.column('#5', stretch = tk.YES)
                self.__tree.column('#6', stretch = tk.YES)
                self.__tree.column('#7', stretch = tk.YES)
                self.__tree.column('#8', stretch = tk.YES)
                self.__tree.column('#9', stretch = tk.YES)
                self.__tree.column('#10', stretch = tk.YES)
                self.__tree.column('#11', stretch = tk.YES)
                self.__tree.column('#12', stretch = tk.YES)
                self.__tree.column('#13', stretch = tk.YES)
                self.__tree.column('#14', stretch = tk.YES)
                self.__id = 0
                self.__iid = 0
                self.__scrolltabley = tk.Scrollbar(self._Data_display__master, command = self.__tree.yview)
                self.__scrolltablex = tk.Scrollbar(self._Data_display__master, command = self.__tree.xview)
                self.__tree.configure(yscrollcommand = self.__scrolltabley.set)
                self.__tree.configure(xscrollcommand = self.__scrolltablex.set)
                self.__scrolltabley.pack(side = tk.RIGHT, fill = tk.Y)
                self.__scrolltablex.pack(side = tk.BOTTOM, fill = tk.X)
                self.__tree.pack(expand = tk.YES, fill = tk.BOTH)
                self.__tree.bind('<Escape>', lambda ev: self._Data_display__data_display_window_escape(ev, menu))

        def focus_force(self): #метод, устанавливающий фокус на окно таблицы
                self.__tree.lift()
                self.__tree.focus_force()
                
        def insert_values(self, rows): #метод, добавляющий данные в таблицу
                for row in rows:
                        self.__tree.insert('', tk.END, iid = self.__iid, text = str(self.__id), values = row)
                        self.__id += 1
                        self.__iid += 1