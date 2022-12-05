from appointment_template import AppointmentTemplate

class Assignment(AppointmentTemplate):

  def __init__(self, description, date, title, file_name, a_time):
    super().__init__(description, date, title, file_name)
    self.a_time = a_time

  def write_file(self):
    super(Assignment, self).write_to_file()