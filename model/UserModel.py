import random
from model.PropensityModel import PropensityModel
import util

class UserModel:
    userId = ""
    propensitySize = 0
    propensityList = []

    def __init__(self, propensitySize):
        self.userId = util.generateRandomString()
        self.propensitySize = propensitySize
        self.propensityList = []

        self.generatePropensityRandomly()
    
    def generatePropensityRandomly(self):
        for i in range(0, self.propensitySize):
            weight = random.random() - 0.5
            bias = random.random() - 0.5
            self.propensityList.append(PropensityModel(weight, bias))

        for i in range(0, random.randrange(10,20)):
            self.propensityList[random.randrange(0, self.propensitySize)].weight = random.random() / 2
            self.propensityList[random.randrange(0, self.propensitySize)].bias = random.random() / 2 
        
        for i in range(0, random.randrange(10,20)):
            self.propensityList[random.randrange(0, self.propensitySize)].weight = - (random.random() / 2 )
            self.propensityList[random.randrange(0, self.propensitySize)].bias = - (random.random() / 2 )
    
    def getPreference(self, featureList):
        layer = [0] * self.propensitySize
        preference = 0
        for k in range(0, self.propensitySize):
            for i in range(0, len(featureList)):
                layer[k] = util.getSigmoidResult(
                    layer[k] + self.propensityList[k].getCalculateOutput(featureList[i])
                )
#            print(layer[k])
            preference += layer[k]
        
        return (preference)

    def getPropensitySize(self):
        return self.propensitySize
    
    def printValue(self):
        print("===============================")
        print("userId : " + self.userId)
        print("propensitySize : " + str(self.propensitySize))
        for i in range(0, self.propensitySize):
            self.propensityList[i].printValue()
