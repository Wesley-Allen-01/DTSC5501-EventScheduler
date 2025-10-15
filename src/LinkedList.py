from Event import Event, compare_event_times
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
        
    def _insertion_sort(self, by):
        # TODO: IMPLEMENT INSERTION SORT FOR LINKED LIST
        if not self.head or not self.head.next:
            return self  

        sorted_list = LinkedList()

        curr = self.head
        while curr:
            next = curr.next
            curr.next = None  

           
            if not sorted_list.head:
                sorted_list.head = Node(curr.event)
                sorted_list.length = 1
            else:
                sorted_curr = sorted_list.head
                prev = None

                while sorted_curr:
                    if by == "time":
                        cmp_result = compare_event_times(curr.event, sorted_curr.event)
                        
                        if cmp_result == 1:
                            break
                    elif by == "id":
                        if curr.event.id < sorted_curr.event.id:
                            break
                    prev = sorted_curr
                    sorted_curr = sorted_curr.next

                new = Node(curr.event)
                if prev is None:  
                    new.next = sorted_list.head
                    sorted_list.head = new
                else:
                    new.next = sorted_curr
                    prev.next = new
                sorted_list.length += 1

            curr = next

        return sorted_list
    
    def _split_list(self):
        """ 
        splits a LL into 2 halves. returns two lists
        
        Note: this function does not modify the internal LL
        """
        mid = self.length // 2
        left = LinkedList()
        right = LinkedList()
        
        curr_node = self.head
        curr_idx = 0
        while curr_idx < mid:
            left.insert(curr_node.event)
            curr_node = curr_node.next
            curr_idx += 1
        
        while curr_node:
            right.insert(curr_node.event)
            curr_node = curr_node.next
            
        return left, right
    
    def _merge_lists(self, l, r, by):
        """
        Given to sorted LLs, merge them to create one sorted list
        """
        merged_list = LinkedList()
        
        l_curr_node = l.head
        r_curr_node = r.head
        
        while l_curr_node and r_curr_node:
            if by == "time":
                if compare_event_times(l_curr_node.event, r_curr_node.event) == 1:
                    merged_list.insert(l_curr_node.event)
                    l_curr_node = l_curr_node.next
                else:
                    merged_list.insert(r_curr_node.event)
                    r_curr_node = r_curr_node.next
            elif by == "id":
                if l_curr_node.event.id < r_curr_node.event.id:
                    merged_list.insert(l_curr_node.event)
                    l_curr_node = l_curr_node.next
                else:
                    merged_list.insert(r_curr_node.event)
                    r_curr_node = r_curr_node.next
        while l_curr_node:
            merged_list.insert(l_curr_node.event)
            l_curr_node = l_curr_node.next
            
        while r_curr_node:
            merged_list.insert(r_curr_node.event)
            r_curr_node = r_curr_node.next
        
        return merged_list

    def _merge_sort(self, by):
        # print(self)
        if self.length <= 1:
            return self
        
        
        left_half, right_half = self._split_list()
        
        left_sorted = left_half._merge_sort(by)
        right_sorted = right_half._merge_sort(by)

        return self._merge_lists(left_sorted, right_sorted, by)
        
    
    def _quick_sort(self, by):
        # TODO: IMPLEMENT QUICK SORT FOR LINKED LIST
        if self.length <= 1:
            return self

        
        pivot_event = self.head.event
        left = LinkedList()
        right = LinkedList()
        equal = LinkedList()
        equal.insert(pivot_event)

        curr = self.head.next
        while curr:
            ev = curr.event
            if by == "time":
                cmp = compare_event_times(ev, pivot_event)
                
                if cmp == 1:
                    left.insert(ev)
                elif cmp == -1:
                    right.insert(ev)
                else:
                    equal.insert(ev)
            elif by == "id":
                if ev.id < pivot_event.id:
                    left.insert(ev)
                elif ev.id > pivot_event.id:
                    right.insert(ev)
                else:
                    equal.insert(ev)
            curr = curr.next

        left_sorted = left._quick_sort(by) if left.length > 1 else left
        right_sorted = right._quick_sort(by) if right.length > 1 else right

        
        merged = LinkedList()

        curr = left_sorted.head
        while curr:
            merged.insert(curr.event)
            curr = curr.next

        curr = equal.head
        while curr:
            merged.insert(curr.event)
            curr = curr.next

        curr = right_sorted.head
        while curr:
            merged.insert(curr.event)
            curr = curr.next

        return merged
    
    def sort_list(self, method, by="time"):
        if by not in ["time", "id"]:
            print("ERROR: Invalid sort by parameter")
            print("Acceptable values: [time, id]")
            return
        
        if method == "insertion":
            sorted_list = self._insertion_sort(by)
        elif method == "merge":
            sorted_list = self._merge_sort(by)
        elif method == "quick":
            sorted_list = self._quick_sort(by)
        else:
            print("ERROR: Invalid sort method")
            return
        return sorted_list


    def _linear_search(self, id):
        start = time.time()
        counter = 1
        curr_node = self.head
        
        while curr_node:
            if curr_node.event.id == id:
                end = time.time()
                print(f"Event {id} found in {counter} attempts ({(end-start):.4f} seconds)")
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
        sorted_self = self.sort_list(method="merge", by="id")
        start = time.time()
        # set left/right indexes
        left_idx = 0
        right_idx = sorted_self.length - 1
        counter = 1
        # while loop
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx)//2
            mid_node = sorted_self._node_at_idx(mid_idx)

            if mid_node.event.id == id:
                end = time.time()
                print(f"Event {id} found in {counter} attempts ({(end-start):.4f} seconds)")
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
