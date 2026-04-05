# instance variable
class Student:
  name = "ray"
  age = 22
  def display(self):
    print(self.name, self.age)
s1 = Student()
s1.name = "Harsh"  # instance variable -> each class have it's own instance variable
s1.age = 26
s1.display()
s2 = Student()
s2.name = "Ellie"
s2.age = 3
s2.display()
