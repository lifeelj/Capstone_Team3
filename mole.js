var moleNumber;
var randomNum;
var preNum;

function randomHole(){
  randomNum = Math.floor(Math.random() * 10);
  if (preNum !== randomNum && randomNum > 0) {
    preNum = randomNum;
    return randomNum;
  }
  return randomHole();
 }

function moleActive(num){
    num.classList.add('active');
}
function moleHide(num){
    num.classList.remove('active');
}
var moleCatch = 0;

function showingMole(){
  if(turn < 10){
    moleNumber = document.getElementById(`${randomHole()}`);
    moleActive(moleNumber);
    moleNumber.addEventListener('click', catchMole);
    moleCatch = setTimeout(seeMOle, 3000);
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
  console.log('qwerqewr');
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
