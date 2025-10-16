import pytest
import sys

sys.path.append("../src/")

from LinkedList import LinkedList
from Event import Event


test_event = Event(1, "Meeting", "2023-10-01", "10:00", "11:00", "Conference Room")
ll = LinkedList(test_event)


def test_LL_init():
    assert(len(ll) == 1)


def test_ll_insertion():    
    next_event = Event(2, "Class", "2023-10-01", "11:15", "12:00", "KOBL 231")
    ll.insert(next_event)

    early_event = Event(4, "Conversation", "2023-10-01", "11:05", "11:14", "Virtual")
    ll.insert(early_event, 1)

    new_head_event = Event(5, "Workout", "2023-10-10", "7:00", "8:30", "Rec Center")
    ll.insert(new_head_event, 0)

    tail_insert_event = Event(17, "Manager Meeting", "2023-10-01", "15:30", "16:30", "Home")
    ll.insert(tail_insert_event)
    assert(len(ll) == 5)
    
    
def test_ll_remove():
    ll.delete(0)
    assert(len(ll) == 4)
    

# def test_pos_linear_search_by_id():
#     val = ll.search_by_id(17, "linear")
#     assert(val.id == 17)


# def test_neg_linear_search_by_id():
#     val = ll.search_by_id("some fake id", "linear")
#     assert(val is None)

#     val = ll.search_by_id(-17, "linear")
#     assert(val is None)


# def test_binary_search_by_id():
#     pass


# def test_neg_binary_seach_by_id():
#     pass

