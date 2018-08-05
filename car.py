import os
import string
import csv

class BaseCar:
    def __init__(self, brand, photo_file_name,carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]
     

class Car(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'



class Truck(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, body):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        _body = str(body).split('x')
        if len(_body) == 3:
            self.body_length = float(_body[0])
            self.body_width = float(_body[1])
            self.body_height = float(_body[2])
        else:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0
    def get_body_volume(self):
        return self.body_length * self.body_height * self.body_width
        

class SpecMachine(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            try:
                if row[0] == 'car':
                    car_list.append(Car(brand=row[1], passenger_seats_count=row[2], photo_file_name=row[3],carrying=row[5]))
                elif row[0] == 'truck':
                    car_list.append(Truck(brand=row[1], photo_file_name=row[3], body=row[4], carrying=row[5]))
                elif row[0] == 'spec_machine':
                    car_list.append(SpecMachine(brand=row[1], photo_file_name=row[3], carrying=row[5], extra=row[6]))
            except IndexError:
                pass
    return car_list



#car_list = get_car_list('input.csv')

#for c in car_list:
#    print(c.get_photo_file_ext())