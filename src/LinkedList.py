from Event import Event
import time

class Node:
    def __init__(self, event: Event):
        self.event = event
        self.next = None
        
class LinkedList:
    def __init__(self, head: Event = None):
        self.length = 0
        self.head = Node(head) if head else None
        if self.head:
            self.length += 1
    
    def __len__(self):
        return self.length

    def __str__(self):
        ret = """
        Events shown below:
        
        -----------------------------------
        
        """
        curr_node = self.head
        while curr_node:
            ret += str(curr_node.event)
            ret += "\n\n\t-----------------------------------\n\n\t"
            curr_node = curr_node.next
        return ret
    
    def __repr__(self):
        return self.__str__()
    
    def _insert_at_tail(self, n: Node):
        if not self.head: # if no head, new node becomes head
            self.head = n
            return
        
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        
        curr_node.next = n
        
        return
        
    def _insert_at_idx(self, n: Node, idx):
        curr_node = self.head
        curr_idx = 0
        
        while curr_idx < idx-1:
            curr_node = curr_node.next
            curr_idx += 1
            
        next_node = curr_node.next
        curr_node.next = n
        n.next = next_node
        
        return
    
    def _insert_at_head(self, n: Node):
        old_head = self.head
        self.head = n
        n.next = old_head
    
    def insert(self, event: Event, idx=-1):
        """
        This function inserts creates a node from an event and inserts it in the 
        list. The user can specify an idx to insert at a specific position. If 
        the user does not provide an idx, the node is appeneded to the tail of 
        the list. 
        """
        if idx > len(self) or idx < -1:
            print("ERROR: This index is invalid")
            return
        
        event_node = Node(event)
        
        if idx == -1 or idx == len(self):
            self._insert_at_tail(event_node)
        elif idx == 0:
            self._insert_at_head(event_node)
        else:
            self._insert_at_idx(event_node, idx)
        
        self.length += 1
        return
    
    def _delete_head(self):
        old_head = self.head
        new_head_node = old_head.next
        self.head = new_head_node
        return old_head
        
    
    def _delete_at_idx(self, idx):
        curr_node = self.head
        curr_idx = 0
        
        while curr_idx < idx-1:
            curr_node = curr_node.next
            curr_idx += 1
        
        node_to_delete = curr_node.next
        new_next_node = node_to_delete.next
        curr_node.next = new_next_node
        return node_to_delete
    
        
    
    def delete(self, idx):
        if idx < 0 or idx >= len(self):
            print("ERROR: This index is invalid")
            return
        elif idx == 0:
            deleted_node = self._delete_head()
        else:
            deleted_node = self._delete_at_idx(idx)
        self.length -= 1
        return deleted_node.event
        
    def _insertion_sort(self, head, by):
        # TODO: IMPLEMENT INSERTION SORT FOR LINKED LIST
        pass
    
    def _merge_sort(self, head, by):
        # TODO: IMPLEMENT MERGE SORT FOR LINKED LIST
        pass
    
    def _quick_sort(self, head, by):
        # TODO: IMPLEMENT QUICK SORT FOR LINKED LIST
        pass
    
    def sort_list(self, by, method):
        if method == "insertion":
            self._insertion_sort(self.head, by)
        elif method == "merge":
            self._merge_sort(self.head, by)
        elif method == "quick":
            self._quick_sort(self.head, by)
        else:
            print("ERROR: Invalid sort method")
            return
        return
        

    def _linear_search(self, id):
        start = time.time()
        counter = 1
        curr_node = self.head
        
        while curr_node:
            if curr_node.event.id == id:
                end = time.time()
                print(f"Event {id} found in {counter} attempts ({end-start} seconds)")
                return curr_node.event
            curr_node = curr_node.next
            counter += 1
        
        print("ERROR: Event ID not found")
        return

    # helper, returns node at given index
    def _node_at_idx(self, idx):
        curr_node = self.head
        i = 0

        while curr_node and i < idx:
            curr_node = curr_node.next
            i += 1
        
        return curr_node

    def _binary_search(self, id):
        start = time.time()
        # set left/right indexes
        left_idx = 0
        right_idx = self.length - 1
        counter = 1
        # while loop
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx)//2
            mid_node = self._node_at_idx(mid_idx)

            if mid_node.event.id == id:
                end = time.time()
                print(f"Event {id} found in {counter} attempts ({end-start} seconds")
                return mid_node.event
            elif mid_node.event.id < id:
                left_idx = mid_idx + 1
                counter += 1
            else:
                right_idx = mid_idx - 1
                counter += 1
        # if event not found
        print("ERROR: Event ID not found")
        return
    
    def search_by_id(self, id, method):
        if method == "linear":
            return self._linear_search(id)
        elif method == "binary":
            return self._binary_search(id)
        else:
            print("ERROR: Invalid search method")
            print("Acceptable values: [linear, binary]")
            return
    
    def _detect_conflicts(self):
        start = time.time()
        
        conflicts = []
        known = set()

        # group events by date to reduce number of checks
        event_dates = {}
        my_node = self.head
        while my_node:
            event = my_node.event
            date = event.date
            if date not in event_dates:
                event_dates[date] = []
            event_dates[date].append(event)
            my_node = my_node.next

        for dt in event_dates:
            evs = event_dates[dt]

            # outer loop
            for i in range(len(evs)):
                ev1 = evs[i]
                start1 = ev1.get_start_hour()*60 + ev1.get_start_min()
                end1 = ev1.get_end_hour()*60 + ev1.get_end_min()

                # inner loop
                for j in range(i+1, len(evs)):
                    ev2 = evs[j]
                    start2 = ev2.get_start_hour()*60 + ev2.get_start_min()
                    end2 = ev2.get_end_hour()*60 + ev2.get_end_min()

                    # check overlap
                    if start1 < end2 and start2 < end1:
                        pair = tuple((min(ev1.id, ev2.id), max(ev1.id, ev2.id)))
                        if pair not in known:
                            known.add(pair)
                            conflicts.append((ev1, ev2))
        
        end = time.time()
        print(f"{len(conflicts)} conflicts detected in {end-start} seconds")
        return conflicts
    
    def list_all(self):
        print(self)