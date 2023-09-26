// Toggle messages open / closed. Submits Form to View.
$('.message-toggle').change(function(e) {

    let messageId = e.target.id;
    let input = document.getElementById(`message-${messageId}-input`);
    let form = document.getElementById(`message-form-${messageId}`);

    if ($(this).is(':checked')) {
        input.value = "False";
    } else {
        input.value = "True";
    }
    form.submit();
});