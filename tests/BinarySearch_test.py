import pytest
import sys

sys.path.append("../src/")

from LinkedList import LinkedList
from ArrayList import ArrayList
from Event import Event
from GenerateData import create_event_dataset

# sample datasets
n = 10000
arr = create_event_dataset(n, "array")
ll = create_event_dataset(n, "ll")

def test_generate_data():
    assert(len(arr.events) == n)
    assert(len(ll) == n)

def test_pos_binary_search_by_id():
    val = ll.search_by_id(6784, "binary")
    assert(val.id == 6784)

def test_neg_binary_search_by_id():
    val = ll.search_by_id("some fake id", "binary")
    assert(val is None)

    val = ll.search_by_id(-17, "binary")
    assert(val is None)
