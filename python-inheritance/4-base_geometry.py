#!/usr/bin/python3
"""
A base class representing geometry.
"""


class BaseGeometry:
    """
    A base class representing geometry.
    """
    
    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: When called, as the area() method\
            is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating value"""
        if type(value) != int:
            raises TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
