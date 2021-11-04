#201724500 심진섭
import random
import math

class Problem:
    def __init__(self):
        print("Hello")

class Numeric(Problem):
    def __init__(self):
        self._NumEval = 0
        self._expression = []
        self._domain = []
        self._LIMIT_STUCK = 100
        self._DELTA = 0.01
        self._solution = []
        self._minimum = 0
        self._alpha = 0.01
        self._EPSILON = 10**(-4)

    def getDelta(self):
        return self._DELTA

    def createProblem(self):
        file = input("Enter the file name of a function : ")
        infile = open(file, 'r')
        p = [line.rstrip() for line in infile]
        expression = p[0]
        domain = []
        unknown = []
        low = []
        up = []

        for i in range(len(p) - 1):
            c = p[i + 1].split(',')
            unknown.append(c[0])
            low.append(float(c[1]))
            up.append(float(c[2]))

        domain.append(unknown)
        domain.append(low)
        domain.append(up)

        self._expression = expression
        self._domain = domain

    def randomInit(self):
        init = []
        for i in range(len(self._domain[1])):
            init.append(random.randint(self._domain[1][i], self._domain[2][i]))
        return init

    def evaluate(self, current):
        global NumEval

        self._NumEval += 1
        expr = self._expression  # p[0] is function expression
        varNames = self._domain[0]  # p[1] is domain: [varNames, low, up]
        for i in range(len(varNames)):
            assignment = varNames[i] + '=' + str(current[i])
            exec(assignment)
        return eval(expr)

    def moving(self, current):
        i = random.randint(0, len(self._domain[0])-1)
        step = self._alpha * self.gradient(i, current)

        return self.gd_mutate(current, i, step)

    def gradient(self, i, current):
        derived_current = current[:]
        derived_current[i] = derived_current[i] + self._EPSILON

        y = self.evaluate(current)
        derived_y = self.evaluate(derived_current)

        gradi = (derived_y - y) / self._EPSILON
        return gradi

    def gd_mutate(self, current, i, step):  ## Mutate i-th of 'current' if legal
        curCopy = current[:]
        l = self._domain[1][i]  # Lower bound of i-th
        u = self._domain[2][i]  # Upper bound of i-th
        if l <= curCopy[i] - step <= u:
            curCopy[i] -= step
        return curCopy

    def randomMutant(self, current):
        i = random.randint(0, len(self._domain[0]) - 1)
        flag = random.randint(0, 1)
        if flag:
            d = self._DELTA
        else:
            d = -self._DELTA
        return self.mutate(current, i, d)  # Return a random successor

    def mutate(self, current, i, d):  ## Mutate i-th of 'current' if legal
        curCopy = current[:]
        l = self._domain[1][i]  # Lower bound of i-th
        u = self._domain[2][i]  # Upper bound of i-th
        if l <= (curCopy[i] + d) <= u:
            curCopy[i] += d
        return curCopy

    def mutants(self, current):
        neighbors = []

        for i in range(len(self._domain[0])):
            neighbors.append((self.mutate(current, i, -self._DELTA)))
            neighbors.append((self.mutate(current, i, self._DELTA)))

        return neighbors

    def describeProblem(self):
        print()
        print("Objective function:")
        print(self._expression)  # Expression
        print("Search space:")
        varNames = self._domain[0]  # p[1] is domain: [VarNames, low, up]
        low = self._domain[1]
        up = self._domain[2]
        for i in range(len(varNames)):
            print(" " + varNames[i] + ":", (low[i], up[i]))

    def displayResult(self):
        print()
        print("Solution found:")
        print(self.coordinate(self._solution))  # Convert list to tuple
        print("Minimum value: {0:,.3f}".format(self._minimum))
        print()
        print("Total number of evaluations: {0:,}".format(self._NumEval))

    def coordinate(self, solution):
        c = [round(value, 3) for value in solution]
        return tuple(c)

class TSP(Problem):
    def __init__(self):
        self._NumEval = 0
        self._LIMIT_STUCK = 100
        self._minimum = 0
        self._numCities = 0
        self._cost = 0
        self._table = []
        self._solution = []
        self._location = []

    def createProblem(self):
        fileName = input("Enter the file name of a TSP: ")
        infile = open(fileName, 'r')
        self._numCities = int(infile.readline())

        line = infile.readline()  # The rest of the lines are locations
        while line != '':
            self._location.append(eval(line))  # Make a tuple and append
            line = infile.readline()
        infile.close()

        self._table = self.calcDistanceTable(self._numCities, self._location)

    def calcDistanceTable(self, numCities, locations):
        table = []
        temp = []
        for i in range(0, numCities):
            for j in range(0, numCities):
                temp.append(math.sqrt((locations[i][0] - locations[j][0]) ** 2 + (locations[i][1] - locations[j][1]) ** 2))
            table.append(temp)
            temp = []

        return table

    def randomInit(self):  # Return a random initial tour
        n = self._numCities
        init = list(range(n))
        random.shuffle(init)
        return init

    def evaluate(self, current):
        global NumEval

        self._NumEval += 1
        self._cost = 0
        table = self._table
        for i in range(len(current) - 2):
            self._cost = self._cost + table[current[i]][current[i + 1]]
        return self._cost

    def mutants(self, current): # Apply inversion
        n = self._numCities
        neighbors = []
        count = 0
        triedPairs = []
        while count <= n:  # Pick two random loci for inversion
            i, j = sorted([random.randrange(n) for _ in range(2)])
            if i < j and [i, j] not in triedPairs:
                triedPairs.append([i, j])
                curCopy = self.inversion(current, i, j)
                count += 1
                neighbors.append(curCopy)
        return neighbors

    def randomMutant(self, current): # Apply inversion
        while True:
            i, j = sorted([random.randrange(self._numCities)
                       for _ in range(2)])
            if i < j:
                curCopy = self.inversion(current, i, j)
                break
        return curCopy

    def inversion(self, current, i, j):  ## Perform inversion
        curCopy = current[:]
        while i < j:
            curCopy[i], curCopy[j] = curCopy[j], curCopy[i]
            i += 1
            j -= 1
        return curCopy

    def describeProblem(self):
        print()
        n = self._numCities
        print("Number of cities:", n)
        print("City locations:")
        locations = self._location
        for i in range(n):
            print("{0:>12}".format(str(locations[i])), end = '')
            if i % 5 == 4:
                print()

    def displayResult(self):
        print()
        print("Best order of visits:")
        self.tenPerRow(self._solution)       # Print 10 cities per row
        print("Minimum tour cost: {0:,}".format(round(self._minimum)))
        print()
        print("Total number of evaluations: {0:,}".format(self._NumEval))

    def tenPerRow(self, solution):
        for i in range(len(solution)):
            print("{0:>5}".format(solution[i]), end='')
            if i % 10 == 9:
                print()
