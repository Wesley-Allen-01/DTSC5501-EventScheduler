from Event import Event

class ArrayList:
    def __init__(self, event=None):
        if event:
            self.events = [event]
        else:
            self.events = []
          
    def __str__(self):
        ret = """
        Events shown below:
        
        -----------------------------------
        
        """
        for ev in self.events:
            ret += str(ev)
            ret += "\n\n\t-----------------------------------\n\n\t"
        
        return ret
    
    def __repr__(self):
        return self.__str__()
    
    def insert(self, event: Event, idx=-1):
        if not isinstance(event, Event):
            print("ERROR: Event must by of type Event")
            return
        if idx > len(self.events) or idx < -1:
            print("ERROR: Invalid Index")
            return
        elif idx == -1 or idx == len(self.events):
            self.events.append(event)
        else:
            first_half = self.events[:idx]
            second_half = self.events[idx:]
            self.events = first_half + [event] + second_half
    
    def delete(self, idx):
        if idx >= len(self.events) or idx < 0:
            print("ERROR: Invalid Index")
            return
        elif idx == len(self.events) - 1:
            self.events = self.events[:len(self.events)-1]
        else:
            first_half = self.events[:idx]
            second_half = self.events[idx+1:]
            self.events = first_half + second_half
            
    def search_by_id(self, id):
        for ev in self.events:
            if ev.id == id:
                return ev
        print("ERROR: Event not found")
        return None
        
    def list_all(self):
        print(self)