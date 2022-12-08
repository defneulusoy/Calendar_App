from appointment_template import AppointmentTemplate

class Birthday(AppointmentTemplate):
  def __init__(self, description, date, title):
    super().__init__(description, date, title)

  

  def __str__(self) -> str:
    return super(Birthday, self).__str__() + " AppointmentType: Birthday"
