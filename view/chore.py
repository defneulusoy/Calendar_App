from appointment_template import AppointmentTemplate

class Chore(AppointmentTemplate):

  def __init__(self, day, month, title):
    super().__init__(day, month, title)



  def __str__(self) -> str:
    return super(Chore, self).__str__() + " AppointmentType: Chore"

if __name__ == '__main__':
  x = Chore('5', 'December', 'General Cleaning')
  print(x)
