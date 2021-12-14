# Genetic Algorithm
---
## Summary
- Genetic Algorithm은 다음과 같이 동작한다.
1. 초기 염색체의 집합(Population)을 생성한다.
2. 초기 염색체들에 대한 Fitness(적합도)를 계산한다. 그 중 Best Individual을 찾는다.
3. 초기 염색체들로부터 Crossover, Mutate 등의 방법을 통해 자손을 생성한다.
4. 그 자손들의 Fitness를 다시 계산한다.
5. 그 중에 Best Individual을 찾는다.
6. 계산 횟수가 Limit에 도달할 때 까지 반복.

## Pseudo functions
