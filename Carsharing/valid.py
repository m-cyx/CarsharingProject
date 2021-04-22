import re
import datetime
import string
from abc import ABC, abstractmethod

class Validation(ABC):
    def validate(self, data):
        pass

class ValidPhone(Validation):
    def validate(self, data):
        phone = re.sub(r'\b\D', '', data)
        clear_phone = re.sub(r'[\ \(]?', '', phone)
        if re.findall(r'^[\+7|8]*?\d{10}$', clear_phone) or re.match(r'^\w+[\.]?(\w+)*\@(\w+\.)*\w{2,}$', string):
            return True
        else:
            return False

class ValidDate(Validation):
    def validate(self, data):
        try:
            datetime.datetime.strptime(data, "%d.%m.%Y")
            return True
        except ValueError:
            return False

class ValidStr(Validation):
    def validate(self, data):
        if data.isalpha():
            return True
        else:
            return False

class ValidTariff(Validation):
    def validate(self, data):
        if ():
            return True
        else:
            return False
class ValidNumber(Validation):
    def validate(self, data):
        if data.isdigit():
            return True
        else:
            return False

class ValidFloat(Validation):
    def validate(self, data):
        try:
            float(data)
            return True
        except:
            return False

class ValidIdentify(Validation):
    def validate(self, data):
        if data.isalnum():
            return True
        else:
            return False