#!/usr/bin/python3
"""
    A base class representing geometry. This is based on the previous base_geometry class.
    It has the area method that raises an exception if not used. Also contains the method
    that validates integers.
"""


class BaseGeometry:
    """A base class representing geometry."""
    
    def area(self):
        """ Public instance method of the area, raises
        an exception if the area isnt used """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating value"""
        if type(value) != int:
            raises TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
