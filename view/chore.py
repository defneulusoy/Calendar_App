from appointment_template import AppointmentTemplate

class Chore(AppointmentTemplate):

  def __init__(self, description, date, title):
    super().__init__(description, date, title)



  def __str__(self) -> str:
    return super(Chore, self).__str__() + " AppointmentType: Chore"
