from Event import Event

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
        new_head_node = self.head.next
        self.head = new_head_node
        return
        
    
    def _delete_at_idx(self, idx):
        curr_node = self.head
        curr_idx = 0
        
        while curr_idx < idx-1:
            curr_node = curr_node.next
            curr_idx += 1
        
        new_next_node = curr_node.next.next
        
        curr_node.next = new_next_node
        return
        
    
    def delete(self, idx):
        if idx < 0 or idx >= len(self):
            print("ERROR: This index is invalid")
            return
        elif idx == 0:
            self._delete_head()
        else:
            self._delete_at_idx(idx)
        
        
    def search_by_id(self, id):
        curr_node = self.head
        
        while curr_node:
            if curr_node.event.id == id:
                return curr_node.event
            curr_node = curr_node.next
        
        print("ERROR: Event ID not found")
        return
    
    def list_all(self):
        print(self)