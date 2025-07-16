class MyCalendar:

    def __init__(self):
        self.calendar = []
        
    def book(self, startTime: int, endTime: int) -> bool:
        i = bisect_left(self.calendar, (startTime, endTime))
        
        
        if i > 0 and self.calendar[i - 1][1] > startTime:
            return False
        
        if i < len(self.calendar) and self.calendar[i][0] < endTime:
            return False
        
        self.calendar.insert(i, (startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)