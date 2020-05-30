document.onkeydown = checkKey

function checkKey(e) {
  if(!enableInput)
    return;

  e = e || window.event;
  var parameter = '?';
  if (e.keyCode == 37) 
    parameter += 'left=true&'
  else 
    parameter += "left=false&"
  

  if (e.keyCode == 38) 
    parameter += 'front=true&'
  else 
    parameter += "front=false&"
  

  if (e.keyCode == 39) 
    parameter += 'right=true&'
  else 
    parameter += "right=false&"
  


  if (e.keyCode == 40) 
    parameter += 'back=true&'
  else 
    parameter += "back=false&"
  
  if (e.keyCode == 16) 
    parameter += 'gearup=true&'
  else 
    parameter += "gearup=false&"
  

  if (e.keyCode == 17) 
    parameter += 'geardown=true&'
  else 
    parameter += "geardown=false&"
  

  if (e.keyCode == '32')
    parameter += 'stop=true&';
  else
    parameter += 'stop=false&';

  if (e.keyCode == '192')
    parameter += 'reset=true&'
  
  console.log("Key pressed: ", e.keyCode);
  console.log(parameter);

  $.ajax({
    type: "GET",
    url: "/setMotors" + parameter,
    success: (response) => {
      if (/error/i.exec(response))
        document.getElementById("errorDiv").innerHTML =
        `<div class="alert alert-danger alert-dismissible fade show" role="alert">
          ${response}
          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>`;
      else
        document.getElementById("motorStatus").innerText = response;
    },
    fail: () => {
      console.log("Motor AJAX Failed!");
    }
  })
}




document.getElementById('motorSpeedSelect').addEventListener('change', () => {
  console.log(document.getElementById('motorSpeedSelect').value);
  $.get("/setRPM/" + document.getElementById('motorSpeedSelect').value, function (response) {
    if (/error/i.exec(response))
      document.getElementById("errorDiv").innerHTML =
      `<div class="alert alert-danger alert-dismissible fade show" role="alert">
          ${response}
          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>`;
    else{
      console.log(response);
      return;
    }
  });
});