if __name__ == "__main__":
    xTest = open("data/Test/X_test.txt", mode="r")
    yTest = open("data/Test/y_test.txt", mode="r")

    xTestLines = xTest.readlines()
    yTestLines = yTest.readlines()

    newFile = ""

    for i in range(len(xTestLines)):
        thisLine = yTestLines[i].strip("\n")
        data = xTestLines[i].strip("\n").split()
        for j in range(len(data)):
            thisLine += " " + str(j + 1) + ":" + data[j]
        newFile += thisLine + "\n"

    xTest.close()
    yTest.close()

    xTrain = open("data/Train/X_train.txt", mode="r")
    yTrain = open("data/Train/y_train.txt", mode="r")

    xTrainLines = xTrain.readlines()
    yTrainLines = yTrain.readlines()

    for i in range(len(xTrainLines)):
        thisLine = yTrainLines[i].strip("\n")
        data = xTrainLines[i].strip("\n").split()
        for j in range(len(data)):
            thisLine += " " + str(j + 1) + ":" + data[j]
        newFile += thisLine + "\n"

    xTrain.close()
    yTrain.close()

    outputFile = open("result.txt", mode="w")
    outputFile.write(newFile)
    outputFile.close()
