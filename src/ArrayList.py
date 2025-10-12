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
            item_to_delete = self.events[idx]
            self.events = self.events[:len(self.events)-1]
        else:
            item_to_delete = self.events[idx]
            first_half = self.events[:idx]
            second_half = self.events[idx+1:]
            self.events = first_half + second_half
        return item_to_delete
    
    def _insertion_sort(self, head, by):
        # TODO: IMPLEMENT INSERTION SORT FOR ARRAY LIST
        pass
    
    def _merge_sort(self, head, by):
        # TODO: IMPLEMENT MERGE SORT FOR ARRAY LIST
        pass
    
    def _quick_sort(self, head, by):
        # TODO: IMPLEMENT QUICK SORT FOR ARRAY LIST
        pass
    
    def sort_list(self, by, method):
        if method == "insertion":
            self._insertion_sort(self.events, by)
        elif method == "merge":
            self._merge_sort(self.events, by)
        elif method == "quick":
            self._quick_sort(self.events, by)
        else:
            print("ERROR: Invalid sort method")
            return
        return

    def _linear_search(self, id):
        for ev in self.events:
            if ev.id == id:
                return ev
        print("ERROR: Event not found")
        return None
    
    def _binary_search(self, id):
        # TODO: IMPLEMENT BINARY SEARCH FOR ARRAY LIST
        pass
    
    def search_by_id(self, id, method):
        if method == "linear":
            return self._linear_search(id)
        elif method == "binary":
            return self._binary_search(id)
        else:
            print("ERROR: Invalid search method")
            print("Acceptable values: [linear, binary]")
            return
        
    def detect_conflicts(self) -> bool:
        # TODO: IMPLEMENT CONFLICT DETECTION FOR ARRAY LIST
        pass
    
    def list_all(self):
        print(self)