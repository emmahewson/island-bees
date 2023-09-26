// Toggle reviews to approved. Submits Form to View.
$('.review-toggle').change(function(e) {

    let reviewId = e.target.id;
    let input = document.getElementById(`review-${reviewId}-input`);
    let form = document.getElementById(`review-toggle-form-${reviewId}`);

    if ($(this).is(':checked')) {
        input.value = "True";
    } else {
        input.value = "False";
    }

    form.submit();
});