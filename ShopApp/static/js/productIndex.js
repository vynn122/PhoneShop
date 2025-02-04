var dynamicWrappers = document.querySelectorAll(".dynamic-wrapper");
dynamicWrappers.forEach((wrapper) => {
  const texts = wrapper.querySelectorAll(".dynamic-text");
  let currentIndex = 0;

  texts[currentIndex].classList.add("visible");
  texts[currentIndex].classList.remove("hidden");

  function changeText() {
    texts[currentIndex].classList.remove("visible");
    texts[currentIndex].classList.add("hidden");

    currentIndex = (currentIndex + 1) % texts.length;

    texts[currentIndex].classList.remove("hidden");
    texts[currentIndex].classList.add("visible");
  }
  setInterval(changeText, 3000);
});
// new
