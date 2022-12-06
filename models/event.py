from appointment_template import AppointmentTemplate

class Event(AppointmentTemplate):

    def __init__(self, description, date, title, file_name, e_time) -> None:
        super().__init__(description, date, title, file_name)

        self.e_time = e_time


    def write_calendar(self):
        super(Event, self).write_to_calendar()
