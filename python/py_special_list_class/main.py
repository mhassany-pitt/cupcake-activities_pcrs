
class SpecialList:
    """A list that can hold a limited number of items."""

    def __init__(self, size):
        """ (SpecialList, int)

        >>> L = SpecialList(10)
        >>> L.size
        10
        >>> L.value_list
        []
        """
        # complete this code


    def push_value(self, new_value):
        """ (SpecialList, object) -> NoneType

        Append new_value to this list, if there is enough space in the list according to its maximum size.  
        If there is insufficient space, new_value should not be added to the list.

        >>> L = SpecialList(10)
        >>> L.push_value(3)
        >>> L.value_list
        [3]
        """
        # complete this code


    def pop_most_recent_value(self):
        """ (SpecialList) -> object

        Precondition: len(self.value_list) != 0

        Return the value added most recently to value_list and remove it from the list.

        >>> L = SpecialList(10)
        >>> L.push_value(3)
        >>> L.push_value(4)
        >>> L.value_list
        [3, 4]
        >>> L.pop_most_recent_value()
        4
        """
        # complete this code

    
    def compare(self, other):
        """ (SpecialList, SpecialList) -> int

        Return 0 if both SpecialList objects have lists that contain the same number of items.
        Return 1 if self's list contains more items than other's list.
        Return -1 if self's list contains fewer items than other's list.
        """
        # complete this code