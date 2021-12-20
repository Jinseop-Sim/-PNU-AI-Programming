# Gradient Descent
---
## Summary
- 앞서 정리했던 Steepest Ascent와 같은 알고리즘이다.
- 하지만 이번에는 편미분을 이용한 기울기 값을 구해서 코드를 짜 보겠다. 아래와 같이 동작한다.
1. 다른 알고리즘들과 같이 무작위로 초기 미지수 배열을 배정한다.
2. 비교 대상인 변칙 배열을 만들기 위해 기울기를 이용한다.
    - 접선의 기울기를 구하기 위해 미소값 Epsilon을 이용한다.
    - 접선의 기울기를 구한 뒤 임의의 변화량 ALPHA 상수를 곱해 그만큼 Mutate 한다.
3. Mutate한 값이 Minima에 더 가까운 값이면 현재 값을 비교한 값으로 바꾼다.
4. 이 또한 더 이상 더 좋은 값이 나오지 않을 때 까지 Limit 내에서 반복.

## Pseudo functions
### Gradient Descent
```python
def Gradient Descent(Problem Object): # First HC와 유사하게 동작하도록 한다.
  Current Object = Random Initialize()
  Current Value = Evaluate(Current Object)
  i = 0
  while i < Limit(보통 100):
    Success Object = Move(Current Object)
    Success Value = Evaluate(Success Object)
    if Success Value < Current Value:
      Current Object = Success Object
      Current Value = Success Value
      i = 0
    else: i += 1
  return Current Object, Current Value
```

### Move by gradient
```python
def Move(Current Object):
  i = random.randint(0, len(Problem Object[1][0])-1) # 미지수의 갯수 범위 내에서
  Step = ALPHA * Gradient(i, Current Object) # 이 때 Alpha는 다른 알고리즘 에서의 Delta와 같은 변화량 역할이다.
  return Mutate(Current Object, i, Step) # 접선의 기울기 * Alpha 만큼의 Mutate를 시킬 것이다.
```

```python
def Gradient(i, Current Object):
  Copy Array = Current Object[:]
  Copy Array[i] = Copy Array[i] + EPSILON # EPSILON은 기울기를 극한으로 보내서 미분을 시키기 위한 매우 작은 값이다.
  Y Value = Evaluate(Current Object) # 여기서는 10^-4 으로 정한다.
  New Y Value = Evaluate(Copy Array)
  
  Gradient = (New Y Value - Y Value) / EPSILON # 이는 접선의 기울기가 될 것이다.
  return Gradient
```

### Mutate by Gradient
```python
def Mutate(Current Object, i, Step):
  Copy Array = Current Object[:] # Copy를 하는 이유는 Current Object를 바꿔버리면, Current Object와 비교를 못하기 때문!
  Lower Bound = Problem[1][1][i]
  Upper Bound = Problem[1][2][i]
  if Lower Bound <= Copy Array[i] - Step <= Upper Bound:
    Copy Array[i] -= Step
  return Copy Array
```
