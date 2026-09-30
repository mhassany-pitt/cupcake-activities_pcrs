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

    def overlaps(self, other):
        """ (Event, Event) -> bool

        Return True iff this event overlaps with event other.

        >>> e1 = Event(6, 7, 'Run')
        >>> e2 = Event(0, 7, 'Sleep')
        >>> e1.overlaps(e2)
        True
        """

        return not (other.end_time <= self.start_time \
                    or other.start_time >= self.end_time)

class Day:
    """A calendar day and its events."""

    def __init__(self, day=1, month='January', year=2014):
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

        self.day = day
        self.month = month
        self.year = year
        self.events = []


    def schedule_event(self, new_event):
        """ (Day, Event) -> bool

        Schedule new_event on this day iff it does not overlap with
        existing events.  Return True iff new_event is scheduled.


        >>> d = Day(3, 'December', 2014)
        >>> e = event.Event(17, 23, 'Celebrate end of classes')
        >>> d.schedule_event(e)
        True
        >>> d.events[0] == e
        True        
        """

        for existing_event in self.events:
            if existing_event.overlaps(new_event):
                return False

        self.events.append(new_event)
        return True
    
    
    def schedule_multiple_events(self, event_list):
        """ (Day, list of Event) -> int
        
        Return the number of events in event_list that were successfully 
        scheduled on this day, without overlapping with existing events.
        
        >>> d = Day(5, 'December', 2015)
        >>> e1 = Event(12, 16, 'Studying')
        >>> d.schedule_event(e1)
        True
        >>> e2 = Event(17, 19, 'Dinner with A')
        >>> e3 = Event(11, 13, 'Lunch with B')
        >>> e4 = Event(9, 10, 'Gym')
        >>> d.schedule_multiple_events([e2, e3, e4])
        2
        """
