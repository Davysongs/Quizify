const message = document.getElementById("messages")

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting

        // Get input values
        const username = form.querySelector('input[name="username"]').value.trim();
        const password = form.querySelector('input[name="password"]').value.trim();

        // Validate input fields
        if (username === '' || password === '') {
            showError('Please fill in all fields.');
            return;
        }

        // If all validations pass, submit the form
        form.submit();
    });

    function showError(message) {
        const errorMessageElement = document.getElementById('error-message');
        errorMessageElement.textContent = message;
    }
});
