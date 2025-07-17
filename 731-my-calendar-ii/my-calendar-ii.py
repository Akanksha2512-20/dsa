class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.overlaps:
            if startTime < e and endTime > s:
                # If overlap is found in overlaps list
                return False

        # Check overlaps with existing calendar events
        for s, e in self.calendar:
            if startTime < e and endTime > s:
                # If overlap is found, record this overlap
                self.overlaps.append((max(startTime, s), min(endTime, e)))

        # If no triple booking, then add the event
        self.calendar.append((startTime, endTime))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)