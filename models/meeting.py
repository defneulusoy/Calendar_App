from appointment_template import AppointmentTemplate

class Meeting():

    def __init__(self, description, date, title, m_time, fle) -> None:
        super().__init__(description, date, title)
        self.m_time = m_time
        self.fle = fle

    def write_file(self):
        super.write_to_file(self.fle)