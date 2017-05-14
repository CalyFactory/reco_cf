import random 
import util 

class ItemModel:
    itemId = ""
    featureSize = 0
    featureList = []

    def __init__(self, featureSize):
        self.itemId = util.generateRandomString()
        self.featureSize = featureSize
        self.featureList = []
        
        self.generateFeatureRandomly()
    
    def generateFeatureRandomly(self):
        for i in range(0, self.featureSize):
            self.featureList.append(random.randrange(1,100))

        for i in range(0, random.randrange(10,20)):
            self.featureList[random.randrange(0, self.featureSize)] = random.randrange(70,100)
    
    def getFeatureList(self):
        return self.featureList
    
    def getFeatureSize(self):
        return self.featureSize