# class
class Car:
  brand = "BMW"
  wheels = 4
  def accelerator(self):
    print("accelerate")
  def brake(self):
    print("brake")
# object
car1 = Car()
print(car1.brand)
print(car1.accelerator())
