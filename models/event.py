from write import Write

class Event():

    def __init__(self, e_title, e_date, e_description, e_time, fle) -> None:
        self.e_title = e_title
        self.e_date = e_date
        self.e_description = e_description
        self.e_time = e_time
        self.fle = fle

    def write_file(self):
        return super.write_to_file(self.fle)
