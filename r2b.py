class BMI:
    def __init__(self,myHeight,myWeight,myName):
        self.mH = myHeight
        self.mW = myWeight
        self.mN = myName
    def calBmi(self):
        currentBMI = self.mW / (self.mH * self.mH)
        return currentBMI
with open('C:/Users\T05-17\PycharmProjects\Revision2\listOfNames.txt') as f:
    myArray = f.readlines()
    print(myArray)

totalBMI = 0
noOfName = 0
for line in myArray:
    myList = line.split()
    myName = myList[0]
    myHeight = float(myList[1])
    myWeight = int(myList[2])
    person = BMI(myHeight,myWeight,myName)
    currentBMI = person.calBmi()
    print(myName,'has a bmi of',round(currentBMI,2))
    noOfName +=1
    totalBMI +=currentBMI
averageBMI = totalBMI / noOfName
print('Average bmi is',round(averageBMI,2))