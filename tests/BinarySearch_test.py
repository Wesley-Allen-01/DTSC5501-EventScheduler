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
ll_srt = ll.sort_list(by="id", method="merge")

def test_generate_data():
    assert(len(arr.events) == n)
    assert(len(ll) == n)

def test_pos_binary_search_by_id():
    sample_event = ll_srt.head.event
    val = ll_srt.search_by_id(sample_event.id, "binary")
    assert(val.id == sample_event.id)

def test_neg_binary_search_by_id():
    val = ll_srt.search_by_id("some fake id", "binary")
    assert(val is None)

    val = ll_srt.search_by_id(-17, "binary")
    assert(val is None)
