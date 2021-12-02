# Linear Regression
---
## Linear Regression(선형 회귀)
> 데이터의 분포를 선형의 그래프에 근사 시켜 Regression을 진행하는 방식.  
> 주어진 데이터를 가지고 근사한 예측 모형을 모델링할 때 사용한다.  

``` y = h(x) = wx + b ```
- 독립 변수 x에 곱해지는 w를 가중치(weight), 더해지는 b를 편향(bias)라고 한다.

## Univariate Linear Regression
``` y = h(x) = wx + b ```
- 위 식에 대해서 w와 b를 구하는 방식이다.
- 구하는 원리는 ```SUM((y(주어진 Data) - (wx+b(우리가 세운 Linear)))^2)```가 최소가 되는 가중치(weight)를 찾는 것!
  - 앞서 계산한 방식들과 동일하게 편미분을 이용한다.

## Multivariate Linear Regression
``` y = h(x(j)) = w inner product x(j) = ```
- Univariate와는 다르게 Multivariate가 되면서 선형 식이 아닌 행렬로 주어진다.

## Nearest Neighbor Models
> __Query Xq__ 가 주어질 때, k Nearest Neghbors(NN) (k, Xq)를 찾는 방식으로  
> 가장 간단한 기계 학습 방식이다(게으른 학습).  

- Regression : NN(k, Xq)의 중간 값이나 NN(k, Xq)의 선형 회귀 값을 구한다.
- Classification : 가장 가까운 데이터들의 종류가 어떤 것이냐에 따라 데이터의 종류를 결정한다.
  - 여기서 k의 값은 검사할 데이터들의 범위가 된다.
