from appointment_template import AppointmentTemplate

class Meeting(AppointmentTemplate):

    def __init__(self, description, date, title, file_name, m_time) -> None:
        super().__init__(description, date, title, file_name)
        self.m_time = m_time


    def write_calendar(self):
        super(Meeting, self).write_to_calendar()

