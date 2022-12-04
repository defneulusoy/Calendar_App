from appointment_template import AppointmentTemplate

class Assignment():

  def __init__(self, description, date, title, a_time, fle):
    super().__init__(description, date, title)
    self.a_time = a_time
    self.fle = fle

def write_file(self):
    super.write_to_file(self.fle)