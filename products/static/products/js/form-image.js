// Displays message containing image filename after user selection
// Adapted from Code Institute's Boutique Ado Walkthrough

$('.new-image').change(function() {
    var file = $('.new-image')[0].files[0];
    $('#filename').text(`Image will be set to: ${file.name}`);
});