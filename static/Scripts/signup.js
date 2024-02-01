/* Because i didnt set placeholder values in forms.py they will be set here using vanilla Javascript
//We start indexing at one because CSRF_token is considered and input field 
*/
//Query All input fields
var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder='Username..';
form_fields[2].placeholder='Email..';
form_fields[3].placeholder='Enter password...';
form_fields[4].placeholder='Re-enter Password...';


for (var field in form_fields){	
    form_fields[field].className += ' form-control'
}




// const form = document.querySelector(".form");


// const namePattern = /^[a-zA-Z ]{3,}$/;
// const passwordPattern = /^[a-zA-Z0-9]{8,}$/;
// const emailPattern = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;

// let errorTest = [];
// let error;
// let userExist;


// let pattern;


// function liveFeedBack(e) {

//     function displayBorder() {
//         let small = e.target.parentNode.querySelector('.form__group-small');
//         small.textContent = pattern.test(e.target.value) ? "Valid" : "Invalid";
       
//         if(pattern.test(e.target.value)){
//             e.target.classList.add("success");
//             e.target.classList.remove("error");
//         }else{
//             e.target.classList.add("error");
//             e.target.classList.remove("success");
//         }
//     }

//     if (e.target.name === 'username') {
//         pattern = /^[a-zA-Z ]{3,}$/;
//         displayBorder();
//     }else if (e.target.name === 'email') {
//         pattern = /^[a-zA-Z0-9._%+-]{3,}$/;
//         displayBorder();
//     }else if (e.target.name === 'password1') {
//         pattern = /^[a-zA-Z0-9]{8,}$/;
//         displayBorder();
//     }else if (e.target.name === 'password2') {
//         pattern = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;
//         displayBorder();
//     }
// }

// form.addEventListener('keyup', liveFeedBack);
// form.addEventListener('click', (e)=>{
//     errorTest.push(e.target);
// });
// // form.addEventListener('submit', submitUserData);
