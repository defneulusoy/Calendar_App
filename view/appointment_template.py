import all_months
class AppointmentTemplate:
    def __init__(self, day, month, title) :
        self.day =day
        self.month = month
        self.title = title
        



    def __str__(self) -> str:
        return f'Day: {self.day} Month: {self.month} Title: {self.title}'


if __name__ == "__main__":
    a = AppointmentTemplate("3","March","Title")
    print(a)

