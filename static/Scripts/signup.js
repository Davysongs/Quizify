/* Because i didnt set placeholder values in forms.py they will be set here using vanilla Javascript
//We start indexing at one because CSRF_token is considered and input field 
*/
//Query All input fields
var form_fields = document.getElementsByTagName('input')
const success = document.getElementById("success")
success.style.display= "none"

const username = form_fields[1]
const email = form_fields[2]
const password1 = form_fields[3]
const password2 =form_fields [4]
username.placeholder='Username..';
email.placeholder='Email..';
password1.placeholder='Enter password...';
password2.placeholder='Re-enter Password...';


for (var field in form_fields){	
    form_fields[field].className += ' form-control'
}
const form = document.getElementById('register-form');
const passwordInput = form.querySelector('input[name="password1"]');
const confirmPasswordInput = form.querySelector('input[name="password2"]');
const emailInput = form.querySelector('input[name="email"]');
const passwordStrength = document.getElementById('password-strength');

form.addEventListener('submit', function (event) {
    let password = passwordInput.value;
    let confirmPassword = confirmPasswordInput.value;
    let email = emailInput.value;
    let errors = [];

    // Check if passwords match
    if (password !== confirmPassword) {
        errors.push("Passwords do not match");
    }

    // Check password strength
    if (password.length < 8) {
        errors.push("Password must be at least 8 characters long");
    }

    // Check if email is valid
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        errors.push("Invalid email format");
    }

    // Display error messages
    if (errors.length > 0) {
        event.preventDefault(); // Prevent form submission
        passwordStrength.innerHTML = errors.join("<br>");
    }
});

// Clear error messages when user interacts with the form
[passwordInput, confirmPasswordInput, emailInput].forEach(input => {
    input.addEventListener('input', function () {
        passwordStrength.innerHTML = '';
    });
});
