#201724500 심진섭
from Problem import Numeric

def main():
    p = Numeric()
    p.createProblem()
    gradientDescent(p)
    p.describeProblem()
    displaySetting(p)
    p.displayResult()

def gradientDescent(p):
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

def displaySetting(p):
    print()
    print("Search Algorithm : Gradient Descent Hill Climbing")
    print()
    print("Alpha : ", p._alpha, " EPSILON : 10^(-4)")

main()
