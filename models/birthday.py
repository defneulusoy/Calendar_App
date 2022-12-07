from appointment_template import AppointmentTemplate

class Birthday(AppointmentTemplate):
  def __init__(self, description, date, title, file_name):
    super().__init__(description, date, title, file_name)

  
  def write_calendar(self):
    super(Birthday, self).write_to_calendar()

  def __str__(self) -> str:
    return super(Birthday, self).__str__()

