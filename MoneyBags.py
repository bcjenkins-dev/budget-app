# Money Bags object: 

class MoneyBags:
    def __init__(self, category, amt, freq, freq_unit):
        self.category = category
        self.amount = amt
        self.amt_freq = freq
        self.amt_freq_unit = freq_unit

    def convertUnit(self):
        if self.amt_freq_unit == "d":
            if int(self.amt_freq) > 1:
                unit = "days"
            elif int(self.amt_freq) == 1:
                unit = "day"
        return unit

    def getBag(self):
        unit = self.convertUnit()
        print("You spend $" + str(self.amount) + " on " + self.category + " every " + str(self.amt_freq) + " " + unit)

    def costPerPayChk(self):
        pass