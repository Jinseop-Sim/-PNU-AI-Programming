#201724500 심진섭
from setup import Setup
import random
import math

class Optimizer(Setup):
    def __init__(self):
        self._numRestart = 0
        self._limitStuck = 100
    def setVariables(self, parameters):
        Setup.setVariables(self, parameters)
        self._pType = parameters['pType']
        self._numExp = parameters['numExp']
        self._numRestart = parameters['numRestart']
    def displaySetting(self):
        pass
    def run(self):
        pass
    def getNumExp(self):
        return self._numExp
    def displayNumExp(self):
        print()
        print('Number of experiments:', self._numExp)

class HillClimbing(Optimizer):
    def __init__(self):
        Optimizer.__init__(self)

    def randomRestart(self, p):
        i = 1
        self.run(p)  # 초기값을 설정하기 위해 self.run(p)을 한번 실행해준다.
        bestSolution = p.getSolution()
        bestMinimum = p.getMinimum()  # First result is current best
        numEval = p.getNumEval()

        while i < self._numRestart:
            self.run(p)
            newSolution = p.getSolution()
            newMinimum = p.getMinimum()
            numEval += p.getNumEval()

            if newMinimum < bestMinimum:
                bestSolution = newSolution
                bestMinimum = newMinimum
            i += 1

        p.storeResult(bestSolution, bestMinimum)

class MetaHeruistics(Optimizer):
    def __init__(self):
        Optimizer.__init__(self)
        self.numSample = 5
    def initTemp(self, p):
        pass
    def displaySetting(self):
        print('Total number of evaluations until termination : ', self._limitEval)
        print()
    def getWhenBestFound(self):
        pass

class SteepestAscent(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)

    def displaySetting(self):
        if self._pType == 1: # Numeric
            print()
            print("Search algorithm: Steepest-Ascent Hill Climbing")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Mutation step size:', self._delta)   # Setup Class에서 초기화한 self._delta변수 사용
            print('Max evaluations with no improvement: ',self._limitStuck, end='')
            print(' iterations')
            print()

        elif self._pType == 2: # TSP
            print()
            print("Search algorithm: Steepest-Ascent Hill Climbing")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Max evaluations with no improvement: ', self._limitStuck, end='')
            print(' iterations')
            print()

    def setVariables(self, aType, pType):
        self._aType = aType
        self._pType = pType

    def run(self, p):
        current = p.randomInit()  # A current candidate solution
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = self.bestOf(neighbors, p)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)

    def bestOf(self, neighbors, p):
        best = neighbors[0]
        bestValue = p.evaluate(best)
        for i in range(1, len(neighbors)):
            newValue = p.evaluate(neighbors[i])
            if newValue < bestValue:
                best = neighbors[i]
                bestValue = newValue
        return best, bestValue

class FirstChoice(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)

    def displaySetting(self):
        if self._pType == 1:  # Numeric
            print()
            print("Search algorithm: First-Choice Hill Climbing")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Mutation step size:', self._delta)  # Setup Class에서 초기화한 self._delta변수 사용
            print('Max evaluations with no improvement: ', self._limitStuck, end='')
            print(' iterations')
            print()

        elif self._pType == 2:  # TSP
            print()
            print("Search algorithm: First-Choice Hill Climbing")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Max evaluations with no improvement: ', self._limitStuck, end='')
            print(' iterations')
            print()

    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        i = 0
        f = open('FC.txt', 'w')
        while i < self._limitStuck:
            f.write(str(valueC) + '\n')
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
        p.storeResult(current, valueC)
        f.close()

class GradientDescent(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)

    def displaySetting(self):
        print()
        print("Search Algorithm: Gradient Descent")
        print()
        print("Update rate:", self._alpha)
        print("Increment for calculating derivatives:", self._dx)

    def run(self, p):
        currentP = p.randomInit()  # Current point
        valueC = p.evaluate(currentP)
        while True:
            nextP = p.takeStep(currentP, valueC)
            valueN = p.evaluate(nextP)
            if valueN >= valueC:
                break
            else:
                currentP = nextP
                valueC = valueN
        p.storeResult(currentP, valueC)

class Stochastic(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)

    def displaySetting(self):
        if self._pType == 1:  # Numeric
            print()
            print("Search algorithm: Stochastic Algorithm")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Mutation step size:', self._delta)  # Setup Class에서 초기화한 self._delta변수 사용
            print('Max evaluations with no improvement: ', self._limitStuck, end='')
            print(' iterations')
            print()

        elif self._pType == 2:  # TSP
            print()
            print("Search algorithm: Stochastic Algorithm")
            print()
            print('Number of random restarts: ', self._numRestart)
            print()
            print('Max evaluations with no improvement: ', self._limitStuck, end='')
            print(' iterations')
            print()

    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = self.stochasticBest(neighbors, p)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)

    def stochasticBest(self, neighbors, p):
        # Smaller valuse are better in the following list
        valuesForMin = [p.evaluate(indiv) for indiv in neighbors]
        largeValue = max(valuesForMin) + 1
        valuesForMax = [largeValue - val for val in valuesForMin]
        # Now, larger values are better
        total = sum(valuesForMax)
        randValue = random.uniform(0, total)
        s = valuesForMax[0]
        for i in range(len(valuesForMax)):
            if randValue <= s: # The one with index i is chosen
                break
            else:
                s += valuesForMax[i+1]
        return neighbors[i], valuesForMin[i]

class SimulatedAnnealing(MetaHeruistics):
    def __init__(self):
        MetaHeruistics.__init__(self)
        self._numSample = 100
        self._whenBest = 0

    def displaySetting(self):
        print()
        print("Search algorithm: Simulated Annealing")
        print()
        print('Number of random restarts: ', self._numRestart)
        print()
        print('Limited Total number of evaluations until termination : ', self._limitEval)
        print()
        print('Number of times executed to get the best value : ', self._whenBest)
        print()
        print("Increment for calculating derivatives: ", self._dx)  # Setup Class에서 초기화한 self._dx변수 사용
        print('Max evaluations with no improvement: {}'.format(self._limitStuck), end='')
        print(' iterations')
        print()

    def run(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)
        temp = self.initTemp(p)
        best, valueBest = current, valueC
        whenBest = i = 1
        f = open('SA.txt', 'w')

        while True:
            f.write(str(valueC) + '\n')
            neighbor = p.randomMutant(current)
            valueN = p.evaluate(neighbor)
            i += 1
            temp = self.tSchedule(temp)

            if temp == 0 or i == self._limitEval:
                break
            dE = valueN - valueC
            if dE < 0:
                current = neighbor
                valueC = valueN
            elif random.uniform(0, 1) < math.exp(-dE / temp):
                current = neighbor
                valueC = valueN
            if valueC < valueBest:
                (best, valueBest) = (current, valueC)
                whenBest = i

        self._whenBest = whenBest
        p.storeResult(best, valueBest)
        f.close()

    def initTemp(self, p): # To set initial acceptance probability to 0.5
        diffs = []
        for i in range(self._numSample):
            c0 = p.randomInit()     # A random point
            v0 = p.evaluate(c0)     # Its value
            c1 = p.randomMutant(c0) # A mutant
            v1 = p.evaluate(c1)     # Its value
            diffs.append(abs(v1 - v0))
        dE = sum(diffs) / self._numSample  # Average value difference
        t = dE / math.log(2)        # exp(–dE/t) = 0.5
        return t

    def getWhenBestFound(self):
        return self._whenBest

    def tSchedule(self, t):
        return t * (1 - (1 / 10**4))