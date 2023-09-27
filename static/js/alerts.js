/**Fade out animation for sign in/out success notifications on index.html */ 
const alertMessages = document.querySelectorAll(".alert-success");
setTimeout(function() {
  alertMessages.forEach(function(alertMessages) {
    alertMessages.style.animation = "fadeout 1s forwards";
  });
  // set fade out to 2 seconds
}, 2000);



