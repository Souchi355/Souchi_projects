function cal(){
  function m(mc1,mc2,ms,mr){
    if (mc1=="arc1"){
      var arr=eval(document.getElementById(mc1).value*1.5+"+"+document.getElementById(mc2).value+"+"+document.getElementById(ms).value*2)/4.5
  
      document.getElementById(mr).value=arr.toString().substring(0,5)
    }
    else if (document.getElementById(mc1).value == 0){
      var arr=eval(document.getElementById(mc1).value+"+"+document.getElementById(mc2).value+"+"+document.getElementById(ms).value*2)/3
  
      document.getElementById(mr).value=arr.toString().substring(0,5)
    }
    else if (document.getElementById(mc2).value == 0){
      var arr=eval(document.getElementById(mc1).value+"+"+document.getElementById(mc2).value+"+"+document.getElementById(ms).value*2)/3
  
      document.getElementById(mr).value=arr.toString().substring(0,5)
    }
    else if (document.getElementById(ms).value==0){
      var arr=eval(document.getElementById(mc1).value+"+"+document.getElementById(mc2).value+"+"+document.getElementById(ms).value)/2
  
      document.getElementById(mr).value=arr.toString().substring(0,5)
    }
    else{
      var arr=eval(document.getElementById(mc1).value+"+"+document.getElementById(mc2).value+"+"+document.getElementById(ms).value*2)/4
  
      document.getElementById(mr).value=arr.toString().substring(0,5)
    }
  }
 
 m("arc1","arc2","ars","arr");
 m("frc1","frc2","frs","frr");
 m("enc1","enc2","ens","enr");
 m("hisc1","hisc2","hiss","hisr");
 m("geoc1","geoc2","geos","geor");
 m("isc1","isc2","iss","isr");
 m("madc1","madc2","mads","madr");
 m("mtc1","mtc2","mts","mtr");
 m("phyc1","phyc2","phys","phyr");
 m("tecc1","tecc2","tecs","tecr");
 m("inc1","inc2","ins","inr");
 m("spc1","spc2","sps","spr");
 document.getElementById("gr").value=eval(document.getElementById("arr").value*2+"+"+document.getElementById("frr").value*2+"+"+document.getElementById("enr").value*2+"+"+document.getElementById("hisr").value+"+"+document.getElementById("geor").value+"+"+document.getElementById("isr").value+"+"+document.getElementById("madr").value+"+"+document.getElementById("mtr").value*4+"+"+document.getElementById("phyr").value*3+"+"+document.getElementById("tecr").value*2+"+"+document.getElementById("inr").value*3+"+"+document.getElementById("spr").value)/23
}
function reset() {
  function p(x){
    document.getElementById(x).value=""
  }
  p("arc1")
  p("arc2")
  p("ars")
  p("arr")
  p("frc1")
  p("frc2")
  p("frs")
  p("frr")
  p("enc1")
  p("enc2")
  p("ens")
  p("enr")
  p("hisc1")
  p("hisc2")
  p("hiss")
  p("hisr")
  p("geoc1")
  p("geoc2")
  p("geos")
  p("geor")
  p("isc1")
  p("isc2")
  p("iss")
  p("isr")
  p("madc1")
  p("madc2")
  p("mads")
  p("madr")
  p("mtc1")
  p("mtc2")
  p("mts")
  p("mtr")
  p("phyc1")
  p("phyc2")
  p("phys")
  p("phyr")
  p("tecc1")
  p("tecc2")
  p("tecs")
  p("tecr")
  p("inc1")
  p("inc2")
  p("ins")
  p("inr")
  p("spc1")
  p("spc2")
  p("sps")
  p("spr")
  p("gr")
  
}