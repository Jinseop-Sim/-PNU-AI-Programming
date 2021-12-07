# First Hill Climbing Pseudo
---
## Summary
- First Hill Climbing의 진행 순서는 아래와 같다.
  1. 랜덤하게 시작 값을 배정한다.
  2. 그 값을 기준으로 그 값에서 빼고 더하고를 해본다(Mutate).
  3. 더 답에 가까운 쪽을 선택해서 현재 값을 바꾼다.
  4. 더 이상 Current보다 좋은게 나오지 않을 경우 Maxima(Minima)로 인정하고 종료한다.

### Pseudo Functions
```python
def firstChoice(Problem Object): # p는 여기서 File에서 받아온 정보를 담고 있는 객체이다.
  i = 0
  Current Object = RandomInit(Problem Object) # 값을 Random Initialize하는 함수를 통해 현재 객체의 값을 랜덤 배정한다.
  Current Value = Evaluate(Current Object, Problem Object) # 현재 객체에 들어있는 배열의 값을 계산해주는 함수.
  while i < LIMIT:
    Success Object = randomMutant(Current Object, Problem Object) # 비교할 배열의 값들을 +DELTA 하거나 -DELTA하여 또 랜덤하게 만들어 준다.
    Success Value = evaluate(Success Object, Problem Object) # 비교할 객체에 들어있는 배열의 값을 계산해준다.
    if Success Value < Current Value:
      Current Object = Success Object # 비교한 값이 답에 더 가까운 값이면 교체한다.
      Current Value = Success Value
      i = 0 # 다시 계산을 처음부터 하므로 0으로 되돌린다.
    else:
      i += 1 # 비교한 값이 더 크다면, 다시 새로 Mutate를 진행해야 하므로, 계산 횟수만 증가시켜준다.
  return Current Object, Current Value
```

### Evaluate Function
```python
def Evaluate(Current Object, Problem Object):
  Expression(계산식) = Problem Object[0] # 이 계산식은 제일 처음 문제를 읽어올 때 이미 저장이 되어 있다.
  Unknown variable = p[1][0] # 미지수 리스트를 받아온다.
  for i in range(len(Unknown variable)):
    Assignment = Unknown variable[i] + '=' + str(Current Object[i]) # 각 리스트에 저장된 x1 = 30, x2 = 50, 이런 식으로 문자열을 만드는 코드이다.
    exec(Assignment) # Exec 코드를 통해서 위에서 받은 문자열을 실행시킨다.
  return eval(Expression) # 문자열에 의해 값이 대입이 되었으므로, 계산식을 실행시킨다.
```

### Radnom Initialize Function
```python
def RandomInit(Problem Object):
Initial array = []
for i in range(len(p[1][0])): # 여기서 p[1][0]은 File에서 읽어온 문제를 읽었던 P 객체의 배열 중 미지수 리스트(5개)이다.
  Initial array.append(random.randint(p[1][1][i], p[1][2][i])) # 여기서 p[1][1][i], p[1][2][i]는 각각 lower bound와 upper bound이다.
return Initial array
```

### Random Mutate Function
```python
def Random Mutate(Current Object, Problem Object):
  i = random.randint(0, len(p[1][0])-1) # 미지수의 갯수 만큼 반복문을 돌려야 하므로 쓴 코드.
  flag = random.randint(0, 1) # flag를 통해서 - Mutate, + Mutate를 정하도록 한다.
  if flag: return Mutate(Current Object, i, DELTA, Problem Object) # 여기서 DELTA는 변이 정도를 나타낸다.
  else: return Mutate(Current Object, i, -DELTA, Problem Object) # 이 문제에서는 0.01로 잡았다.
```

```python
def Mutate(Current Object, i, DELTA, Problem Object)
  Copy Array = Current Object[:] # Slicing을 이용한 Current Object 배열 복사. 
  Lower Bound = Problem Object[1][i] # 배열을 복사하는 이유는 원래 배열을 Mutate 할 수는 없기 때문이다.
  Upper Bound = Problem Object[1][i] # 비교 대상을 만들기 위해 Mutate 하는 것!
  if Lower Bound <= (Copy Array[i] + DELTA) <= Upper Bound:
    Copy Array[i] += DELTA # Mutate를 위해 -DELTA +DELTA 변이.
  return Copy Array # 비교 대상을 Return 해준다.
```
