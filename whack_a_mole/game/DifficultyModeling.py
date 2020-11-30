import numpy as np
import random
import math

lastPosition_x = 0
lastPosition_y = 0
r_list = []
t_list = []
catch = []

# 두더지 사이의 거리 r을 인자로 받아 두더지 잡는데 예상되는 시간 T를 return
def fitts_10to20(r):
    return 481.6+88.64*(math.log2(r)-7)

def fitts_30to40(r):
    return 511.71+104*(math.log2(r)-7)

def fitts_50to60(r):
    return 994.89+63.83*(math.log2(r)-8)

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
  x = random.random() * 1400 # 0 ~ 1400 난수 생성
  y = random.random() * 700
  lastPosition_x = x
  lastPosition_y = y


# 새로운 두더지 좌표 생성 함수
def generatePosition():
  global lastPosition_x, lastPosition_y
  r = lognormalRandom(9.2, 0.4) # parameter: mu(평균), sigma(표준편차)
  theta = random.random() * 2 * math.pi
  x = lastPosition_x + r*math.cos(theta)
  y = lastPosition_y + r*math.sin(theta)

  while (x<0 or x>820 or y<0 or y>820): # 지정 범위 밖의 범위에서 좌표가 생성될 경우 좌표를 재생성
   r = lognormalRandom(9.2, 0.4) # parameter: mu(평균), sigma(표준편차)
   theta = random.random() * 2 * math.pi
   x = lastPosition_x + r*math.cos(theta)
   y = lastPosition_y + r*math.sin(theta)

  lastPosition_x = x
  lastPosition_y = y
  
  return r

while(len(r_list) < 10000):
  r_list.append(generatePosition())
  
while(len(t_list) < 10000):
  t_list.append(randTime(660, 950))

# 두더지가 나타나 있는 시간이 잡는데 걸리는 시간보다 크면 잡았다는 의미로 True를 리턴
for i in range(10000):
  catch.append(fitts_30to40(r_list[i]) < t_list[i])

print("거리의 평균(10,000개): ", np.mean(r_list))
print("성공률: ", np.mean(catch))