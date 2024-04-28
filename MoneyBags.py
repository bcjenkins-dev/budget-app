import TimeUnit as tu
# Money Bags object: 

class MoneyBags:
    def __init__(self, category, amt, freq, freq_unit):
        self.category = category
        self.amount = amt
        self.amt_freq = freq
        self.amt_freq_unit = freq_unit

    def getBag(self):
        tmp_tu = tu.TimeUnit(self.amt_freq, self.amt_freq_unit)
        unit = tmp_tu.printUnit()
        print("You spend $" + str(self.amount) + " on " + self.category + " every " + str(self.amt_freq) + " " + unit)

    def costPerPayChk(self):
        pass