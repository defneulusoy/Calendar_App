from appointment_template import AppointmentTemplate

class Appointment(AppointmentTemplate):

  def __init__(self, description, date, title, appt_time, fle):
    super().__init__(description, date, title)
    self.appt_time = appt_time
    self.fle = fle

  def write_calendar(self):
    super(Appointment, self).write_to_calendar()

  def __str__(self) -> str:
    return super(Appointment, self).__str__() + self.appt_time


