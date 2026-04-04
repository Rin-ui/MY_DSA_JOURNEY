# constructor
class Student:
  def __init__(self, name, roll_no, marks):
    self.name = name
    self.roll_no = roll_no
    self.marks = marks
  def display(self):
    print(self.name, self.roll_no, self.marks)
s1 = Student("John", 10, 90)
print(s1.name)
print(s1.roll_no)
print(s1.marks)
s1.display()


