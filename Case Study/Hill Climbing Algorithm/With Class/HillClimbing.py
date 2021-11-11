#201724500 심진섭
from Setup import *

class HillClimbing(Setup):
    def __init__(self):
        Setup.__init__(self)
        self._LIMIT_STUCK = 100

    def createProblem(self, algo, prob):
        self._algo = algo
        self._prob = prob

    def algorithm(self, p):
        pass
    def displaySetting(self):
        pass

class SteepestAscent(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)

    def displaySetting(self):
        if self._prob == 1:
            print()
            print("Search Algorithm : Steepest-Ascent Hill Climbing")
            print()
            print("Mutation step size : ", self._delta)
        elif self._prob == 2:
            print()
            print("Search Algorithm : Steepest-Ascent Hill Climbing")

    def algorithm(self, p):
         current = p.randomInit()  # 'current' is a list of values
         valueC = p.evaluate(current)
         while True:
             neighbors = p.mutants(current)
             successor, valueS = self.bestOf(neighbors, p)
             if valueS >= valueC:
                 break
             else:
                 current = successor
                 valueC = valueS
         p._solution = current
         p._minimum = valueC

    def bestOf(self, neighbors, p):
        bestValue = p.evaluate(neighbors[0])
        best = neighbors[0]
        for i in range(len(neighbors)):
            if p.evaluate(neighbors[i]) < bestValue:
                bestValue = p.evaluate(neighbors[i])
                best = neighbors[i]
        return best, bestValue

class FirstChoice(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)

    def displaySetting(self):
        if self._prob == 1:
            print()
            print("Search Algorithm : First-Choice Hill Climbing")
            print()
            print("Mutation step size : ", self._delta)
        elif self._prob == 2:
            print()
            print("Search Algorithm : First-Choice Hill Climbing")
    def algorithm(self, p):
        current = p.randomInit()  # 'current' is a list of values
        valueC = p.evaluate(current)
        i = 0
        while i < self._LIMIT_STUCK:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0  # Reset stuck counter
            else:
                i += 1
        p._solution = current
        p._minimum = valueC

class GradientDescent(HillClimbing):
    def __init__(self):
        HillClimbing.__init__(self)

    def displaySetting(self):
        print()
        print("Search Algorithm : Gradient Descent Hill Climbing")
        print()
        print("Update Rate(alpha) : ", self._alpha)

    def algorithm(self, p):
        current = p.randomInit()
        valueC = p.evaluate(current)

        i = 0
        while i < p._LIMIT_STUCK:
            successor = p.moving(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0
            else:
                i += 1
        p._solution = current
        p._minimum = valueC