document.addEventListener("DOMContentLoaded", function () {
  const primaryHeader = document.querySelector(".primary-header");
  const navToggle = document.querySelector(".mobile-nav-toggle");
  const primaryNav = document.querySelector(".primary-navigation");


  const moon_icon = document.getElementById("icon_moon");

  navToggle.addEventListener("click", () => {
    primaryNav.hasAttribute("data-visible")
      ? navToggle.setAttribute("aria-expanded", false)
      : navToggle.setAttribute("aria-expanded", true);
    primaryNav.toggleAttribute("data-visible");
    primaryHeader.toggleAttribute("data-overlay");
  });

  moon_icon.onclick = function () {
    document.body.classList.toggle("dark-mode");
    if (document.body.classList.contains("dark-mode")) {
      moon_icon.src = "{% static 'images/sun.png' %}";
    } else {
      moon_icon.src = "{% static 'images/moon.png' %}";
    }
  };
});

document.addEventListener("DOMContentLoaded", function () {
  // Your code to create an A11YSlider instance


const slider = new A11YSlider(document.querySelector(".slider"), {
  adaptiveHeight: false,
  dots: true,
  centerMode: true,
  arrows: false,
  responsive: {
    480: {
      dots: false, // dots enabled 1280px and up
    },
  },
});
});

