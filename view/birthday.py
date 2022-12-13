from appointment_template import AppointmentTemplate

class Birthday(AppointmentTemplate):
  def __init__(self, day, month, title):
    super().__init__(day, month, title)

  

  def __str__(self) -> str:
    return super(Birthday, self).__str__() + " AppointmentType: Birthday"
  
if __name__ == '__main__':
  x = Birthday('22', 'August', 'Mother')
  print(x)
 