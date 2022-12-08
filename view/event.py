from appointment_template import AppointmentTemplate

class Event(AppointmentTemplate):

    def __init__(self, description, date, title, e_time) -> None:
        super().__init__(description, date, title)

        self.e_time = e_time



    def __str__(self) -> str:
        return super(Event, self).__str__() + f' Time: {self.e_time} AppointmentType: Event'
