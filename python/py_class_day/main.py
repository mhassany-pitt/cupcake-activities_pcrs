
class Event:    
    """A new calendar event."""

    def __init__(self, start_time, end_time, event_name):
        """ (Event, int, int, str) -> NoneType

        Precondition: 0 <= start_time < end_time <= 23
        
        Initialize a new event that starts at start_time, ends at end_time,
        and is named name.

        >>> e = Event(12, 13, 'Lunch')
        >>> e.start_time
        12
        >>> e.end_time
        13
        >>> e.name
        'Lunch'
        """
        
        self.start_time = start_time
        self.end_time = end_time
        self.name = event_name

    def __str__(self):
        """ (Event) -> str

        Return a string representation of this event.

        >>> e = Event(6, 7, 'Run')
        >>> str(e)
        'Run: from 6 to 7'
        """
        
        return '{0}: from {1} to {2}'.format(self.name, self.start_time,
                                             self.end_time)

class Day:
    """A calendar day and its events."""

    def __init__(self, day, month, year):
        """ (Day, int, str, int) -> NoneType

        Initialize a day on the calendar with day, month and year,
        and no events.

        >>> d = Day(5, 'April', 2014)
        >>> d.day
        5
        >>> d.month
        'April'
        >>> d.year
        2014
        >>> d.events
        []
        """

        # To do: Complete this method body.

    def schedule_event(self, new_event):
        """ (Day, Event) -> NoneType
        
        Schedule new_event on this day, even if it overlaps with
        an existing event. Later we will improve this method.
        
        >>> d = Day(26, 'March', 2014)
        >>> e = event.Event(11, 12, 'Meeting')
        >>> d.schedule_event(e)
        >>> d.events[0] == e
        True
        """

        # To do: Complete this method body.
    
    def __str__(self):
        """ (Day) -> str
    
        Return a string representation of this day.
        
        >>> d = Day(4, 'April', 2014)
        >>> d.schedule_event(event.Event(13, 14, 'Submit last exercise'))
        >>> d.schedule_event(event.Event(19, 23, 'Celebrate end of classes'))
        >>> print(d)
        4 April 2014:
        - Submit last exercise: from 13 to 14
        - Celebrate end of classes: from 19 to 23
        """

        # To do: Complete this method body.