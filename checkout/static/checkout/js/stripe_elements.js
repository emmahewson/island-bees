/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Add the card element & set variables
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#4D4D4D',
        fontFamily: '"Source Sans 3", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#959595',
        }
    },
    invalid: {
        color: '#B25B76',
        iconColor: '#B25B76'
    }
};
var card = elements.create('card', {
    style: style,
    hidePostalCode: true
});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="me-1" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

// Event listener for payment form submit
form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    // Disables the submit button & card input
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);

    // Hides the payment form
    $('#payment-form').fadeToggle(100);

    // Displays the loading animation
    $('#loading-overlay').fadeToggle(100);

    // Passes card details to Stripe
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {

        // if there is an error send error message below input
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="me-1" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);

            // Re-displays the payment form
            $('#payment-form').fadeToggle(100);

            // Hides the loading animation
            $('#loading-overlay').fadeToggle(100);

            // Re-enable the submit button and card input
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);

        // if payment details are valid submit payment form
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});

