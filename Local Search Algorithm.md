# Local Search Algorithm
---
## Conventional vs AI Algorithm
> 보통 Conventional한 알고리즘은 어떤 문제가 있을 때 최적의 해를 구해내는 Optimization을 추구한다.  
> 하지만 매우 효율적인 알고리즘이 없을 뿐더러, 엄청난 시간을 요구한다.(__Intractable(다루기 힘들다)__)  
> 따라서 효율성이 매우 중요하게 생각되는 지금, AI Algorithm이 필요하다!  

- Example : TSP(Traveling Salesperson Problem)
  - 영업 사원이 각 지점을 돌아다니는데, 최소 비용으로 돌아다니는 최적의 해를 구하는 문제이다.
  - n가지 중 한 도시를 고르고, n-1가지 중 한 도시를 고르고, .., 하나가 남을 때 까지 고른다.
  - 이는 n! 가지의 길을 가지게 되므로, 매우 비효율적이고 시간이 많이 걸리게 된다.
  - __Nearest Neighbor Heuristic__ : 항상 가장 가까운 도시만 들린다. (Heuristic? 발견법, 고민하지 않고 익숙한 것으로 고르는 것.)
    - 가장 가까운 도시만 들르는 경우의 경우의 수는 곱하기가 아닌 더하기로 연결된다. 
    - 따라서 n가지에 대해서 (n-1) + (n-2) + .. + 1 = n^2(n-1)/n <<<< n! ==> 훨씬 가짓 수가 적다!
    - Big O 표기법으로 표현하면, 복잡도는 O(n^3) <<< O(n!) 이 될 것이다.
    - 물론 저비용이지만 최적의 해라고 단정 지을 수는 없다.
- 위의 예시로 말미암아 봤을 때, __AI Algorithm은 Heuristics__ 와 __Radomized Strategies__ 를 이용해, 최적에 가까운 해를 "빠르게" 찾는 것이 핵심이다.

## Local Search Algorithm?
> Local Search Algorithm은 순수 최적화 문제를 해결할 때 매우 유용한 알고리즘이다.  
> Objective Function(목적 함수)에 따라서 최선의 상태를 찾는 알고리즘이며, 결과적으로 Final Goal이 존재하는 알고리즘이 아니다.  
> 그 말인 즉슨, Current Node를 기준으로 Neighbor Node를 확인하여 조금이라도 더 좋은 노드로 이동하는 방식을 채택하며, 빠르게 Best state를 찾는다.  

