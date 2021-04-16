function potatoSugar() {
var mPotato=+document.getElementById("m_Potato").value;
var mSugar=mPotato*8/100;
var vSugar=mSugar*6/100;
var spoon=mSugar*25/100;
document.getElementById("m_Sugar").value=mSugar;
document.getElementById("v_Sugar").value=vSugar;
document.getElementById("s_poon").value=spoon;
}