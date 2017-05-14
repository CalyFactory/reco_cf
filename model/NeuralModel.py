class NeuralModel:
    weight = 0
    bias = 0

    def __init__(self, weight, bias):
        self.weight = weight 
        self.bias = bias 
    
    def printValue(self):
        print("weight : " + str(self.weight) + " bias : " + str(self.bias))