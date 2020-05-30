var enableInput=false;
function controlFocus(focus){
  console.log("Focus: ", focus);
  var box = document.getElementById('motorControlBox');
  if(focus=='on'){
    box.classList.add('table-success');
    box.classList.add('text-white');
    enableInput = true;
  }
  else{
    box.classList.remove('table-success');
    box.classList.remove('text-white');
    enableInput = false;
  }
}
