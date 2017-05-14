from model.PropensityModel import PropensityModel
from model.UserModel import UserModel
from model.ItemModel import ItemModel
import util

def test1():
    positive = 0
    negative = 0
    for i in range(0, 1000):
        userModel = UserModel(100)
        data = [0.5, 0.4, 0.3, 0.9, 0.1]
        preference = userModel.getPreference(data)

        if preference > 0:
            positive += 1
        else:
            negative += 1
    
    print("positive : " + str(positive))
    print("negative : " + str(negative))

def test2():
    userPropensitySize = 100
    userSize = 100
    itemFeatureSize = 10
    itemSize = 100
    userList = []

    for i in range(0, userSize):
        userList.append(UserModel(userPropensitySize))

def test3():
    itemListSize = 10
    itemList = []

    for i in range(0, itemListSize):
        itemList.append(ItemModel(10))

    print("========================= Euclidean Distance =========================")
    for i in range(0, itemListSize):
        resultString = ""
        for j in range(0, itemListSize):
            resultString += "{:06.2f} ".format(util.getEuclideanDistance(itemList[i].getFeatureList(), itemList[j].getFeatureList()))
        print(resultString)
    print("====================================================================")

    print("========================= Pearson Distance =========================")
    for i in range(0, itemListSize):
        resultString = ""
        for j in range(0, itemListSize):
            resultString += "{:6.2f} ".format(util.getPearsonCofficient(itemList[i].getFeatureList(), itemList[j].getFeatureList()))
        print(resultString)
    print("====================================================================")

def test4():
    itemListSize = 10
    itemList = []

    for i in range(0, itemListSize):
        itemList.append(ItemModel(100))
    
    userListSize = 5
    userList = []
    for i in range(0, userListSize):
        userList.append(UserModel(100))

    print("========================= Item Euclidean Distance =========================")
    for i in range(0, itemListSize):
        resultString = ""
        for j in range(0, itemListSize):
            resultString += "{:06.2f} ".format(util.getEuclideanDistance(itemList[i].getFeatureList(), itemList[j].getFeatureList()))
        print(resultString)
    print("====================================================================")

    print("========================= Item Pearson Distance =========================")
    for i in range(0, itemListSize):
        resultString = ""
        for j in range(0, itemListSize):
            resultString += "{:6.2f} ".format(util.getPearsonCofficient(itemList[i].getFeatureList(), itemList[j].getFeatureList()))
        print(resultString)
    print("====================================================================")

    print("============================ User Response ==========================")
    for i in range(0, userListSize):
        resultString = ""
        for j in range(0, itemListSize):
            result = userList[i].getPreference(itemList[j].getFeatureList())
            resultString += "{:6.2f} ".format(result)
        print(resultString)
    print("====================================================================")




test4()