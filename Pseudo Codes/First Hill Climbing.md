# First Hill Climbing Pseudo
---
### Main Function
```python
def firstChoice(p): # p는 여기서 File에서 받아온 정보를 담고 있는 객체이다.
  i = 0
  Current Object = RandomInit(p) # 값을 Random Initialize하는 함수를 통해 현재 객체의 값을 랜덤 배정한다.
  Current Value = Evaluate(Current Object, p) # 현재 객체에 들어있는 배열의 값을 계산해주는 함수.
  while i < LIMIT:
    Success Object = randomMutant(Current Object, p) # 비교할 배열의 값들을 +DELTA 하거나 -DELTA하여 또 랜덤하게 만들어 준다.
    Success Value = evaluate(Success Object, p) # 비교할 객체에 들어있는 배열의 값을 계산해준다.
    if Success Value < Current Value:
      Current Object = Success Object # 비교한 값이 답에 더 가까운 값이면 교체한다.
      Current Value = Success Value
      i = 0 # 다시 계산을 처음부터 하므로 0으로 되돌린다.
    else:
      i += 1 # 비교한 값이 더 크다면, 다시 새로 Mutate를 진행해야 하므로, 계산 횟수만 증가시켜준다.
  return Current Object, Current Value
```
