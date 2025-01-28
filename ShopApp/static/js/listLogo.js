const logos = [
  {
    img: "/static/images/listLogo/Apple.png",
    link: "#",
  },
  {
    img: "/static/images/listLogo/SS.png",
    link: "#",
  },
  {
    img: "/static/images/listLogo/Oppo.png",
    link: "#",
  },
  {
    img: "/static/images/listLogo/vivo.png",
    link: "#",
  },
];

const logoContainer = document.querySelector(".list-logo-container .list-logo");
console.log(logoContainer);

if (logoContainer) {
  logoContainer.innerHTML = logos
    .map(
      (logo) => `
      <a href="${logo.link}">
        <img src="${logo.img}" alt="Brand Logo" class="logo" />
      </a>
    `
    )
    .join("");
} else {
  console.error("Logo container not found");
}
