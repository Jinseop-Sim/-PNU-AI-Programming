# Steepest Ascent
---
## Summary
- Steepest Ascent 알고리즘의 진행은 다음과 같다.
  1. First HC와 같이 첫 값은 랜덤 배정을 받는다.
  2. 이후에 Mutant를 만드는데, 여기가 First HC와는 다르다.
    - First HC는 초기 배열을 복사해서 Mutate를 시킨 후 그 배열과 초기 배열을 비교하는 방식이었다.
    - 하지만 Steepest 방식은 초기 배열을 복사해 여러개의 후보군을 만들어 놓고, 그 후보군 중 가장 작은(큰) 값을 찾아 비교한다.
    - 이 때 Descent라면 작은 값, Ascent라면 큰 값을 반복해서 계속 찾게 될 것이다.
  3. 만든 후보군 중 가장 작은(큰) 후보와 현재의 계산 값을 비교해서 더 작은 쪽으로 미지수들을 정해준다.
  4. 계산을 종료하는 시점은, 비교한 값이 현재 값보다 더 좋지 않으면, 즉 후보군에 현재 값보다 더 Maxima(Minima)에 가까운 값이 없다면 종료한다.

## Pseudo Functions
```python
def SteepestAscent(Problem Object):
  Current Object = RandomInit(Problem Object)
  Current Value = Evaluate(Current Object, Problem Object)
  while True:
    neighbors = Mutants(Current Object, Problem Object)
    Success Object, Success Value = Best Candidate(neighbors, Problem Object)
    if Success Value >= Current Value:
      break
    else:
      Current Object = Success Object
      Current Value = Success Value
  return Current Object, Current Value
```

### Random Initialize
> First Hill Climbing과 동일하게 진행된다.  
```python
def Random Initialize(Problem Object):
  Initial array = []
  for i in range(len(p[1][0])): # 미지수의 갯수 만큼
    Initial array.append(random.randint(p[1][1][i], p[1][2][i])) # Lower Bound, Upper Bound 사이의 랜덤 정수
  return Initial array # 초기 미지수 반환
```

### Random Mutate
```python
def Mutants(Current Object, Problem Object):
  neighbors = [] # 비교 대상이 될 후보군을 저장할 배열
  for i in range(len(p[1][0])):
    neighbors.append((mutate(Current Object, i, -DELTA, Problem Object))) # Mutate를 시킨다.
    neighbors.append((mutate(Current Object, i, DELTA, Problem Object))) # 이 때는 +, - 모두 시켜서 저장한다. 총 미지수의 수 X2 개의 후보
  return neighbors
```

```python
def Mutate(Current Object, i, DELTA, Problem Object): # First HC와 같은 Mutate 방식.
  Copy Array = Current Object[:]
  Lower Bound = Problem Object[1][1][i]
  Upper Bound = Problem Object[1][2][i]
  if Lower Bound <= (Copy Array[i] + DELTA) <= Upper Bound:
    Copy Array[i] += DELTA
  return Copy Array
```
### Find Best Candidate
```python
def Best Candidate(neighbors, Problem Object):
  bestValue = evaluate(neighbors[0], Problem Object)
  best = neighbors[0]
  for i in range(1, len(neighbors)):
    if evaluate(neighbors[i], Problem Object) < bestValue:
      bestValue = evaluate(neighbors[i], Problem Object)
      best = neighbors[i]
  return best, bestValue
```
