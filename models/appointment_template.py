from templates import monthly_template

class AppointmentTemplate:
    def __init__(self, description, date, title, file_name) -> None:
        self.description = description
        self.date = date
        self.title = title
        self.file_name = file_name

    def write_to_calendar(self):
        pass



