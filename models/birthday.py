from appointment_template import AppointmentTemplate

class Birthday():
  def __init__(self, description, date, title, fle):
    super().__init__(description, date, title)
    self.fle = fle
  
  def write_file(self):
    super.write_to_file(self.fle)