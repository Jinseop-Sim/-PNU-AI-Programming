# Steepest Ascent
---
## Pseudo Functions
```python
def SteepestAscent(Problem Object):
  Current Object = RandomInit(Problem Object)
  Current Value = Evaluate(Current Object, Problem Object)
  while True:
    neighbors = Mutants(Current Object, Problem Object)
    Success Object, Success Value = bestOf(neighbors, Problem Object)
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
