from appointment_template import AppointmentTemplate

class Assignment(AppointmentTemplate):

  def __init__(self, description, date, title, file_name, a_time):
    super().__init__(description, date, title, file_name)
    self.a_time = a_time

  def write_calendar(self):
    super(Assignment, self).write_to_calendar()

  def __str__(self) -> str:
    return super(Assignment, self).__str__() + self.a_time
