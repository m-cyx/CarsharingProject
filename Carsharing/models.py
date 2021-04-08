from peewee import *
from connectToDB import *
import datetime

class Carsharing(BaseModel):
    id_client = AutoField(column_name='ID_Client')
    name = CharField(column_name='Name')
    surname = CharField(column_name='Surname')
    gender = CharField(column_name="Gender")
    phone_number = CharField(column_name='PhoneNumber')
    birth_date = DateField(column_name='BirthDate')
    driver_license_number = CharField(column_name='DriverLicenseNumber')
    driving_experience = IntegerField(column_name='DrivingExperience')
    status = CharField(column_name='Status')
    tariff = CharField(column_name='Tariff')
    distance_to_car = FloatField(column_name='DistanceToCar', null=True)
    order_date = DateField(column_name='OrderDate', null=True)
    trip_start_time = DateField(column_name='TripStartTime', null=True)
    trip_end_time = DateField(column_name='TripEndTime', null=True)
    car_number = CharField(column_name='CarNumber')

    #добавление записей в таблицу
    def add_record(self, data):
        row = Carsharing(
            name=data[0],
            surname=data[1],
            gender=data[2],
            phone_number=data[3],
            birth_date=data[4],
            driver_license_number=data[5],
            driving_experience=data[6],
            status=data[7],
            tariff=data[8],
            distance_to_car=data[9],
            order_date=datetime.datetime.now().strftime("%d.%m.%Y"),
            trip_start_time=data[10],
            trip_end_time=data[11],
            car_number=data[12],
        )
        row.save()

    #Данные получаются в виде списка словарей. Каждый элемент списка - это словарь, в котором ключи - названия полей
    def get_all_dict(self):
        try:
            result = Carsharing.select()
        except DoesNotExist as de:
            error_message = "Table does not exist"
            print(error_message)

        data = []
        for record in result:
            data.append(
                {
                    'name': record.name,
                    'surname': record.surname,
                    'gender': record.gender,
                    'phone_number': record.phone_number,
                    'birth_date': record.birth_date,
                    'driver_license_number': record.driver_license_number,
                    'driving_experience': record.driving_experience,
                    'status': record.status,
                    'tariff': record.tariff,
                    'distance_to_car': record.distance_to_car,
                    'order_date': record.order_date,
                    'trip_start_time': record.trip_start_time,
                    'trip_end_time': record.trip_end_time,
                    'car_number': record.car_number
                }
            )
        return data

    #Данные получаются в виде списка кортежей
    def get_all_tuples(self):
        try:
            result = Carsharing.select()
        except DoesNotExist as de:
            error_message = "Table does not exist"
            print(error_message)

        data = []
        for record in result:
            data.append(
                (
                    record.name,
                    record.surname,
                    record.gender,
                    record.phone_number,
                    record.birth_date,
                    record.driver_license_number,
                    record.driving_experience,
                    record.status,
                    record.tariff,
                    record.distance_to_car,
                    record.order_date,
                    record.trip_start_time,
                    record.trip_end_time,
                    record.car_number
                )
            )
        return data

    # #Получить текущий обьект класса
    # def getCur(self):
    #     return self.get(self)
    #
    # #Получить все обьекты
    # def getAll(self):
    #     query = self.select().execute()
    #
    # #Функция для добавления ОДНОГО элемента в модель и в базу данных
    # #На вход подается словарь вида {"field_name":"field_value"}
    # def insertOne(self, data):
    #     self.create(data)
    #
    # #Функция для добавления МНОГИХ элементов в модель и в базу данных
    # #На вход подается словарь вида {"field_name":"field_value"}
    # def insertMany(self, data):
    #     with db.atomic():
    #         for every_row in data:
    #             self.create(**every_row)
    #
    # #Заготовка под редактирование. Это еще необходимо
    # #обкашлять, что именно будем редачить и т.д.
    # def updateCur(self, data):
    #     query = self.update().where
    #     query.execute()
    #
    # #Удаление по ID
    # def deleteByID(self, id):
    #     tmp = self.get(self.id_client==id)
    #     tmp.delete_instance()

    class Meta:
        table_name = 'carsharing'
