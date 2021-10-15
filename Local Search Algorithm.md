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
> Local Search Algorithm은 순수 최적화 문제를 해결할 때 매우 유용하며, 
### Stochastic Algorithm

### First 

### Random State Algorithm
