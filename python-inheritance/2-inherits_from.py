#!/usr/bin/python3
"""
Check if an object is an instance of a_class or\
one that inherited from a_class, directly or indirectly!
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a_class or\
    one that inherited from a_class, directly or indirectly.
    """
    obj.class = type(obj)
    return issubclass(obj_class, a_class) and obj is not a_class
