// Hex rating functionality for review form
// Adapted from https://medium.com/geekculture/how-to-build-a-simple-star-rating-system-abcbb5117365 by Simon Ugorji

let hexes = document.getElementsByClassName("rating-hex");

// loop through hexes
for (let i = 0; i < hexes.length; i++) {

    // attach click event for rating select
    hexes[i].addEventListener("click", function() {

        // set hidden input value
        let selectedHex = parseInt(this.getAttribute("data-hex"));
        document.getElementsByClassName("rating-field")[0].value = selectedHex;

        // add selected styling to hexes up to selected
        let pre = selectedHex;
        while(1 <= pre) {

            if(!document.querySelector('.hex-'+pre).classList.contains('rating-hex-selected')) {
                document.querySelector('.hex-'+pre).classList.add('rating-hex-selected');
            }
            --pre;
        }

        // remove selected styling on hexes when selecting a lower rating
        let succ = selectedHex + 1;
        while(5 >= succ) {

            if(document.querySelector('.hex-'+succ).classList.contains('rating-hex-selected')) {
                document.querySelector('.hex-'+succ).classList.remove('rating-hex-selected');
            }
            ++succ;
        }
        
    });
}
