from models import *
from connectToDB import *


if __name__ == '__main__':
    try:
        db.connect()
        Model.create_table()
    except:
        print("Error")

