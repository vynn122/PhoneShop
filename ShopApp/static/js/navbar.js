const hamburger = document.querySelector(".burger-menu");
const navLinks = document.querySelector(".menu-list");

//  hamburger menu
hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navLinks.classList.toggle("active");
});
function toggleHamburgerMenu() {
  const hamburgerMenu = document.querySelector(".hamburger-menu");
  hamburgerMenu.classList.toggle("active");
}

window.addEventListener("resize", () => {
  const hamburgerMenu = document.querySelector(".hamburger-menu");
  const burgerMenu = document.querySelector(".burger-menu");

  if (window.innerWidth > 800) {
    hamburgerMenu.classList.remove("active");
    burgerMenu.style.display = "none";
    hamburger.classList.remove("active");
    navLinks.classList.remove("active");
  } else {
    burgerMenu.style.display = "block";
  }
});
