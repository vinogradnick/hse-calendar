class Schedule:
    def __init__(self, startTime, endTime, number):
        self.startTime = startTime
        self.endTime = endTime
        self.number = number

    def toDict(self):
        return dict(number=self.number, startTime=self.startTime, endTime=self.endTime)

    @staticmethod
    def toSchedule(string):
        if(string == None):
            raise TypeError('string cannot be converted to Schedule')
        spl = string.split('\n\n')
        times = spl[1].split('-')
        return Schedule(times[0], times[1], int(spl[0]))
