# Simulated Annealing
---
## Summary
- Simulated Annealing(담금질) 알고리즘은 아래와 같이 진행된다.
1. 다른 알고리즘들과 같이 초기 값을 배정한다.
2. 초기 값을 배정했으면, 초기 온도(나쁜 해를 선택할 확률)를 설정한다.
4. 다른 알고리즘들과 같이 비교 대상(Mutant)를 구한다.
5. 비교 대상 값이 현재 값보다 작으면, 무조건 해를 바꾼다.
6. 비교 대상 값이 현재 값보다 크면, 이전에 구해놓은 온도에 기인하는 확률(볼츠만 상수)에 따라 해가 나쁜 해로 바뀔 수도 있다.
  - 이 과정은 Local minima같은 Critical Point에 빠졌을 때, 탈출할 수 있도록 해준다.
8. 그래서 최종 값을 따로 만들어 놓고, Bad Solution은 저장하지 않도록 해야한다(최소값 구하는 알고리즘).
9. Global Minima가 구해질 때 까지 위의 과정을 반복. 온도도 매번 새로 구한다.
10. 온도가 0이 되거나 계산 횟수가 Limit에 도달하면 종료.

## Pseudo functions
### Simulated Annealing
```python
def Simulated Annealing(Problem Object):
  Current Object = Random Initialize()
  Current Value = Evaluate(Current Object)
  Temperature = Initial Temperature(Problem Object)
  Best, Best Value = Current Object, Current Value
  
  while True:
    Mutant = Random Mutant(Current Object)
    Mutant Value = Evaluate(Mutant)
    Temperature = Calculate Temperature(Temperature)
    i += 1 # 계산 횟수를 제한하기 위한 값
    if Temperature == 0 or i == Limit: break # 온도가 0이거나 계산 횟수가 한계에 도달하면 종료.
    dE = Mutant Value - Current Value
    if dE < 0:
      Current Object = Mutant
      Current Value = Mutant Value
    elif random.uniform(0, 1) < e^(-dE / Temperature):
      Current Object = Mutant
      Current Value = Mutant Value
    if Current Value < Best Value:
      Best, Best Value = Current Object, Current Value
    
    return Best, Best Value
```

### Calculate Temperature
```python
def Initial Temperature(Problem Object):
  Differences = []
  for i in range(Number of Sample):
    a = Random Initial()
    a_v = Evaluate(a)
    b = Random Initial()
    b_v = Evaluate(b)
    Differences.append(abs(b_v - a_v))
  dE = sum(Differences) / Number of Sample # 모든 차이 값의 평균.
  Temperature = dE / log2 # 초기의 exp(-dE/t) = 0.5로 잡기 위함이다.
  return Temperature
```

```python
def Calculate Temperature(Temperature):
  return Temperature * (1 - (1 / 10^4)) # 새로운 온도를 계산하는 함수이다.
```
