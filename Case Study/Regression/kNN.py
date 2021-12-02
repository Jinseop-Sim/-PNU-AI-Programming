#201724500 심진섭

import numpy as np
def main():
    ml = ML()
    fileName = input("Enter the file name of training data: ")
    ml.setData('train', fileName)
    fileName = input("Enter the file name of test data: ")
    ml.setData('test', fileName)
    ml.buildModel()
    ml.testModel()
    ml.report()


class ML:
    def __init__(self):
        self._trainDX = np.array([])  # Feature value matrix (training data)
        self._trainDy = np.array([])  # Target column (training data)
        self._testDX = np.array([])  # Feature value matrix (test data)
        self._testDy = np.array([])  # Target column (test data)
        self._testPy = np.array([])  # Predicted values for test data
        self._rmse = 0  # Root mean squared error
        self._aType = 0  # Type of learning algoritm
        self._w = np.array([])  # Optimal weights for linear regression
        self._k = 0  # k value for k-NN

    def setData(self, dtype, fileName):  # set class variables
        XArray, yArray = self.createMatrices(fileName)
        if dtype == 'train':
            self._trainDX = XArray
            self._trainDy = yArray
        elif dtype == 'test':
            self._testDX = XArray
            self._testDy = yArray
            self._testPy = np.zeros(np.size(yArray))  # Initialize to all 0

    def createMatrices(self, fileName):  # Read data from file and make arrays
        infile = open(fileName, 'r')
        XSet = []
        ySet = []
        for line in infile:
            data = [float(x) for x in line.split(',')]
            features = data[0:-1]
            target = data[-1]
            XSet.append(features)
            ySet.append(target)
        infile.close()
        XArray = np.array(XSet)
        yArray = np.array(ySet)
        return XArray, yArray

    def buildModel(self):
        print()
        print("Which learning algorithm do you want to use?")
        print(" 1. Linear Regression")
        print(" 2. k-NN")
        aType = int(input("Enter the number: "))
        self._aType = aType
        if aType == 1:
            self._w = self.linearRegression()
        elif aType == 2:
            self._k = int(input("Enter the value for k: "))

    def linearRegression(self):  # Do linear regression and return optimal w
        X = self._trainDX
        n = np.size(self._trainDy)
        X0 = np.ones([n, 1])
        nX = np.hstack((X0, X))  # Add a column of all 1's as the first column
        y = self._trainDy
        t_nX = np.transpose(nX)
        return np.dot(np.dot(np.linalg.inv(np.dot(t_nX, nX)), t_nX), y)

    def testModel(self):
        n = np.size(self._testDy)
        if self._aType == 1:
            self.testLR(n)
        elif self._aType == 2:
            self.testKNN(n)

    def testLR(self, n):  # Test linear regression with the test set
        for i in range(n):
            self._testPy[i] = self.LR(self._testDX[i])

    def LR(self, data):  # Apply linear regression to a test data
        nData = np.insert(data, 0, 1)
        return np.inner(self._w, nData)

    def testKNN(self, n):  # Apply k-NN to the test set
        for i in range(n):
            self._testPy[i] = self.kNN(self._testDX[i])

    ### Implement the following and other necessary methods
    def kNN(self, query):
        near_neighbor = self.findNN(query)
        result = self.takeAvg(near_neighbor)
        return result

    def findNN(self, query):
        m = np.size(self._trainDy)
        k = self._k
        near_neighbor = np.arange(2 * k).reshape(k, 2)
        for i in range(k):
            near_neighbor[i, 0] = i
            near_neighbor[i, 1] = self.sDistance(self._trainDX[i], query)

        for i in range(k, m):
            self.updateNN(near_neighbor, i, query)

        return near_neighbor

    def sDistance(self, a, b):
        limit = np.size(a)
        sq_sum = 0
        for i in range(limit):
            sq_sum += (a[i] - b[i]) ** 2
        return sq_sum

    def updateNN(self, near_neighbor, i, query):
        d = self.sDistance(self._trainDX[i], query)
        for j in range(len(near_neighbor)):
            if near_neighbor[j, 1] > d:
                near_neighbor[j, 0] = i
                near_neighbor[j, 1] = d
                break

    def takeAvg(self, closestK):
        k = self._k
        total = 0
        for i in range(k):
            j = closestK[i, 0]
            total += self._trainDy[j]
        return total / k

    def report(self):
        self.calcRMSE()
        print()
        print("RMSE: ", round(self._rmse, 2))

    def calcRMSE(self):
        n = np.size(self._testDy)  # Number of test data
        totalSe = 0
        for i in range(n):
            se = (self._testDy[i] - self._testPy[i]) ** 2
            totalSe += se
        self._rmse = np.sqrt(totalSe) / n


main()
