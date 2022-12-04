from appointment_template import AppointmentTemplate

class Event():

    def __init__(self, description, date, title, e_time, fle) -> None:
        super().__init__(description, date, title)

        self.e_time = e_time
        self.fle = fle

    def write_file(self):
        super.write_to_file(self.fle)
