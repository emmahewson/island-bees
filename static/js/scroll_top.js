// Scroll to top button

let button = document.getElementById("btt-btn");

window.onscroll = function() {scrollFunction()};

button.addEventListener('click', function() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
})

function scrollFunction() {
    console.log(document.documentElement.scrollTop)
    if (document.documentElement.scrollTop > 20) {
        button.style.display = "block"
    } else {
        button.style.display = "none"
    }
}