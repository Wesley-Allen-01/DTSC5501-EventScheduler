from Event import Event
import time

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
        
        for i in range(1, len(head)):
            key = head[i]
            j = i - 1
            while j >= 0 and getattr(head[j], by) > getattr(key, by):
                head[j + 1] = head[j]
                j -= 1
            head[j + 1] = key
        self.events = head
    
    def _merge_sort(self, head, by):
        
        def _merge(self, left, right, by):
            merged = []
            i = j = 0
    
            while i < len(left) and j < len(right):
                if getattr(left[i], by) <= getattr(right[j], by):
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
    
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
            
        if len(head) <= 1:
            return head

        mid = len(head) // 2
        left = self._merge_sort(head[:mid], by)
        right = self._merge_sort(head[mid:], by)

        return _merge(self, left, right, by)
    
    def _quick_sort(self, head, by):
        
        if len(head) <= 1:
            return head

        pivot = head[len(head)//2]
        left = [x for x in head if getattr(x, by) < getattr(pivot, by)]
        middle = [x for x in head if getattr(x, by) == getattr(pivot, by)]
        right = [x for x in head if getattr(x, by) > getattr(pivot, by)]

        return self._quick_sort(left, by) + middle + self._quick_sort(right, by)
    
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
        start = time.time()
        counter=1
        for ev in self.events:
            if ev.id == id:
                end = time.time()
                tries = counter
                print(f"Event {ev.id} found in {tries} attempts ({end-start} seconds)")
                return ev
            else:
                counter += 1
        print("ERROR: Event not found")
        return None
    
    def _binary_search(self, id):
        start = time.time()
        # get left and right indexes
        left_index = 0
        right_index = len(self.events)-1
        counter = 1
        
        # while loop
        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2

            if self.events[mid_index].id == id:
                end = time.time()
                print(f"Event {id} found in {counter} attempts ({end-start} seconds) ")
                return self.events[mid_index]
            elif id < self.events[mid_index].id:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
            counter += 1
        
        # if event not found
        print("ERROR: Event not found")
        return None
        
    def search_by_id(self, id, method):
        if method == "linear":
            return self._linear_search(id)
        elif method == "binary":
            return self._binary_search(id)
        else:
            print("ERROR: Invalid search method")
            print("Acceptable values: [linear, binary]")
            return
        
    def detect_conflicts(self):
        start = time.time()
        # Sort Events by Date, Time
        ## placeholder until sort methods available
        sorted_events = sorted(
            self.events,
            key = lambda ev: (ev.date, ev.get_start_hour() * 60 + ev.get_start_min()) # minutes since midnight
        )

        conflicts = []
        known = set()

        for i in range(len(sorted_events)):
            ev1=sorted_events[i]
            start1 = int(ev1.get_start_hour() * 60 + ev1.get_start_min())
            end1 = int(ev1.get_end_hour() * 60 + ev1.get_end_min())

            # compare to other events
            for j in range(i+1, len(sorted_events)):
                ev2 = sorted_events[j]
                if ev1.date != ev2.date:  # exit if other event is on different date
                    break

                start2 = int(ev2.get_start_hour() * 60 + ev2.get_start_min())
                end2 = int(ev2.get_end_hour() * 60 + ev2.get_end_min())

                # check for overlap
                if start1 < end2 and start2 < end1:
                    pair_id = tuple(sorted((ev1.id, ev2.id)))
                    if pair_id not in known:
                        known.add(pair_id)
                        conflicts.append((ev1, ev2))
        
        end = time.time()
        print(f"{len(conflicts)} conflicts identified in {end-start} seconds")
        return conflicts
    
    def list_all(self):
        print(self)
