# Genetic Algorithm(유전 알고리즘)
---
## Genetic Algorithm
> 어떤 개인들의 집단을 통해 시작된다.
- 각 상태들은 Finite Alphabet으로 이루어진 String으로 표현된다. (보통 0과 1)
  - 이는 Chromosome(염색체)라고 칭한다.
- 각 개인은 __Fitness function(적자생존)__ 에 의해서 평가된다.
  - 즉, Fitness score에 의거하여 확률을 부여해 Reproduction 할 개인을 선택하게 된다.
- Local Search Algorithm은 Specific Heuristics를 전혀 사용하지 않았지만
  - Simulated Annealing과 Genetic Algorithm은 __Meta-level Heuristic__ 을 사용한다! ==> __Metaheuristic Algorithm__

## 동작
- Crossover : Chromosome의 특정 구간을 잘라 Pair와 교환한다.
  - 초반에는 Crossover이 랜덤하게 일어나므로, Fitness score의 변동폭이 매우 크다!
  - Crossover이 점점 진행될 수록 Fitness score의 변동폭은 점점 줄어든다.
  - Crossover의 강점은, 확률에 의해 Pair의 높은 Fitness score을 가진 부분끼리 결합을 하게 되는 경우, 최고 점수를 보장한다.
- Mutation : 매우 낮은 확률로 랜덤한 Mutation이 발생할 수 있다.
- Example : N-Queens  
![Genetic N queens](https://user-images.githubusercontent.com/71700079/140737036-20bbd277-7a6f-4c4e-a119-ff15379d84a9.jpg)  

- 부모(Parent)는 __Binary Tournament__ 에 의해 선택된다.
  1. Population에서 2개의 state를 Random하게 선택한다.(__With Replacement__)
  2. 둘 중 Fitness가 더 좋은 쪽을 Winner로 고른다.(동점일 시, Random하게)
  - Uniform Crossover : 각 유전자에서 동전 던지기(Random)를 하여 부모를 선택한다.
    - 이 때, Crossover이 발생하는 평균 횟수는 당연히 길이/2 가 된다. (동전 던지기는 1/2의 확률!)
    - 하지만, 보통 0.5가 아닌 __p = 0.2__ 로 확률을 사용한다.
  - Parent를 선택한 이후에, Crossover은 __Crossover Rate__ 에 따라 발생하는데, 보통 1에 가깝게 본다.(거의 Crossover 된다.)
  - Bit-flip mutation : 각 Bit는 __Mutation Rate__ 에 의해 조그만 돌연변이를 일으킨다.보통 1/길이의 확률로 발생하도록 한다.
