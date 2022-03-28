function screen(x){
  document.getElementById("screen").value +=x
}
function c(){
  document.getElementById("screen").value =""
}
function display(){
  var h=eval(document.getElementById("screen").value)
document.getElementById("screen").value = h
}
