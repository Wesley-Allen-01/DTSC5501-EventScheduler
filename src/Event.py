class Event:
    def __init__(self, id, title, date, start_time, end_time, location):
        self.id: int = id
        self.title: str = title
        self.date: str = date
        self.start_time: str = start_time
        self.end_time: str = end_time
        self.location: str = location
    
    def __str__(self):
        return f"{self.id}: {self.title} on {self.date} from {self.start_time} to {self.end_time} at {self.location}"

    def __repr__(self):
        return self.__str__()