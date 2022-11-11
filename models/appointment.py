from write import Write

class Appointment():

  def __init__(self, appt_name, appt_description, appt_date, appt_time, fle):
    self.appt_name = appt_name
    self.appt_description = appt_description
    self.appt_date = appt_date
    self.appt_time = appt_time
    self.fle = fle

def write_file(self):
    return super.write_to_file(self.fle)