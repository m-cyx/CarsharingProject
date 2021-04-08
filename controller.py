from models import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)


    def main(self):
        print('это мейн контроллера')
        self.view.main()

    def new_record(self): # Создание новой записи. Получает данные с View и отдаёт Model
        data = View.create_add_user_window()
        Model.add_record(data)

    def get_records(self): # Получение всех пользователей. Получает с Model пользователей и отдаёт View
        table = Model.get_all_tuples()
        View.create_users_table(table)

    def get_view_data(self):
        return View.return_data_list()


    def tool(self):
        data = Model.get_all_tuples()
        self.get_view_data(data)


if __name__ == '__main__':
    carsharing = Controller()
    carsharing.mainloop()
    