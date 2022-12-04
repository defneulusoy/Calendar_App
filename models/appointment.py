from appointment_template import AppointmentTemplate

class Appointment(AppointmentTemplate):

  def __init__(self, description, date, title, appt_time, fle):
    super().__init__(description, date, title)
    self.appt_time = appt_time
    self.fle = fle

def write_file(self):
    super.write_to_file(self.fle)