class Car:
  total_car=0

  def __init__(self,brand,modal):
    self.__brand=brand
    self.__modal=modal
    Car.total_car+=1

  def get_brand(self):
    return self.__brand+"!!!"
  
  def displayname(self):
    return f"{self.__brand} {self.__modal}"
  
  def fuel_type(self):
    return f"{self.displayname()} is type of petrol Car"
  
  @staticmethod
  def general_description():
    return "Static methods are typically accessed via the class, but can also be called from instances."
  @property
  def modal(self):
    return self.__modal
  

class ElectricCar(Car):
  def __init__(self,__brand,__modal,battery_size):
    super().__init__(__brand,__modal)
    self.battery_size=battery_size

  def fuel_type(self):
    return f"{self.displayname()} is type of Electric Car"
  


first_car=Car("maruti","suzuki")

# print(first_car.brand)
# print(first_car.modal)
# print(first_car.displayname())
# print(first_car.fuel_type())

# my_tesla=ElectricCar("Tesla","Model S","85kwh")
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))
# print(my_tesla.__modal)
# print(my_tesla.fuel_type())
# I can't access this brand because it is encapsulated if i want to access brand then i have to use getter method to use brand which is get_brand()
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
# print(my_tesla.battery_size)
# print(my_tesla.displayname())

# print(Car.total_car)

# print(first_car.general_description())
# print(Car.general_description())

class Battery:
  def battery_info(self):
    return "this is powerfull battery"
class Engine:
   def Engine_info(self):
    return "this is powerfull Engine"

class Electric_Car(Battery,Engine,Car):
  pass

my_new_tesla=Electric_Car("Newtesla","Model w")
print(my_new_tesla.battery_info())
print(my_new_tesla.Engine_info())