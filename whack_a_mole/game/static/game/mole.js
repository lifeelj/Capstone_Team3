var moleNumber;

// t1, t2는 각각 randTime의 min, max임
var t1 = new Array(600, 660, 1000);
var t2 = new Array(890, 950, 1290);

// 두더지의 width
var width = new Array(128, 128, 256);

var spareRandom = null;
function lognormalRandom(mu, sigma) {
  var val, u, v, s, mul;

  if (spareRandom !== null) {
    val = spareRandom;
    spareRandom = null;
  }
  else {
    do {
      u = Math.random() * 2 - 1;
      v = Math.random() * 2 - 1;

      s = u * u + v * v;
    } while (s === 0 || s >= 1);

    mul = Math.sqrt(-2 * Math.log(s) / s);

    val = u * mul;
    spareRandom = v * mul;
  }

  return Math.pow(2, val * sigma + mu);
}

function moleActive(num) {
  num.classList.add('active');
}
function moleHide(num) {
  num.classList.remove('active');
}
var moleCatch = 0;
let timeUp = false;
var lastPosition_x;
var lastPosition_y;
var x;
var y;
var r;
var time;


function randTime(min, max) {
  return Math.round(Math.random() * (max - min) + min);
}

// 첫 두더지 좌표 생성 함수 (나타나지 않는 임시 좌표)
function firstGeneratePosition() {
  x = Math.random() * 820;
  y = Math.random() * 820;
  lastPosition_x = x;
  lastPosition_y = y;
}

// 새로운 두더지 좌표 생성 함수
function generatePosition() {
  do {
    mu = document.getElementById("mu").value;
    mu = parseInt(mu);
    console.log(mu);
    r = lognormalRandom(mu, 0.4); // parameter: mu(평균), sigma(표준편차)
    var theta = Math.random() * 2 * Math.PI;
    x = lastPosition_x + r * Math.cos(theta);
    y = lastPosition_y + r * Math.sin(theta);
  } while (x < 0 || x > 820 || y < 0 || y > 820); // 지정 범위 밖의 범위에서 좌표가 생성될 경우 좌표를 재생성

  lastPosition_x = x;
  lastPosition_y = y;
}

function showingMole() {
  if (turn === 0) {
    firstGeneratePosition();
    turn++;
    showingMole();
  }
  else {
    time = randTime(t1[0], t2[0]);
    moleNumber = document.getElementById('1');
    generatePosition();
    const mole = document.getElementById('molespace');
    mole.style.width = width[0] + "px";
    mole.style.height = width[0] + "px";
    mole.style.marginLeft = x + "px";
    mole.style.marginTop = y + "px";
    console.log(turn, r, time);
    moleActive(moleNumber);
    moleNumber.addEventListener('click', catchMole);
    moleCatch = setTimeout(seeMOle, time);
    turn++;
  }
}

var BGM = new Audio('./Game_BGM.mp3');
var hitAudio = new Audio('./Jab.mp3');
var startBtn = document.querySelector('.start-btn');
var header = document.querySelector("h1");

startBtn.addEventListener('click', startMole);

var leftTime = document.getElementById("timer");

function startMole() {
  startBtn.removeEventListener('click', startMole);
  startBtn.style.color = '#3d3f43';
  turn = 0;
  getPoint = 0;
  timeUp = false;
  BGM.play();
  showingMole();
  setTimeout(() => {
    timeUp = true;
    modalEvent();
    startBtn.addEventListener('click', startMole);
    startBtn.textContent = '다시 시작';
    startBtn.style.color = '#f2ecff';
    BGM.pause();
    BGM.currentTime = 0;
  }, 30000); // 플레이 시간 설정

  let i = 30; // 타이머 설정
  const work = () => {
    leftTime.innerHTML = i;
    if (i--) setTimeout(work, 1000);
  }
  work();
}

var cntBox = document.querySelector('#count-mole');

// 두더지를 집어넣고 클릭이벤트를 제거
function seeMOle() {
  moleNumber.removeEventListener('click', catchMole);
  moleHide(moleNumber);
  clearTimeout(moleCatch);

  if (!timeUp) {
    showingMole();
  }
}

// 두더지 잡기에 성공 시 실행됨
function catchMole() {
  seeMOle();
  getPoint++;
  hitAudio.play();
  cntBox.innerHTML = getPoint;
}

var endingBackground = document.querySelector('#ending-bg');
var endingBtn = document.getElementById('quit-ending');
var finalEnding = "finalEnding";

endingBtn.addEventListener('click', hideModal);

function modalEvent() {
  let point = getPoint;
  ending.children[0].innerHTML = "<span>수고하셨습니다</span></br>성공률은 &nbsp;&nbsp;<span class='last'>" + Math.round(point / turn * 100) + '</span>% 입니다!';
  endingBtn.innerHTML = "<span>확인</span>";
  ending.classList.add(finalEnding);
  endingBackground.classList.add(finalEnding);
  document.getElementById("score").value = Math.round(point / turn * 100);
}
function hideModal() {
  ending.classList.remove(finalEnding);
  endingBackground.classList.remove(finalEnding);
  document.getElementById("submit").click();
}
