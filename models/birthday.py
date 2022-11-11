from write import Write

class Birthday():
  def __init__(self, b_name, b_date, fle):
    self.b_name = b_name
    self.b_date = b_date
    self.fle = fle
  
  def write_file(self):
    return super.write_to_file(self.fle)