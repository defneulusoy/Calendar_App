from write import Write

class Meeting():

    def __init__(self, m_title, m_date, m_description, m_time, fle) -> None:
        self.m_title = m_title
        self.m_date = m_date
        self.m_description = m_description
        self.m_time = m_time
        self.fle = fle

    def write_file(self):
        return super.write_to_file(self.fle)