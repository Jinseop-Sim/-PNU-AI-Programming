# Stochastic Hill Climbing
---
## Summary
- Stochastic Hill Climbing은 다음과 같이 동작한다.
1. 다른 알고리즘들과 동일하게 초기 값을 배정한다.
2. 여러 Mutants들 중 확률을 부여해서 값을 배정하도록 하기 위해 Mutants 배열을 생성한다.
3. 확률적으로 더 나은 값이 나올 수도 있고 더 안 좋은 값이 나올 수도 있다.
      - 이는 Local Minima(Maxima)에 갇힘을 방지해준다.
4. 뽑은 다음 더 나은 값이면 바꿔주고, 이 과정을 반복하며 더 안좋은 값이 나오면 종료한다.

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
