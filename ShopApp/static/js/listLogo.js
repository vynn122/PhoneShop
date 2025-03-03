const logos = [
  {
    img: "/static/images/listLogo/Apple.png",
    link: "Apple",
  },
  {
    img: "/static/images/listLogo/SS.png",
    link: "Samsung",
  },
  {
    img: "/static/images/listLogo/Oppo.png",
    link: "Oppo",
  },
  {
    img: "/static/images/listLogo/vivo.png",
    link: "Vivo",
  },
];

const logoContainer = document.querySelector(".list-logo-container .list-logo");

logoContainer.innerHTML = logos
  .map(
    (logo) => `
      <a href="${logo.link}">
        <img src="${logo.img}" alt="Brand Logo" class="logo" />
      </a>
    `
  )
  .join("");
