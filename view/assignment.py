from appointment_template import AppointmentTemplate

class Assignment(AppointmentTemplate):

  def __init__(self, day, month, title, a_time):
    super().__init__(day, month, title)
    self.a_time = a_time


  def __str__(self) -> str:
    return super(Assignment, self).__str__() + f' Time: {self.a_time} AppointmentType: Assignment'

if __name__ == '__main__':
  x = Assignment('3', 'March', 'Math Homework', '23:59')
  print(x)