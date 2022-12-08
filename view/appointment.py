from appointment_template import AppointmentTemplate

class Appointment(AppointmentTemplate):

  def __init__(self, day, month, title, appt_time):
    super().__init__(day, month, title)
    self.appt_time = appt_time
    


  def __str__(self) -> str:
    return super(Appointment, self).__str__()  + f' Time: {self.appt_time} AppointmentType: Appointment'

if __name__ == "__main__":
  a = Appointment("1","2","3","4","5")
  print(a)


