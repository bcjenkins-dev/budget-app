class TimeUnit:
    def __init__(self, amt_freq, unit):
        self.amt_freq = amt_freq
        self.unit = unit
    
    # 1 year = 365 days = 12 months = 52 weeks = 4 quarters
    # 1/4 year = 3 months = 1 quarter
    # 1/12 year = 28-31 days = 1 month = 1/3 quarter
    # 1/52 year = 7 days = 1 week 
    # 1/365 year = 1 days
    def getDaily(self):
        pass

    def getWeekly(self):
        pass

    def getMonthly(self):
        pass

    def getQuarterly(self):
        pass

    def getAnnual(self):
        pass

    def getPerPayChk(self):
        pass

    def printUnit(self):
        if self.unit == "d":
            if int(self.amt_freq) > 1:
                unit = "days"
            elif int(self.amt_freq) == 1:
                unit = "day"
        elif self.unit == "w":
            if int(self.amt_freq) > 1:
                unit = "weeks"
            elif int(self.amt_freq) == 1:
                unit = "week"
        elif self.unit == "m":
            if int(self.amt_freq) > 1:
                unit = "months"
            elif int(self.amt_freq) == 1:
                unit = "month"
        elif self.unit == "q":
            if int(self.amt_freq) > 1:
                unit = "quarters"
            elif int(self.amt_freq) == 1:
                unit = "quarter"
        elif self.unit == "y":
            if int(self.amt_freq) > 1:
                unit = "years"
            elif int(self.amt_freq) == 1:
                unit = "year"
        return unit