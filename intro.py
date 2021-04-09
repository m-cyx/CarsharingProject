class Intro: #класс, инициализирующий окно заставки и методы взаимодействия с ним
        def __init__(self, master):
                self.__master = master
                self.__master.geometry('235x130')
                x = (root.winfo_screenwidth() - 235) / 2
                y = (root.winfo_screenheight() - 130) / 2
                self.__master.wm_geometry("+%d+%d" % (x, y))
                self.__Label1 = tk.Label(self.__master, text='KaRDeli', fg = 'blue', bg = 'black', font = 'Calibri 20')
                self.__Label1.place(x = 71, y = 30)
                self.__Label2 = tk.Label(self.__master, text = 'КаРДели', fg = 'blue', bg = 'black', font = 'Calibri 20')
                self.__Label2.place(x = 65, y = 65)
                self.__master.configure(background = 'black')
                self.__master.overrideredirect(1)

        def withdraw(self): #метод, закрывающий окно заставки спустя 2 секунды
                self.__master.after(2000, self.__master.withdraw)