var moleNumber;
var randomNum;
var preNum;

var spareRandom = null;

function lognormalRandom(mu, sigma)
{
  var val, u, v, s, mul;

  if(spareRandom !== null)
  {
    val = spareRandom;
    spareRandom = null;
  }
  else
  {
    do
    {
      u = Math.random()*2-1;
      v = Math.random()*2-1;

      s = u*u+v*v;
    } while(s === 0 || s >= 1);

    mul = Math.sqrt(-2 * Math.log(s) / s);

    val = u * mul;
    spareRandom = v * mul;
  }

  return Math.exp(val*sigma + mu);
}

function moleActive(num){
    num.classList.add('active');
}
function moleHide(num){
    num.classList.remove('active');
}
var moleCatch = 0;
var lastPosition_x;
var lastPosition_y;
var x;
var y;

// 첫 두더지 좌표 생성 함수
function firstGeneratePosition(){
  x = Math.random() * 920; // 0 ~ 920 난수 생성
  y = Math.random() * 920;
  lastPosition_x = x;
  lastPosition_y = y;
}

// 새로운 두더지 좌표 생성 함수
function generatePosition(){
  do {
  var r = lognormalRandom(7, 1); // parameter: mu(평균), sigma(표준편차)
  var theta = Math.random() * 2 * Math.PI;
  x = lastPosition_x + r*Math.cos(theta);
  y = lastPosition_y + r*Math.sin(theta);
} while (x<0 || x>920 || y<0 || y>920); // 지정 범위 밖의 범위에서 좌표가 생성될 경우 좌표를 재생성

  lastPosition_x = x;
  lastPosition_y = y;
}

function showingMole(){
  if(turn === 0) {
    moleNumber = document.getElementById('1');
    firstGeneratePosition();
    console.log(turn, x, y);
    const mole = document.getElementById('molespace');
    mole.style.marginLeft = x+"px";
    mole.style.marginTop = y+"px";
    moleActive(moleNumber);
    moleNumber.addEventListener('click', catchMole);
    moleCatch = setTimeout(seeMOle, 1000);
    turn++;
  }
  else if(turn < 10){
    moleNumber = document.getElementById('1');
    generatePosition();
    const mole = document.getElementById('molespace');
    mole.style.marginLeft = x+"px";
    mole.style.marginTop = y+"px";
    console.log(turn, x, y);
    moleActive(moleNumber);
    moleNumber.addEventListener('click', catchMole);
    moleCatch = setTimeout(seeMOle, 1000);
    turn++;
  }else{
    modalEvent();
    startBtn.addEventListener('click', startMole);
    startBtn.textContent = 'PRESS AGAIN';
    startBtn.style.color = '#f2ecff';
  }
}

var startBtn = document.querySelector('.start-btn');

startBtn.addEventListener('click', startMole);

function startMole(){
  startBtn.removeEventListener('click', startMole);
  startBtn.style.color = '#3d3f43';
  getPoint = 0;
  turn = 0;
  setTimeout(showingMole, 1000);
}

var cntBox = document.querySelector('#count-mole');
function seeMOle(){
  moleNumber.removeEventListener('click', catchMole);
  moleHide(moleNumber);
  clearTimeout(moleCatch);
  setTimeout(showingMole, 1000);
}

function catchMole(){
  seeMOle();
  clearTimeout(moleCatch);
  getPoint++;
  cntBox.innerHTML = getPoint;
}

var endingBtn = document.querySelector('#ending-bg');
var finalEnding = "finalEnding";

endingBtn.addEventListener('click', hideModal);

function modalEvent(){
  let point = (getPoint / 10) * 100;
  if (point <= 70){
    ending.children[0].innerHTML = "<span>GAME OVER </span></br>YOUR SCORE IS&nbsp;&nbsp;<span class='last'>" + point + '</span>!';
  }else{
    ending.children[0].innerHTML = "<span>YOU WIN</span></br>YOUR SCORE IS&nbsp;&nbsp;<span class='last'>" + point + '</span>!';
  }
  ending.classList.add(finalEnding);
  endingBtn.classList.add(finalEnding);
}
function hideModal(){
  ending.classList.remove(finalEnding);
  endingBtn.classList.remove(finalEnding);
}
