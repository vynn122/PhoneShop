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
