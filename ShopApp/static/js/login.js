document.getElementById("password").addEventListener("focus", () => {
  console.log("Password field focused");
  document.getElementById("monkey").src = monkeyPwdGif;
  document.getElementById("hands").style.top = "0";
  document.getElementById("hands").style.opacity = "1";
});

document.getElementById("password").addEventListener("blur", () => {
  console.log("Password field lost focus");
  document.getElementById("monkey").src = monkeyGif;
  document.getElementById("hands").style.top = "40px";
  document.getElementById("hands").style.opacity = "0";
});
