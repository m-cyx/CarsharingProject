class Add_user: #класс, инициализирующий окно для добавления пользователя в базу данных и методы взаимодействия с ним
        def __init__(self, master, menu, controller):
                self.__master = master
                self.__gif_index = 0
                self.__cnt = 34
                self.__count_of_files = len(listdir(path = r'C:\Users\User\Desktop\CARSHARING\GIFS'))
                print(self.__count_of_files)
                self.__master.configure(background = 'black')
                self.__flag = False
                self.__canvas_add = tk.Canvas(self.__master, bg = 'black', highlightthickness = 0)
                self.__add_button = tk.Button(self.__canvas_add, text = "Добавить пользователя", width = 29)
                self.__entry_phone_number = tk.Entry(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 35)
                self.__entry_birth_date = tk.Entry(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 35)
                self.__lab_gender = tk.Label(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 30, text = 'Пол')
                self.__list_gender = ['мужской', 'женский']
                self.__list_tariff = ['первый тариф', 'второй тариф', 'третий тариф']
                self.__list_status = ['не арендована', 'арендована']
                self.__entry_driver_license_number = tk.Entry(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 35)
                self.__entry_driving_experience = tk.Entry(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 35)
                self.__entry_status = tk.Entry(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 35)
                self.__lab_tariff = tk.Label(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 30, text = 'Тариф')
                self.__lab_status = tk.Label(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 30, text = 'Статус машины')
                self.__entry_distance_to_car = tk.Entry(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 35)
                self.__entry_trip_start_time = tk.Entry(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 35)
                self.__entry_trip_end_time = tk.Entry(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 35)
                self.__entry_car_number = tk.Entry(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 35)
                self.__frames = []
                self.__tmp = []
                self.__frameCnt = 34
                self.__frames.append([tk.PhotoImage(file = r'C:\Users\User\Desktop\CARSHARING\GIFS\{0}.gif'.format(self.__gif_index), format = f'gif -index {i}').zoom(2,2).subsample(4,4) for i in range(self.__frameCnt)])
                self.__canvas_add.pack(fill = 'both', expand = True)
                self.__master.geometry('560x315')
                self.__master.configure(background = 'black')
                self.__master.overrideredirect(1)
                self.__x = (root.winfo_screenwidth() - 560) / 2
                self.__y = (root.winfo_screenheight() - 315) / 2
                self.__master.wm_geometry("+%d+%d" % (self.__x, self.__y))
                if self.__count_of_files == 1:
                        self.__canvas_add.after(0, lambda : self.__update(0, 19, add = False))
                else:
                        self.__gif_index += 1
                        self.__canvas_add.after(0, lambda : self.__update(0, 19, change_cnt = True))
                self.__entry_name_surname = tk.Entry(self.__canvas_add, fg = 'grey', bg = 'white', relief = 'flat', width = 35)
                self.__entry_name_surname.insert(0, 'ИФ')
                self.__entry_phone_number.insert(0, 'Номер телефона')
                self.__entry_birth_date.insert(0, 'Дата рождения')
                self.__entry_driver_license_number.insert(0, 'Номер водительского удостоверения')
                self.__entry_driving_experience.insert(0, 'Стаж вождения')
                self.__entry_distance_to_car.insert(0, 'Расстояние до машины(км)')
                self.__entry_trip_start_time.insert(0, 'Дата начала пользования')
                self.__entry_trip_end_time.insert(0, 'Дата конца пользования')
                self.__entry_car_number.insert(0, 'Номер машины')
                self.__entry_name_surname.place(x = 26, y = 15, height = 22)
                self.__lab_status.place(x = 320, y = 235, height = 22)
                self.__lab_gender.place(x = 26, y = 55, height = 22)
                self.__entry_phone_number.place(x = 26, y = 135, height = 22)
                self.__entry_birth_date.place(x = 26, y = 95, height = 22)
                self.__entry_driver_license_number.place(x = 26, y = 185, height = 22)
                self.__entry_driving_experience.place(x = 26, y = 235, height = 22)
                self.__add_button.place(x = 175, y = 275, height = 21)
                self.__lab_tariff.place(x = 320, y = 55, height = 22)
                self.__entry_distance_to_car.place(x = 320, y = 95, height = 22)
                self.__entry_trip_start_time.place(x = 320, y = 135, height = 22)
                self.__entry_trip_end_time.place(x = 320, y = 185, height = 22)
                self.__entry_car_number.place(x = 320, y = 15, height = 22)
                self.__entry_name_surname.bind('<Enter>', lambda ev: self.__foc_in(ev, self.__entry_name_surname))
                self.__entry_name_surname.bind('<Leave>', lambda ev: self.__foc_out(ev, self.__entry_name_surname, 'ИФ'))
                self.__lab_gender.bind('<Button-1>', self.__view_listbox_gender)
                self.__lab_status.bind('<Button-1>', self.__view_listbox_status)
                self.__entry_phone_number.bind('<Enter>', lambda ev: self.__foc_in(ev, self.__entry_phone_number))
                self.__entry_phone_number.bind('<Leave>', lambda ev: self.__foc_out(ev, self.__entry_phone_number, 'Номер телефона'))
                self.__entry_birth_date.bind('<Enter>', lambda ev: self.__foc_in(ev, self.__entry_birth_date))
                self.__entry_birth_date.bind('<Leave>', lambda ev: self.__foc_out(ev, self.__entry_birth_date, 'Дата рождения'))
                self.__entry_driver_license_number.bind('<Enter>', lambda ev: self.__foc_in(ev, self.__entry_driver_license_number))
                self.__entry_driver_license_number.bind('<Leave>', lambda ev: self.__foc_out(ev, self.__entry_driver_license_number, 'Номер водительского удостоверения'))
                self.__entry_driving_experience.bind('<Enter>', lambda ev: self.__foc_in(ev, self.__entry_driving_experience))
                self.__entry_driving_experience.bind('<Leave>', lambda ev: self.__foc_out(ev, self.__entry_driving_experience, 'Стаж вождения'))
                self.__lab_tariff.bind('<Button-1>', self.__view_listbox_tariff)
                self.__entry_distance_to_car.bind('<Enter>', lambda ev: self.__foc_in(ev, self.__entry_distance_to_car))
                self.__entry_distance_to_car.bind('<Leave>', lambda ev: self.__foc_out(ev, self.__entry_distance_to_car, 'Расстояние до машины'))
                self.__entry_trip_start_time.bind('<Enter>', lambda ev: self.__foc_in(ev, self.__entry_trip_start_time))
                self.__entry_trip_start_time.bind('<Leave>', lambda ev: self.__foc_out(ev, self.__entry_trip_start_time, 'Дата начала пользования'))
                self.__entry_trip_end_time.bind('<Enter>', lambda ev: self.__foc_in(ev, self.__entry_trip_end_time))
                self.__entry_trip_end_time.bind('<Leave>', lambda ev: self.__foc_out(ev, self.__entry_trip_end_time, 'Дата конца пользования'))
                self.__entry_car_number.bind('<Enter>', lambda ev: self.__foc_in(ev, self.__entry_car_number))
                self.__entry_car_number.bind('<Leave>', lambda ev: self.__foc_out(ev, self.__entry_car_number, 'Номер машины'))
                self.__add_button.bind('<Button-1>', lambda ev: controller.new_record(ev, self))
                self.__master.bind('<Escape>', lambda ev: self.__add_user_escape(ev, menu))

        def return_data_list(self):
                lis = [self.__entry_name_surname.get(), self.__lab_gender['text'], self.__entry_phone_number.get(), self.__entry_birth_date.get(), self.__entry_driver_license_number.get(), self.__entry_driving_experience.get(), self.__lab_status['text'], self.__lab_tariff['text'], self.__entry_distance_to_car.get(), self.__entry_trip_start_time.get(), self.__entry_trip_end_time.get()]
                return lis

        #изменить на lambda эту функцию с аргументами все entry и selection_box тоже
        def __view_listbox_gender(self, event):
                self.__gender_listbox = tk.Listbox(self.__canvas_add, selectmode = tk.SINGLE, width = 36)
                self.__gender_listbox.insert(0, *self.__list_gender)
                self.__gender_listbox.place(x = 26, y = 65, height = 22)
                self.__gender_listbox.bind('<Double-Button-1>', lambda ev: self.selection_listbox(ev, self.__gender_listbox, self.__lab_gender))

        def __view_listbox_status(self, event):
                self.__status_listbox = tk.Listbox(self.__canvas_add, selectmode = tk.SINGLE, width = 36)
                self.__status_listbox.insert(0, *self.__list_status)
                self.__status_listbox.place(x = 320, y = 235, height = 22)
                self.__status_listbox.bind('<Double-Button-1>', lambda ev: self.selection_listbox(ev, self.__status_listbox, self.__lab_status))
        
        def selection_listbox(self, ev, lbox, ll):
                if ll == self.__lab_gender and lbox.curselection()[0] == 0:
                        ll['fg'] = 'blue'
                        self.__add_button['fg'] = 'blue'
                        if self.__entry_name_surname['fg'] != 'grey':
                                self.__entry_name_surname['fg'] = 'blue'
                        if self.__entry_phone_number['fg'] != 'grey':
                                self.__entry_phone_number['fg'] = 'blue'
                        if self.__entry_birth_date['fg'] != 'grey':
                                self.__entry_birth_date['fg'] = 'blue'
                        if self.__entry_driver_license_number['fg'] != 'grey':
                                self.__entry_driver_license_number['fg'] = 'blue'
                        if self.__entry_driving_experience['fg'] != 'grey':
                                self.__entry_driving_experience['fg'] = 'blue'
                        if self.__lab_tariff['fg'] != 'grey':
                                self.__lab_tariff['fg'] = 'blue'
                        if self.__entry_distance_to_car['fg'] != 'grey':
                                self.__entry_distance_to_car['fg'] = 'blue'
                        if self.__entry_trip_start_time['fg'] != 'grey':
                                self.__entry_trip_start_time['fg'] = 'blue'
                        if self.__entry_trip_end_time['fg'] != 'grey':
                                self.__entry_trip_end_time['fg'] = 'blue'
                        if self.__entry_car_number['fg'] != 'grey':
                                self.__entry_car_number['fg'] = 'blue'
                        if self.__lab_status['fg'] != 'grey':
                                self.__lab_status['fg'] = 'blue'
                        ll['text'] = "мужской"
                        
                elif ll == self.__lab_gender:
                        ll['fg'] = 'purple'
                        self.__add_button['fg'] = 'purple'
                        if self.__entry_name_surname['fg'] != 'grey':
                                self.__entry_name_surname['fg'] = 'purple'
                        if self.__entry_phone_number['fg'] != 'grey':
                                self.__entry_phone_number['fg'] = 'purple'
                        if self.__entry_birth_date['fg'] != 'grey':
                                self.__entry_birth_date['fg'] = 'purple'
                        if self.__entry_driver_license_number['fg'] != 'grey':
                                self.__entry_driver_license_number['fg'] = 'purple'
                        if self.__entry_driving_experience['fg'] != 'grey':
                                self.__entry_driving_experience['fg'] = 'purple'
                        if self.__lab_tariff['fg'] != 'grey':
                                self.__lab_tariff['fg'] = 'purple'
                        if self.__entry_distance_to_car['fg'] != 'grey':
                                self.__entry_distance_to_car['fg'] = 'purple'
                        if self.__entry_trip_start_time['fg'] != 'grey':
                                self.__entry_trip_start_time['fg'] = 'purple'
                        if self.__entry_trip_end_time['fg'] != 'grey':
                                self.__entry_trip_end_time['fg'] = 'purple'
                        if self.__entry_car_number['fg'] != 'grey':
                                self.__entry_car_number['fg'] = 'purple'
                        if self.__lab_status['fg'] != 'grey':
                                self.__lab_status['fg'] = 'purple'
                        ll['text'] = "женский"
                elif ll == self.__lab_tariff and lbox.curselection()[0] == 0:
                        if self.__lab_gender['fg'] == 'grey':
                                ll['fg'] = 'black'
                        elif self.__lab_gender['fg'] == 'blue':
                                ll['fg'] = 'blue'
                        else:
                                ll['fg'] = 'purple'
                        ll['text'] = 'первый тариф'
                elif ll == self.__lab_tariff and lbox.curselection()[0] == 1:
                        if self.__lab_gender['fg'] == 'grey':
                                ll['fg'] = 'black'
                        elif self.__lab_gender['fg'] == 'blue':
                                ll['fg'] = 'blue'
                        else:
                                ll['fg'] = 'purple'
                        ll['text'] = 'второй тариф'

                elif ll == self.__lab_tariff and lbox.curselection()[0] == 2:
                        if self.__lab_gender['fg'] == 'grey':
                                ll['fg'] = 'black'
                        elif self.__lab_gender['fg'] == 'blue':
                                ll['fg'] = 'blue'
                        else:
                                ll['fg'] = 'purple'
                        ll['text'] = 'третий тариф'
                elif ll == self.__lab_status and lbox.curselection()[0] == 0:
                        if self.__lab_gender['fg'] == 'grey':
                                ll['fg'] = 'black'
                        elif self.__lab_gender['fg'] == 'blue':
                                ll['fg'] = 'blue'
                        else:
                                ll['fg'] = 'purple'
                        ll['text'] = 'Не арендована'
                else:
                        if self.__lab_gender['fg'] == 'grey':
                                ll['fg'] = 'black'
                        elif self.__lab_gender['fg'] == 'blue':
                                ll['fg'] = 'blue'
                        else:
                                ll['fg'] = 'purple'
                        ll['text'] = 'арендована'
                lbox.place_forget()

        def __view_listbox_tariff(self, event):
                self.__tariff_listbox = tk.Listbox(self.__canvas_add, selectmode = tk.SINGLE, width = 36)
                self.__tariff_listbox.insert(0, *self.__list_tariff)
                self.__tariff_listbox.place(x = 320, y = 65, height = 22)
                self.__tariff_listbox.bind('<Double-Button-1>', lambda ev: self.selection_listbox(ev, self.__tariff_listbox, self.__lab_tariff))

        def __update(self, ind, cnt, add = True, change_cnt = False):
                if change_cnt == True and self.__count_of_files != self.__gif_index:
                        self.__cnt = Image.open(r'C:\Users\User\Desktop\CARSHARING\GIFS\{0}.gif'.format(self.__gif_index)).n_frames
                if self.__gif_index > 0 and ind < cnt and add == True:
                        img = self.__canvas_add.create_image(0,0,image = self.__frames[self.__gif_index - 1][ind], anchor = 'nw')
                        ind += 1
                if add == True and ind < self.__cnt and self.__count_of_files != self.__gif_index:
                        self.__tmp.append(tk.PhotoImage(file = r'C:\Users\User\Desktop\CARSHARING\GIFS\{0}.gif'.format(self.__gif_index), format = f'gif -index {ind}').zoom(2,2).subsample(4,4)) 
                elif add == False and ind < cnt:
                        img = self.__canvas_add.create_image(0,0,image = self.__frames[self.__gif_index][ind], anchor = 'nw')
                        return self.__canvas_add.after(90, lambda: self.__update(ind + 1, cnt, False, False))
                elif add == False:
                        if self.__gif_index < self.__count_of_files:
                                if self.__gif_index + 1 != self.__count_of_files:
                                        self.__gif_index += 1
                                else:
                                        self.__gif_index = 0
                                self.__canvas_add.delete('all')
                                return self.__canvas_add.after(90, lambda: self.__update(0, len(self.__frames[self.__gif_index]), False, False))
                elif self.__flag == False and self.__count_of_files != 1 and self.__gif_index < self.__count_of_files:
                        self.__frames.append(self.__tmp)
                        if len(self.__frames) != self.__count_of_files:
                                self.__flag = True
                if ind >= cnt:
                        self.__tmp = []
                        self.__flag = False
                        if self.__gif_index < self.__count_of_files:
                                self.__gif_index += 1
                                self.__canvas_add.delete('all')
                                return self.__canvas_add.after(40, lambda: self.__update(0, len(self.__frames[self.__gif_index-1]), True, True))
                        else:
                                self.__gif_index = 0
                                self.__canvas_add.delete('all')
                                self.__flag = True
                                return self.__canvas_add.after(15, lambda: self.__update(0, len(self.__frames[self.__gif_index]), False, False))   
                else:
                        return self.__canvas_add.after(15, lambda: self.__update(ind, cnt, True, False))

        def __foc_in(self, ev, ent): #метод, фокусирующий заданное поле ввода и скрывающий placeholder
                if ent['fg'] == 'grey':
                        ent.delete('0', 'end')
                        if self.__lab_gender['fg'] == 'grey':
                                ent['fg'] = 'black'
                        elif self.__lab_gender['fg'] == 'blue':
                                ent['fg'] = 'blue'
                        else:
                                ent['fg'] = 'purple'


        def __foc_out(self, ev, ent, string): #метод, проявляющий placeholder заданного поля ввода
                if not ent.get():
                        self.__master.focus_force()
                        ent.insert(0, string)
                        ent['fg'] = 'grey'
                
        def __add_user_escape(self, ev, menu): #метод, скрывающий окно добавления пользователя после нажатия ESCAPE
                self.__master.withdraw()
                menu.deiconify(delay = False)
                menu.focus_force()


        def focus_force(self): #метод, устанавливающий фокус на окно ввода пользователя
                self.__master.focus_force()