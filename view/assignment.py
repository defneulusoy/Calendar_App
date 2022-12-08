from appointment_template import AppointmentTemplate

class Assignment(AppointmentTemplate):

  def __init__(self, description, date, title, a_time):
    super().__init__(description, date, title)
    self.a_time = a_time


  def __str__(self) -> str:
    return super(Assignment, self).__str__() + f' Time: {self.a_time} AppointmentType: Assignment'
