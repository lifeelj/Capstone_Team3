import numpy as np
import random
import math
from scipy.optimize import fsolve
from sympy import Symbol, solve

lastPosition_x = 0
lastPosition_y = 0
r_list = []
t_list = []
catch = []

# 두더지 사이의 거리 r을 인자로 받아 두더지 잡는데 예상되는 시간 T를 return
def fitts_10to20(r):
    return 216.2+136*(r-5) # width = 64px

def fitts_30to40(r):
    return 226.7+144.9*(r-5) # width = 64px

def fitts_50to60(r):
    return 640+128.9*(r-6) # width = 128px

def lognormalRandom(mu, sigma):
  spareRandom = None
  if(spareRandom != None): 
    val = spareRandom
    spareRandom = None
  
  else:
    u = random.random()*2-1
    v = random.random()*2-1
    s = u*u+v*v
    
    while(s == 0 or s >= 1):
      u = random.random()*2-1
      v = random.random()*2-1
      s = u*u+v*v

    mul = math.sqrt(-2 * math.log(s) / s)
    val = u * mul
    spareRandom = v * mul

  return math.pow(2, val*sigma + mu)

def randTime(min, max):
  return round(random.random() * (max - min) + min)


# 첫 두더지 좌표 생성 함수 (나타나지 않는 임시 좌표)
def firstGeneratePosition():
  global lastPosition_x, lastPosition_y
  x = random.random() * 620
  y = random.random() * 370
  lastPosition_x = x
  lastPosition_y = y


# 새로운 두더지 좌표 생성 함수
def generatePosition():
  global lastPosition_x, lastPosition_y
  r = lognormalRandom(8.11, 0.32) # parameter: mu(평균), sigma(표준편차)
  theta = random.random() * 2 * math.pi
  x = lastPosition_x + r*math.cos(theta)
  y = lastPosition_y + r*math.sin(theta)

  while (x<0 or x>620 or y<0 or y>370): # 지정 범위 밖의 범위에서 좌표가 생성될 경우 좌표를 재생성
   r = lognormalRandom(8.11, 0.32) # parameter: mu(평균), sigma(표준편차)
   theta = random.random() * 2 * math.pi
   x = lastPosition_x + r*math.cos(theta)
   y = lastPosition_y + r*math.sin(theta)

  lastPosition_x = x
  lastPosition_y = y
  
  return math.log2(r)

while(len(r_list) < 100000):
  r_list.append(generatePosition())
  
while(len(t_list) < 100000):
  t_list.append(randTime(860, 1065))
  
# 두더지가 나타나 있는 시간이 잡는데 걸리는 시간보다 크면 잡았다는 의미로 True를 리턴
for i in range(100000):
  catch.append(fitts_50to60(r_list[i]) < t_list[i])

print("거리의 평균(100,000개): ", np.mean(r_list))
print("거리의 표준편차(100,000개) : ", math.sqrt((np.sum(pow((r_list-np.mean(r_list)), 2)))/100000))
print("성공률: ", np.mean(catch))
