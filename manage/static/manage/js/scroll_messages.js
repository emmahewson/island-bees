
// Scrolls page back to previous location after reload
// Adapted from https://stackoverflow.com/questions/17642872/refresh-page-and-keep-scroll-position

document.addEventListener("DOMContentLoaded", function(event) { 

    // Stops scroll if originating from a different page
    // Adapted from https://masteringjs.io/tutorials/fundamentals/if-url-contains
    if (document.referrer.indexOf("manage") !== -1 ) {
        var scrollpos = sessionStorage.getItem('scrollpos');
        if (scrollpos) {
            window.scrollTo({top: scrollpos, left: 0, behavior: "instant"});
            sessionStorage.removeItem('scrollpos');
        }
    }
});

// Saves scroll position to session before unloading page
window.onbeforeunload = function(e) {
    sessionStorage.setItem('scrollpos', window.scrollY);
};