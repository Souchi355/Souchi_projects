function screen(x){
  document.getElementById("screen").value +=x
}
function c(){
  document.getElementById("screen").value =""
}
function display(){
  var s=document.getElementById("screen").value;
    s=s.replace("^2","**2")
    s=s.replace("^","**")
    s=s.replace("÷","/")
    s=s.replace("×","*")
    document.getElementById("screen").value=eval(s)
  var h=eval(document.getElementById("screen").value)
document.getElementById("screen").value = h
}
function del(){
  var f=document.getElementById("screen").value.slice(0, -1);
  document.getElementById("screen").value=f
}
function p(){
  
}
var his=document.getElementById.value
document.getElementById("h").value=his,"\n"