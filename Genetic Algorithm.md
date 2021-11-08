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
- Example : N-Queens(사진첨부)
