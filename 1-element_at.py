#!/usr/bin/python3

def element_at(my_list, idx):
    """Return element at index idx or None if index is invalid"""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
