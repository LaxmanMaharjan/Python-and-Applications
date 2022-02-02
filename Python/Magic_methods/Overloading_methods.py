class Timespan:
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __len__(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds

    def __repr__(self):
        return 'Timespan(hours=%d, minutes=%d, seconds=%d)' %(self.hours, self.minutes, self.seconds)

print(len(Timespan(3,30,30)))
print(bool(Timespan()))
print(Timespan())
