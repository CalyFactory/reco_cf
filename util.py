import string
import random 
import math

def generateRandomString():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))

def getSigmoidResult(x):
    return 1 / (1 + math.exp(x)) - 0.5

def getEuclideanDistance(featureList1, featureList2):
    result = 0

    if(len(featureList1) != len(featureList2)):
        raise Exception("feature size is different")
    
    for i in range(0, len(featureList1)):
        result += math.pow(featureList1[i] - featureList2[i], 2)
    
    return math.sqrt(result)

"""
-1.0 ~ -0.7 : 매우 부정
-0.7 ~ -0.3 : 강한 부정
-0.3 ~ -0.1 : 약한 부정
-0.1 ~ 0.1 : 관계 없음
0.1 ~ 0.3 : 약한 긍정
0.3 ~ 0.7 : 강한 긍정
0.7 ~ 1.0 : 매우 긍정 
"""

def getPearsonCofficient(featureList1, featureList2):
    result1 = 0
    result2 = 0
    result3 = 0
    sumX = 0
    sumY = 0
    sumPowX = 0
    sumPowY = 0
    sumXY = 0
    n = len(featureList1)

    if(len(featureList1) != len(featureList2)):
        raise Exception("feature size is different")
        raise Exception("feature size is different")

    for i in range(0, len(featureList1)):
        result1 += featureList1[i] * featureList2[i]
        result2 += math.fabs(featureList1[i])
        result3 += math.fabs(featureList2[i])

        sumXY += featureList1[i] * featureList2[i]

        sumX += featureList1[i]
        sumY += featureList2[i]

        sumPowX += math.pow(featureList1[i], 2)
        sumPowY += math.pow(featureList2[i], 2)
    
    result1 = (sumXY - sumX * sumY / n)
    result2 = math.sqrt(((sumPowX - math.pow(sumX, 2) / n) * (sumPowY - math.pow(sumY, 2) / n)))
    return result1/result2
