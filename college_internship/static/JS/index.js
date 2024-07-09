
console.log("ok")
const header = document.querySelector('.header');
const navbar = document.querySelector('.navbar');
const sticky_btn = document.querySelector('.sticky-btn');
const observer = new IntersectionObserver(
(entries)=>{
    const ent = entries[0];
    ent.isIntersecting== false ? navbar.classList.add("sticky")
    : navbar.classList.remove("sticky");
    ent.isIntersecting== false ? sticky_btn.classList.remove("hidden")
    : sticky_btn.classList.add("hidden");

}, {
root : null,
rootMargin : "-60px",
threshold : 0,
});
observer.observe(header);


// popup
// ---- ---- Const ---- ---- //
const cookiesBox = document.querySelector('.wrapper'),
  buttons = document.querySelectorAll('.button');

// ---- ---- Show ---- ---- //
const executeCodes = () => {
  if (document.cookie.includes('AlexGolovanov')) return;
  cookiesBox.classList.add('show');

  // ---- ---- Button ---- ---- //
  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      cookiesBox.classList.remove('show');

      // ---- ---- Time ---- ---- //
      if (button.id == 'acceptBtn') {
        document.cookie =
          'cookieBy= AlexGolovanov; max-age=' + 60 * 60 * 24 * 30;
      }
    });
  });
};

window.addEventListener('load', executeCodes);


// Slider
var swiper = new Swiper(".mySwiper", {
  spaceBetween: 30,
  centeredSlides: true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

// gallery

//popup
      toast = document.querySelector(".toast")
      closeIcon = document.querySelector(".close"),
      progress = document.querySelector(".progress");
      let timer1, timer2;

      window.addEventListener("load", () => {
        toast.classList.add("active");
        progress.classList.add("active");

        timer1 = setTimeout(() => {
            toast.classList.remove("active");
        }, 5000); //1s = 1000 milliseconds

        timer2 = setTimeout(() => {
          progress.classList.remove("active");
        }, 5300);
      });
      
      closeIcon.addEventListener("click", () => {
        toast.classList.remove("active");
        
        setTimeout(() => {
          progress.classList.remove("active");
        }, 300);

        clearTimeout(timer1);
        clearTimeout(timer2);
      });




// gallery
function slidesPlugin(activeSlide = 0) {

  const slides = document.querySelectorAll('.slide')

  slides[activeSlide].classList.add('active')

  for (const slide of slides) {
      slide.addEventListener('click', () => {
      removeActiveClasses()

     slide.classList.add('active')
     })
  }

  function removeActiveClasses() {
      slides.forEach((slide) => {
      slide.classList.remove('active')
      })
  }
}
slidesPlugin();

// const gallery = document.querySelector('.gallery-section');
// const testimonial = document.querySelector('.testimonial');
// const observer2 = new IntersectionObserver(
// (entries)=>{
//     const ent = entries[0];
//     ent.isIntersecting== false ? testimonial.classList.remove("hidden")
//     : testimonial.classList.add("hidden");

// }, {
// root : null,
// rootMargin : "-60px",
// threshold : 0,
// });
// observer2.observe(header);
