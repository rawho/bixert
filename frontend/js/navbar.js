const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const mainNavLinks = document.querySelectorAll('.abc');
const sections = document.querySelectorAll('section')
const navLink = document.querySelectorAll(".nav-link");




hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}


navLink.forEach(n => n.addEventListener("click", closeMenu));

function closeMenu() {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}