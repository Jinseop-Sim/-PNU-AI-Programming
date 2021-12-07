# Stochastic Hill Climbing
---
## Summary
- Stochastic Hill Climbing은 다음과 같이 동작한다.

## Pseudo Code
### Stochastic Algorithm
```python
def Stochastic(Problem):
  Current = Radnom Initialize()
  Current Value = Evaluate(Current)
  while True:
    Mutants = Make Mutants(Current)
    Success, Success Value = Stochastic Best(Mutants, Problem)
    if Success Value >= Current Value: break
    else:
      Current = Success
      Current Value = Success Value
  return Current, Current Value
```

### Make Mutants
```python
def Make Mutants(Current):
  neighbors = [] # Mutants를 담을 배열
  for i in range(len(Current)): # 미지수의 갯수 만큼
    mutant = mutate(Current, i, DELTA)
    neighbors.append(mutant)
    mutant = mutate(Current, i, -DELTA)
    neighbors.append(mutant)
  return neighbors # Mutants의 결과 배열을 반환.
```

```python
def Mutate(Current, i, DELTA):
  mutant = Current[:]
  Lower Bound = Problem[1][1][i]
  Upper Bound = Problem[1][2][i]
  if Lower Bound <= mutant[i] + DELTA <= Upper Bound
    mutant[i] += DELTA # 배열 내의 값들을 변이를 시켜 Return한다.
  return mutant
```

### Take Best Mutant
```python
def Take Best Mutant(Mutants, Problem):
  Values For Minima = [Evaluate(Individual) for Individual in Mutants]
  Largest = max(Values For Minima) + 1
  Values For Maxima = [Largest - Value for Value in Values For Minima]
  Total = sum(Values For Maxima)
  Random Value = random.uniform(0, total)
  for i in range(len(Values For Maxima)):
    if Random Value <= s: break
    else: s += Values For Maxima[i+1]
  return Mutants[i], Values For Minima[i]
```
