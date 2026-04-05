# class variable
class Student:
  name = "ray" # class variable --> same along all objects that uses this class blue print
  age = 22
  def display(self):
    print(self.name, self.age)
s1 = Student()
s1.display()
s2 = Student()
s2.display()
