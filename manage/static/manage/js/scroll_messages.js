
// Scrolls page back to previous location after reload
// Adapted from https://stackoverflow.com/questions/17642872/refresh-page-and-keep-scroll-position

document.addEventListener("DOMContentLoaded", function(event) { 

    // Stops scroll if originating from a different page
    // Adapted from https://masteringjs.io/tutorials/fundamentals/if-url-contains
    if (document.referrer.indexOf("manage") !== -1) {
        var scrollpos = sessionStorage.getItem('scrollpos');
        if (scrollpos) {
            window.scrollTo({top: scrollpos, left: 0, behavior: "instant"});
            sessionStorage.removeItem('scrollpos');
        }

        // Adds scroll position for message div
        // Only works if no filter is applied - if a filter is applied keeping the scroll position provides a bad UX as the message will disappear
        if (window.location.href.indexOf("?open") == -1) {
            const messageScroll = document.querySelector('#manage-messages')
            var messageScrollpos = sessionStorage.getItem('messageScrollpos')

            if (messageScrollpos) {
                messageScroll.scrollTo({top: messageScrollpos, left: 0, behavior: "instant"});
                sessionStorage.removeItem('messageScrollpos');
            }
        }
    }
});

// Saves scroll position to session before unloading page
window.onbeforeunload = function(e) {

    const messageScroll = document.querySelector('#manage-messages')
    sessionStorage.setItem('scrollpos', window.scrollY);
    sessionStorage.setItem('messageScrollpos', messageScroll.scrollTop);
};