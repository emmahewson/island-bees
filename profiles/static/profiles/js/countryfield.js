// Country input styling to display previously selected country
// Adapted from Code Institute's Boutique Ado Walkthrough

let countrySelected = $('#id_default_country').val();

if(!countrySelected) {
    $('#id_default_country').css('color', '#959595');
};
$('#id_default_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#959595');
    } else {
        $(this).css('color', '#140C00');
    }
});