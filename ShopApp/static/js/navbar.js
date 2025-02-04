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
// sub menu
document.addEventListener("DOMContentLoaded", function () {
  const dropdownToggle = document.getElementById("dropdown-toggle");
  const submenu = document.getElementById("submenu");
  const caretIcon = this.querySelector("#icon");

  dropdownToggle.addEventListener("click", function () {
    submenu.classList.toggle("show");
    caretIcon.classList.toggle("rotate");
  });
});

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
function openCart() {
  // Get the cart container
  var cartContainer = document.querySelector(".cart-container");

  // Toggle the display of the cart container
  if (cartContainer.style.display === "block") {
    cartContainer.style.display = "none";
  } else {
    cartContainer.style.display = "block";
  }
}
document.addEventListener("DOMContentLoaded", function () {
  const menuItems = document.querySelectorAll(".nav-menu .menu-list > li > a");

  menuItems.forEach((item) => {
    if (item.href === window.location.href) {
      item.classList.add("act");
    }
  });
});
