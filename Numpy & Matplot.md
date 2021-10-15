# Numpy & Matplot Library
---
## Numpy(Numerical Python)
### NDArray(N dimensional Array)
```python
import numpy as np
a = np.array([1,2,3]) # 1차원 배열
b = np.array([1,2],[3,4]) # 2차원 배열
c = np.array([1,2,3,4,5], ndmin = 2) # 최소 dimension을 제한한다.
d = np.array([1,2,3], dtype = float) # array type을 내가 직접 정한다.
print(a) # [1 2 3] 출력
a # array([1,2,3]) 출력
```
- Array 내의 원소들은 모두 같은 Type으로 이루어져야만 한다.

### Array Creation
```python
import numpy as np
a = np.arange(5) # 0 1 2 3 4 
b = np.arange(3, 9, 2) # 3 5 7
c = np.zeros(5) # 0. 0. 0. 0. 0., 기본 타입은 float
d = np.ones(5) # 1. 1. 1. 1. 1., 기본 타입은 float
slice = np.linspace(10, 20, 5) # 10. 12.5 15. 17.5 20.
```
- ```arange()```, ```zeros()``` 등의 method를 이용해서도 Array를 Creation 할 수 있다.
- ```linspace(begin, end, count)``` method는 begin부터 end사이를 count번 균등하게 분할 해준다.

### Matrix
```python
import numpy as np
im = np.eye(3) # 3X3의 Identity Matrix를 만들어준다.
im2 = np.eye(3, 4) # 3X4의 Identity Matrix를 만들어준다.
a = np.arange(6)
b = a.reshape(3, 2) # 0 1 2 3 4 5 ==> [0 1] [2 3] [4 5]
print(b[2, 1]) # 5
print(b[:, 1]) # [1 3 5]
print(np.shape(b)) # (3, 2) ==> n x m 을 tuple 형태로 출력해준다.
print(np.size(b)) # 총 원소의 개수를 알려준다.
print(np.ndim(b)) # 현재 Matrix의 Dimesion을 알려준다.
print(np.transpose(b)) # 전치행렬을 구해준다.
c = np.copy(b) # Deep copy 기능을 numpy에서 제공한다.
print(np.ravel(c)) # Array를 다시 1차원 배열로.
```
- ```np.eye()``` method는 Identity Matrix를 Creation 해준다.
- ```reshape()``` method는 원래 있던 Array를 내가 원하는 크기로 재구성해준다.
  - b[2, 1]과 같이 특정 원소에 접근할 수 있으며
  - b[:, 1]과 같이 적으면, 모든 행에 대해 1열만 가져오라는 말이다.
- ```np.ravel()``` method로 Array들을 다시 1차원 배열로 만들 수 있다.

### Mathematical Function
> 아래와 같이 다양한 수학적 연산들을 제공한다.  

- Matrix Function
```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(np.dot(a, b)) # 원래 행렬곱인 Dot product 기능이다.
print(np.inner(a, b)) # 내적에 대한 기능이다.

c = np.array([[1,2], [3,4]])
d = np.array([[-4], [1]])
inv = np.linalg.inv(c) # C의 역행렬을 구해준다.
sol = np.linalg.solve(c, d) # CX = D 일때, X의 행렬을 구해준다.
det = np.linalg.det(c) # determinant C를 구해준다.
eigen = np.linalg.eig(c) # C의 eigenvalue나 eigenvector을 구해준다.
```
- Float Function
```python
import numpy as np
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
b = np.around(a) # 반올림 기능이다.
c = np.floor(a) # 내림 기능이다.
d = np.ceil(a) # 올림 기능이다.
```

### Statistical Function
> 다양한 통계적 함수들 또한 제공된다.  
```python
a = np.array([[3,7,5], [8,4,3], [2,4,9]])
b = np.amin(a, 1) # axis = 1, row 방향으로 최소값을 계산한다. [3 3 2]
c = np.amin(a, 0) # axis = 0, column 방향으로 최소값을 계산한다. [2 4 3]
d = np.amin(a) # 전체의 최소값을 구한다.
e = np.amax(a, 1)
f = np.amax(a, 0)

info = np.array([1,2,3,4])
avg = np.average(info) # 배열 원소들의 평균을 반환한다.
dev = np.std(info) # 배열 원소들의 표준편차를 반환한다.
var = np.var(info) # 배열 원소들의 분산을 반환한다.
```

### Random Numbers
```python
import numpy as np
a = np.random.rand(3, 2)
b = np.random.randint(3, 9, size=(2,4))
print(a) # 3행 2열의 Random Number을 제공해준다.
print(b) # 2행 4열의 3 ~ 9 사이 Random Integer을 제공해준다.
```
- ```np.random.rand(size)``` method는 0과 1사이의 무작위 실수를 size에 맞게 Matrix에 넣어 뽑아내준다.
- ```np.random.randint(begin, end, size)``` method는 begin ~ end 사이의 무작위 정수를 size에 맞는 Matrix에 넣어준다.

## Matplot Library
### Pyplot module
```python
from matplotlib import pyplot as plt

plt.plot([1,2,3], [1,4,9]) # x값과 y값을 각각 대응 
plt.plot([2,3,4], [5,6,7]) # x값과 y값을 각각 대응
plt.xlabel('Sequence') # X축의 이름
plt.ylabel('Time(sec)') # Y축의 이름
plt.title('Experimental result') # 제목
plt.legend(['Mouse', 'Cat']) # 범주
plt.show()
```
- 위와 같이 기본적으로 함수 그래프를 표현할 수 있는 모듈이다.

```python
import numpy as np
import matplotlib.pyplot as plt


```
