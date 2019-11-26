class BMI:
    def __init__(self,myHeight,myWeight,myName):
        self.mH = myHeight
        self.mW = myWeight
        self.mN = myName
    def calBmi(self):
        currentBMI = self.mW / (self.mH * self.mH)
        return currentBMI