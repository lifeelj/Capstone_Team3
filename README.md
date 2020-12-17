# Capstone_Team 3 : `An Analysis of the Effect of Game Difficulty Control by Age Group Using Fitts' Law` <br>
[&#9989;GO Source Code](https://github.com/lifeelj/Capstone_Team3/tree/master)<br>
[&#9989;GO Final Presentation](https://github.com/lifeelj/Capstone_Team3/blob/main/Final%20presentation%20_%20Team%203.pdf)<br>

Fitts’ Law는 인간-컴퓨터 상호작용과 인간 공학 분야에서 다양하게 연구되고 사용되었다. 본 논문에서는 이를 게임 분야에 적용하여 연령대별 일정한 성공률을 도출할 수 있는 게임 난이도를 결정하고 이러한 연령대별 난이도 조절의 효과를 분석한다.<br>
Fitts’ task와 두더지 게임이라는 두 가지 실험을 설계하여 분석한 결과 연령대가 증가할수록 버튼 클릭에 대한 수행 능력이 뚜렷하게 감소하는 경향성을 발견할 수 있었다. 아울러 이에 대한 실험 결과를 두더지 게임에 적용했을 때, 평균 성공률이 타깃으로 설정한 80%에 근접하게 나오는 것을 확인할 수 있었다. 

## [Problem Statement]
게임의 난이도를 결정하는 데에는 다양한 요인 존재한다. 그 중에서도 버튼 사이의 거리와 크기는 게임의 난이도를 다르게 하는 주요한 원인이 될 수 있다. <br>
다양한 연령대가 게임을 즐길 수 있는 연령대별 게임 난이도 조절 방식이 부재한 현재, 나이대별로 버튼 사이의 거리와 크기를 조절하여 약 80%의 성공률을 낼 수 있는 적정 게임 난이도 설정하고자 한다. 또한 이러한 난이도 조절 방식이 연령대별 게임 난이도 조절의 가이드라인이 될 수 있을지 살펴본다.

## [Design]
**2.1. Fitts’ task <br>**
연령대별로 Fitts’ task 수행에 차이가 있어서 연령대별 Fitts’ law 식을 다르게 구할 수 있다는 가설 아래 Fitts’ task 실험을 설계하였다. Pointing device의 평가 방법의 표준인 ISO 9249-1를 적용하였으며, 이후 두더지 게임 실험에 적용하기 위해 multi-directional 환경으로 설계하였다. 실험 방식은 Fitts’ law 모델 설계 시 7가지 추천사항을 제시한 논문1을 참고하여
ID의 범위를 2.0-4.0으로 정하였으며, 이를 웹으로 배포하여 연령별 실험 데이터를 수집하고자 한다.  이후 나이대별로 Fitts’ law의 parameter를 추정하기 위해 수집한 데이터를 나이대 (10-20대, 30-40대, 50-60대)로 구분하여 선형회귀분석을 적용하여 T = a + b∙ID 로 나타나는 Fitts’ law식에 parameter a와 b를 추정한다. <br>
**2.2. 두더지 게임<br>**
Fitts’ law 모수를 기반으로 난이도를 모델링하여 연령대별 80%의 성공률을 도출할 수 있다는 가설 아래 두더지 게임 실험을 설계하였다. 약 30초간 실험이 진행되며, 두더지 한 마리가 나온 뒤 t1~t2 (난이도 결정 모수의 최솟값과 최댓값) 사이의 랜덤 표시 시간 동안 표시되었다가 사라지면서 다른 두더지가 나오는 방식이다. 허용된 영역 내부를 터치해야 성공으로 인식하며, 연령별로 두더지의 크기(W) 및 두더지가 나타나는 평균 거리(D)에 따라 게임의 난이도를 3단계로 세분화한다. 

## [Implementation]
**3.1. Fitts’ task <br>**
디자인 설계에서 설정한 ID값의 범위와 일치하도록 그림 1과 같이 버튼의 크기를 25, 30, 거리를 100, 150, 200으로 설정하였다. <br>
![1번그림](https://user-images.githubusercontent.com/55980214/102497418-f8132b80-40bb-11eb-8a2e-618c8291a7d5.png) <br>
피실험자가 클릭한 검정색 원 사이의 거리와 시간을 데이터로 측정하였다. 클릭한 위치의 x좌표와 y좌표를 통해 이전 좌표와 거리를 계산하였다. Fitts' Task를 통해 수집한 데이터는 거리와 시간값으로만 존재하기 때문에 이를 ID값인 log₂(2D/W)로 변환하여 변수로 저장하였다. <br>
이후 코드와 같이 각각의 연령대별로 x축과 y축 변수를 선언하여 x축에는 ID값, y축에는 시간값을 입력해주었다. 마지막으로 앞에서 입력한 연령대별 x좌표와 y좌표 변수를 LinearRegression과 fit 메소드를 활용하여 연령대별 Fitts Law의 절편과 기울기를 도출하였다.
 <br>
**3.2. 두더지 게임<br>**
이후 연령대별 Fitts’ Law 식에 맞게 난이도를 결정하는 시뮬레이션을 진행하였다. Fitts Law식에 r값을 대입해서 계산한 시간과 무작위로 결정된 시간을 비교해서 전자가 작으면 두더지를 포획할 수 있고, 전자가 후자보다 크면 두더지를 포획할 수 없다고 가정하였다. <br>
난이도를 결정하는데 사용한 인자로는 두더지가 나타나 있는 시간 t, 두더지 사이의 거리 D, 두더지의 넓이 W 이 세 가지이다. 여기서 W는 10대-40대는 64px, 50대-60대는 128px로 고정하였다. 나머지 t와 D를 시뮬레이션을 토대로 결정하였다. <br>
성공률이 기존에 의도했던 약 80%가 나오도록 모수를 추정하였고 결과적으로 두더지 사이 거리의 평균인 mu값은 8, 표준편차 sigma는 0.3이라는 값이 도출되었다. <br>
하지만 실제로는 두더지가 화면 바깥으로 나갈 경우 다시 두더지의 위치를 조정하여 생성하기 때문에 이러한 부분을 고려하여 시뮬레이션을 통해 mu값을 8.11, sigma를 0.32로 조정하였다. 
<br>
또한, 각각의 연령대에 두더지의 노출 시간의 최솟값과 최댓값을 결정하였다. 10-20대의 경우 580ms-815ms, 30-40대의 경우 620ms-850ms, 50-60대의 경우 860ms-1065ms로 산출되었다. <br>



## [OUR TEAM]
**우리 팀은 3명으로 구성되어 있습니다.&#9996;** <br>

**&#9989;[Gil Eun-ji](https://github.com/EunJiGil)<br>
&#9989;[Kim Sang-hyun](https://github.com/haan823)<br>
&#9989;[Kwon Jun-Taek](https://github.com/lifeelj)<br>**
