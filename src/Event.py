class Event:
    def __init__(self, id, title, date, start_time, end_time, location):
        self.id: int = id
        self.title: str = title
        
        if self._validate_date(date):
            self.date: str = date
        else:
            print("ERROR: Invalid date")
            return None
        
        if self._validate_time(start_time) and self._validate_time(end_time):
            self.start_time: str = start_time
            self.end_time: str = end_time
        else:
            return None
        
        self.location: str = location
    
    def __str__(self):
        return f"{self.id}: {self.title} on {self.date} from {self.start_time} to {self.end_time} at {self.location}"

    def __repr__(self):
        return self.__str__()

    def _validate_date(self, date: str):
        split_dt = date.split('-')
        try:
            assert(len(split_dt) == 3)

            assert(len(split_dt[0]) == 4)
            year = int(split_dt[0])
            
            assert(len(split_dt[1]) == 2)
            month = int(split_dt[1])
            assert(0 < month < 13)
            
            assert(len(split_dt[2]) == 2)
            day = int(split_dt[2])
            assert(0 < day < 32)
            
            return True
        except Exception as e:
            print(e)
            print("ERROR: Date must be of format: YYYY-MM-DD")
            return False
    
    def _validate_time(self, time: str):
        split_time = time.split(":")
        try:
            assert(len(split_time) == 2)
            
            assert(len(split_time[0]) <= 2)
            hour = int(split_time[0])
            assert(0 <= hour < 24)
            
            assert(len(split_time[1]) == 2)
            minute = int(split_time[1])
            assert(0 <= minute < 60)
            return True
        except:
            print("ERROR: Time must be of format HH:MM")
            return False
    
    def get_year(self):
        date = self.date.split("-")
        return int(date[0])
    
    def get_month(self):
        date = self.date.split("-")
        return int(date[1])

    def get_day(self):
        date = self.date.split("-")
        return int(date[2])
    
    def get_start_hour(self):
        time = self.start_time.split(":")
        return int(time[0])
    
    def get_start_min(self):
        time = self.start_time.split(":")
        return int(time[1])
    
    def get_end_hour(self):
        time = self.end_time.split(":")
        return int(time[0])

    def get_end_min(self):
        time = self.end_time.split(":")
        return int(time[1])
    
    
def compare_event_times(a: Event, b: Event):
    """
    This functiont takes two events as inputs. If event a starts before event b,
    we return 1. if b starts before a we return -1
    """
    a_year = a.get_year()
    a_month = a.get_month()
    a_day = a.get_day()
    a_date = a_year * 365 + a_month * 31 + a_day
    b_year = b.get_year()
    b_month = b.get_month()
    b_day = b.get_day()
    b_date = b_year * 365 + b_month * 31 + b_day
    if a_date < b_date:
        return 1
    elif a_date > b_date:
        return -1
    
    # if we reach this point, events are on same day and we must compare time
    a_start_hour = a.get_start_hour()
    a_start_min = a.get_start_min()
    a_time = a_start_hour * 60 + a_start_min
    
    b_start_hour = b.get_start_hour()
    b_start_min = b.get_start_min()
    b_time = b_start_hour * 60 + b_start_min

    if a_time <= b_time:
        return 1
    elif a_time > b_time:
        return -1
    else:
        print("ERROR: This should never be printed")
        return