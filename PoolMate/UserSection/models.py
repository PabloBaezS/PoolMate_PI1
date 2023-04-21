from django.db import models


class CustomUser:
    def __init__(self, idUser):
        self.homeAddress = None
        self.phone = None
        self.password = None
        self.email = None
        self.name = None
        self.idUser = idUser

    def name(self,name):
        self.name = name

    def email(self,email):
        self.email = email

    def password(self, password):
        self.password = password

    def phone(self,phone):
        self.phone = phone

    def homeAddress(self, homeAddress):
        self.homeAddress = homeAddress

    def get_phone(self):
        return self.phone

    def get_homeAddress(self):
        return self.homeAddress

    def change_password(self, newPassword):
        self.password = newPassword
        print("Password changed successfully")

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def get_idUser(self):
         return self.idUser

    def login(CustomUser):
        return CustomUser

class Passenger(CustomUser):
    def __init__(self, idUser):
        super().__init__(idUser)
        self.dropoff = None
        self.pickup = None

    def pickup(self, pickup):
        self.pickup = pickup

    def dropoff(self, dropoff):
        self.dropoff = dropoff

    def rideRequest(self):
        pass #Falta terminar!!!!

    def feedback(self):
        pass  # Falta terminar!!!!

    def seeRoute(self):
        pass  # Falta terminar!!!!