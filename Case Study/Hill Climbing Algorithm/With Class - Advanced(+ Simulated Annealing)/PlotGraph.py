#201724500 심진섭
import matplotlib.pyplot as plt

f_file = 'FC.txt'
f_infile = open(f_file,'r')

s_file = 'SA.txt'
s_infile = open(s_file,'r')

f_value = [line.rstrip() for line in f_infile] # 라인마다 한 줄씩 읽어오며 value 리스트에 저장한다.
s_value = [line.rstrip() for line in s_infile] # 라인마다 한 줄씩 읽어오며 value 리스트에 저장한다.

for i in range(len(f_value)):
    f_value[i] = round(float(f_value[i]),0)  # string 값인 value를 int값으로 변환하여 리스트에 저장한다.

for i in range(len(s_value)):
    s_value[i] = round(float(s_value[i]),0)  # string 값인 value를 int값으로 변환하여 리스트에 저장한다.

plt.figure()
plt.plot(f_value)
plt.plot(s_value)
plt.xlabel('Evaluations')   # x축의 제목을 설정한다.
plt.ylabel('Cost')               # y축의 제목을 설정한다.
plt.xticks([0,10000,20000,30000,40000,50000]) # x축 단위 바꾸기
plt.title('TSP 100 Perfomance')  # 그래프의 제목을 설정한다.
plt.legend(['First Choice', 'Simulated Annealing'])  # 그래프에서 범례를 설정한다.
plt.show()