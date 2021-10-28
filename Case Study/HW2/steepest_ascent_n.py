#201724500 심진섭
import random
import math

DELTA = 0.01  # Mutation step size
NumEval = 0  # Total number of evaluations


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()  # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)


def createProblem():  ###
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

    return expression, domain


def steepestAscent(p):
    current = randomInit(p)  # 'current' is a list of values
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC


def randomInit(p):
    init = []
    for i in range(len(p[1][0])):
        init.append(random.randint(p[1][1][i], p[1][2][i]))
    return init  # Return a random initial point
    # as a list of values


def evaluate(current, p):
    global NumEval

    NumEval += 1
    expr = p[0]  # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)


def mutants(current, p):
    neighbors = []
    for i in range(len(p[1][0])):
        neighbors.append((mutate(current, i, -DELTA, p)))
        neighbors.append((mutate(current, i, DELTA, p)))
    return neighbors  # Return a set of successors


def mutate(current, i, d, p):  ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]  # [VarNames, low, up]
    l = domain[1][i]  # Lower bound of i-th
    u = domain[2][i]  # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy


def bestOf(neighbors, p):
    bestValue = evaluate(neighbors[0], p)
    best = neighbors[0]
    for i in range(1, len(neighbors)):
        if evaluate(neighbors[i], p) < bestValue:
            bestValue = evaluate(neighbors[i], p)
            best = neighbors[i]
    return best, bestValue


def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])  # Expression
    print("\nSearch space:")
    varNames = p[1][0]  # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i]))


def displaySetting():
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", DELTA)


def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))


def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()
