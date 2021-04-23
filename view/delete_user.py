import tkinter as tk
from PIL import Image, ImageTk
from os import listdir

class Delete_user:
    def __init__(self, master, menu, controller):
        self.__master = master
        self.__gif_index = 0
        self.__count_of_files = len(listdir(path = r'C:\Users\User\Desktop\CARSHARING\view\GIFS'))
        self.__cnt = 34
        self.__master.configure(background = 'black')
        self.__canvas_delete = tk.Canvas(self.__master, bg = 'black', highlightthickness = 0)
        self.__entry_id = tk.Entry(self.__canvas_delete, fg = 'grey', bg = 'white', relief = 'flat', width = 20)
        self.__frames = []
        self.__tmp = []
        self.__frameCnt = 34
        self.__delete_button = tk.Button(self.__canvas_delete, text = "Удалить пользователя", width = 26)
        self.__frames.append([tk.PhotoImage(file = r'C:\Users\User\Desktop\CARSHARING\view\GIFS\{0}.gif'.format(self.__gif_index), format = f'gif -index {i}').zoom(2,2).subsample(7,7) for i in range(self.__frameCnt)])
        self.__canvas_delete.pack(fill = 'both', expand = True)
        self.__master.geometry('320x180')
        self.__master.configure(background = 'black')
        self.__master.overrideredirect(1)
        self.__x = (master.winfo_screenwidth() - 320) / 2
        self.__y = (master.winfo_screenheight() - 180) / 2
        self.__master.wm_geometry("+%d+%d" % (self.__x, self.__y))
        if self.__count_of_files == 1:
                self.__canvas_delete.after(0, lambda : self.__update(0, 19, add = False))
        else:
                self.__gif_index += 1
                self.__canvas_delete.after(0, lambda : self.__update(0, 19, change_cnt = True))
        self.__entry_id.insert(0, 'ID')
        self.__entry_id.place(x = 100, y = 50, height = 20)
        self.__delete_button.place(x = 65, y = 110, height = 20)
        self.__entry_id.bind('<Enter>', lambda ev: self.__foc_in(ev, self.__entry_id))
        self.__entry_id.bind('<Leave>', lambda ev: self.__foc_out(ev, self.__entry_id, 'ID'))
        self.__delete_button.bind('<Button-1>', lambda ev: self.__check(ev, controller, menu))
        self.__master.bind('<Escape>', lambda ev: self.__delete_user_escape(ev, menu))
             
    def __foc_in(self, ev, ent): #метод, фокусирующий заданное поле ввода и скрывающий placeholder
        if ent['fg'] == 'grey':
            ent.delete('0', 'end')
       

    def __foc_out(self, ev, ent, string): #метод, проявляющий placeholder заданного поля ввода
        if not ent.get():
            self.__master.focus_force()
            ent.insert(0, string)
            ent['fg'] = 'grey'

    def __update(self, ind, cnt, add = True, change_cnt = False):
                if change_cnt == True and self.__count_of_files != self.__gif_index:
                        self.__cnt = Image.open(r'C:\Users\User\Desktop\CARSHARING\view\GIFS\{0}.gif'.format(self.__gif_index)).n_frames
                if self.__gif_index > 0 and ind < cnt and add == True:
                        img = self.__canvas_delete.create_image(0,0,image = self.__frames[self.__gif_index - 1][ind], anchor = 'nw')
                        ind += 1
                if add == True and ind < self.__cnt and self.__count_of_files != self.__gif_index:
                        self.__tmp.append(tk.PhotoImage(file = r'C:\Users\User\Desktop\CARSHARING\view\GIFS\{0}.gif'.format(self.__gif_index), format = f'gif -index {ind}').zoom(2,2).subsample(4,4)) 
                elif add == False and ind < cnt:
                        img = self.__canvas_delete.create_image(0,0,image = self.__frames[self.__gif_index][ind], anchor = 'nw')
                        return self.__canvas_delete.after(90, lambda: self.__update(ind + 1, cnt, False, False))
                elif add == False:
                        if self.__gif_index < self.__count_of_files:
                                if self.__gif_index + 1 != self.__count_of_files:
                                        self.__gif_index += 1
                                else:
                                        self.__gif_index = 0
                                self.__canvas_delete.delete('all')
                                return self.__canvas_delete.after(90, lambda: self.__update(0, len(self.__frames[self.__gif_index]), False, False))
                elif self.__flag == False and self.__count_of_files != 1 and self.__gif_index < self.__count_of_files:
                        self.__frames.append(self.__tmp)
                        if len(self.__frames) != self.__count_of_files:
                                self.__flag = True
                if ind >= cnt:
                        self.__tmp = []
                        self.__flag = False
                        if self.__gif_index < self.__count_of_files:
                                self.__gif_index += 1
                                self.__canvas_delete.delete('all')
                                return self.__canvas_delete.after(40, lambda: self.__update(0, len(self.__frames[self.__gif_index-1]), True, True))
                        else:
                                self.__gif_index = 0
                                self.__canvas_delete.delete('all')
                                self.__flag = True
                                return self.__canvas_delete.after(15, lambda: self.__update(0, len(self.__frames[self.__gif_index]), False, False))   
                else:
                        return self.__canvas_delete.after(15, lambda: self.__update(ind, cnt, True, False))
    
    def __check(self, ev, controller, menu):
        self.__master.withdraw()
        menu.deiconify(False)
        menu.focus_force()
        controller.delete_record(self)

    def return_id_for_delete_record(self):
        return self.__entry_id.get()

    def __delete_user_escape(self, ev, menu):
        self.__master.withdraw()
        menu.deiconify(delay = False)
        menu.focus_force()

    def focus_force(self): 
        self.__master.focus_force()

    def __after_err(self):
        self.__entry_id['bg'] = 'white'
        self.__entry_id.delete('0', 'end')
        self.__entry_id.insert(0, 'ID')
        self.__entry_id['fg'] = 'grey'
        self.__master.focus_force()

    def get_mes_incorrect_id(self, idd):
        if idd == 0:
            self.__entry_id['fg'] = 'black'
            self.__entry_id['bg'] = 'red'
            self.__entry_id.insert(2, " некорректен")
            self.__entry_id.after(1500, self.__after_err)
            self.__entry_id.place_forget()
        else:
            self.__master.withdraw()
            menu.deiconify(delay = False)
            self.__entry_id.place(x = 100, y = 50, height = 20)
            menu.focus_force()

    def __delete_user_escape(self, ev, menu): #метод, скрывающий окно добавления пользователя после нажатия ESCAPE
        self.__master.withdraw()
        menu.deiconify(delay = False)
        menu.focus_force()