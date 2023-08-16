alert("Script file loaded and executed.");

// Get the navbar element
const navBar = document.querySelector('.navBar');

// Listen for scroll events
window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
        navBar.classList.add('scrolled');
    } else {
        navBar.classList.remove('scrolled');
    }
});