- Local Algorithm은 Convention Algorithm에 비해 체계적이지 못하다. ==> 우리가 지나온 Node들을 기록하고 유지하지 않는다.
- 그렇기 때문에 아주 적은 메모리만으로 해를 구한다.
- 무한하거나 아주 큰 공간에서 그나마 합리적인 해를 찾아낼 수 있다.
## Hill Climbing Algorithm
> Local Search Algorithm의 대표적인 것들 중 하나인 언덕 등반 알고리즘이다.  
- 일명 __Gradient Ascent(Descent)__ 알고리즘이다.  
![Hill](https://user-images.githubusercontent.com/71700079/137448769-bd56f3a1-7209-4256-9cf0-f306be521bcc.PNG)  
- 위의 그림을 보면 Global Max, Local Max 두 가지의 정상이 존재한다.
  - Global Maximum : 정말 이 문제에서 Conventional Algorithm을 통해 구할 수 있는 최적의 해이다.
  - Local Maximum : 최적의 해는 아니지만 빠르게 구할 수 있는 최선의 해이다.
- __Hill Climbing Algorithm__ 은 주변이 안개로 자욱한 산을 등반하는 것과 같다. 자신의 주변에 올라갈 곳이 있나 없나만 확인한다는 말이다.
- 현재 Node의 Successor(후임자) 중에서 Best State가 현재 Node보다 더 좋다면, Succesor로 이동하는 알고리즘이다.
- 더 이상 자신보다 좋은 Successor이 나오지 않으면 종료한다.
- Example : N-Queens Problem  
  ![N-Queen](https://user-images.githubusercontent.com/71700079/137450491-254adf45-66af-4cd9-9d48-20163753a372.PNG)  
  - Conventional하게 푼다면 BackTracking을 이용해서 Recursion으로 풀어야 하는 유명한 문제이다.
  - 하지만 Hill Climbing Algorithm을 이용해서 다음과 같이 해결한다.  
    1. Queen들은 Column으로만 한 칸씩 움직일 수 있다는 규칙을 만든다.
    2. 하나씩 옮기며 Queen 끼리 충돌이 있는 횟수 h를 기록해나간다.
    3. 그 중 가장 h가 작은 자리에 queen을 위치시킨다.  
 
### Stochastic Hill Climbing
> 하지만, 위에서 얘기했듯이 Hill Climbing Algorithm은 최적의 해를 찾는 것이 아닌, 최선의 해를 찾는 것.  
> 따라서 h(n) = 0 인 경우를 찾아야 하는데, 찾지 못하는 문제가 발생할 수도 있다! (__Greediness__)  
> 그래서 등장하는 것이 아래의 알고리즘들이다.  
- __Stochastic Hill Climbing__ 은 원래 Hill Climbing 보다는 비효율적인 알고리즘이다.
  - 그 이유는, 원래는 Successor의 값 중 그래도 가장 최적의 해를 선택해서 이동했었다.
  - 하지만 __Stochastic Hill Climbing__ 확률에 의존하는 알고리즘이다.
  - 그래서 내 주변의 기울기를 살펴, 기울기가 높은 곳에 높은 확률을 부여하고 기울기가 낮은 곳에 낮은 확률을 부여하며 확률에 따라 이동한다.
  - 확률에 따라 기울기가 낮은 곳으로 이동할 수도 있기 때문에 비효율적인 알고리즘이라고 하는 것이다.
  - 하지만 Hill Climbing 보다는 Local Maximum 값이 더 크게 나오는 경우가 많아 채택한다.

### First-Choice Hill Climbing
- __First Choice Hill Climbing__ 은 그냥 Successor가 가장 좋은 곳으로 이동하는 것이 아닌 Current Node보다 좋기만 하면 즉시 이동한다.
- Stochastic Hill Climbing 보다는 좀 더 운의 요소가 크게 작용하는 Algorithm이다.

### Random State Hill Climbing
- Initial State에 따라 도착하는 Local Maximum이 달라지기 때문에, Radnom하게 Initial State를 부여해보는 것이다.
- 혹시 그 중에 Global Maximum에 도착하는 경우의 수가 생길 수도 있기 때문이다.
- 이 방식 또한 운에 의존하는 방식이라고 볼 수 있겠다.

## Continuous State Spaces
> Gradient Method(Hill Climbing)는 기울기에 따라 값을 Update 했었다.  
> Maximize 일 경우 기울기가 증가하는 쪽으로, Minimize 일 경우 기울기가 감소하는 쪽으로 값을 결정했다.  
- x = x +/- (a X df(x)/dx) ==> df(x)/dx는 __Gradient Vector__, 편미분 값이다.
  - 그 계수인 a는 너무 작아지면 너~무 많은 단계를 거쳐야해서 비효율적이다.
  - 반대로 너무 커지면, __Overshoot__ 이 발생하고 아예 엉뚱한 방향으로 가버릴 수도 있다. (사진 첨부)
  - a 값에 대한 결정은 __Heuristic__ 하게 경험에 의해서 시도를 해본 뒤 결정된다.
  - df(x)/dx가 0이 되면, __Critical Point__ 라고 하게 된다. 이는 Local minimum과 Local maximum등의 변화량이 0인 곳이다.
- Example : Gradient Descent
  - f(w) = w^2+1, f'(w) = 2w, initial value w = 4, step size(a) = 0.1
  - __w = w - af'(w)__ 를 Update 식으로 삼으므로, 처음은 4 - (0.1 x 2 x 4) = 3.2
  - 다음은, 3.2 - (0.1 x 2 x 3.2) = 2.56 ... 이런 식으로 계속 Critical Point가 나올 때 까지 반복한다.
