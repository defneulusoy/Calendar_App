from appointment_template import AppointmentTemplate

class Meeting(AppointmentTemplate):

    def __init__(self, description, date, title, m_time) -> None:
        super().__init__(description, date, title)
        self.m_time = m_time


    def __str__(self) -> str:
        return super(Meeting, self).__str__() + f' Time: {self.m_time} AppointmentType: Meeting'

if __name__ == '__main__':
    x = Meeting('18', 'October', 'Project Meeting', '19:30')
    print(x)
