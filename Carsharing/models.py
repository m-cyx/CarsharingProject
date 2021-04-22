from peewee import *
from connectToDB import *
import datetime
from valid import *

class myType():
    def __init__(self, valid: Validation):
        self.value = None
        self.valid = valid
        self.incorrect = True

    def setValid(self, valid: Validation):
        self.valid = valid

    def set(self, value):
        if self.valid.validate(self, value):
            self.value = value
            self.incorrect = False
        else:
            self.incorrect = True

    def getValue(self):
        return self.value

    def wrongValue(self):
        return self.incorrect

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

    def check_id(self,id):
        a = myType(ValidNumber)
        a.set(id)
        if a.wrongValue():
            return False
        return True

    #Функция проверки данных. Возвращает список проверенных данных либо список данных, не прошедших проверку.
    def check_data(self, data):
        a = myType(Validation)
        res_data = []
        error_list = []

        tmp = data[0].split()
        print(tmp)
        a.setValid(ValidStr)
        a.set(tmp[0])
        res_data.append(a.getValue())
        if a.wrongValue():
            error_list.append(0)

        a.setValid(ValidStr)
        a.set(tmp[1])
        res_data.append(a.getValue())
        if a.wrongValue():
            try:
                error_list.remove(0)
            except IndexError:
                pass
            error_list.append(0)

        a.setValid(Validation)
        a.set(data[1])
        res_data.append(a.getValue())

        a.setValid(ValidPhone)
        a.set(data[2])
        res_data.append(a.getValue())
        if a.wrongValue():
            error_list.append(2)

        a.setValid(ValidDate)
        a.set(data[3])
        res_data.append(a.getValue())
        if a.wrongValue():
            error_list.append(3)

        a.setValid(ValidIdentify)
        a.set(data[4])
        res_data.append(a.getValue())
        if a.wrongValue():
            error_list.append(4)

        a.setValid(ValidNumber)
        a.set(data[5])
        res_data.append(a.getValue())
        if a.wrongValue():
            error_list.append(5)

        a.setValid(Validation)
        a.set(data[6])
        res_data.append(a.getValue())

        a.setValid(Validation)
        a.set(data[7])
        res_data.append(a.getValue())


        a.setValid(ValidFloat)
        a.set(data[8])
        res_data.append(a.getValue())
        if a.wrongValue():
            error_list.append(8)

        res_data.append(datetime.datetime.now().strftime("%d.%m.%Y"))

        a.setValid(ValidDate)
        a.set(data[9])
        res_data.append(a.getValue())
        if a.wrongValue():
            error_list.append(9)

        a.setValid(ValidDate)
        a.set(data[10])
        res_data.append(a.getValue())
        if a.wrongValue():
            error_list.append(10)

        a.setValid(ValidIdentify)
        a.set(data[11])
        res_data.append(a.getValue())
        if a.wrongValue():
            error_list.append(11)

        if not error_list:
            return res_data
        else:
            return {"error": error_list}

    #добавление записей в таблицу. Возвращает список индексов полей, не прошедших проверку либо None
    def add_record(self, data):
        res = self.check_data(data)
        try:
            return res["error"]
        except:
            data = res
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
                order_date=data[10],
                trip_start_time=data[11],
                trip_end_time=data[12],
                car_number=data[13],
            )
            row.save()
            return None

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

    #Редактирование по ID. Возвращает список индексов полей, не прошедших проверку, None, либо 0 в случае некорректного айди
    def change_record(self, data, id):
        if not self.check_id(id):
            return 0
        res = self.check_data(data)
        try:
            return res["error"]
        except:
            data = res
            change = {
                Carsharing.name: data[0],
                Carsharing.surname: data[1],
                Carsharing.gender: data[2],
                Carsharing.phone_number: data[3],
                Carsharing.birth_date: data[4],
                Carsharing.driver_license_number: data[5],
                Carsharing.driving_experience: data[6],
                Carsharing.status: data[7],
                Carsharing.tariff: data[8],
                Carsharing.distance_to_car: data[9],
                Carsharing.order_date: data[10],
                Carsharing.trip_start_time: data[11],
                Carsharing.trip_end_time: data[12],
                Carsharing.car_number: data[13]
            }
            query = Carsharing.update(change).where(Carsharing.id_client == id)
            query.execute()
            return None

    #Удаление по ID. Возвращает 0 в случае некорректного айди
    def delete_by_id(self, id):
        if not self.check_id(id):
            return 0
        query = Carsharing.delete().where(Carsharing.id_client == id)
        query.execute()

    class Meta:
        table_name = 'carsharing'
