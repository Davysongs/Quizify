const form = document.querySelector(".form");


const namePattern = /^[a-zA-Z ]{3,}$/;
const passwordPattern = /^[a-zA-Z0-9]{8,}$/;
const emailPattern = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;

let errorTest = [];
let error;
let userExist;


let pattern;


function liveFeedBack(e) {

    function displayBorder() {
        let small = e.target.parentNode.querySelector('.form__group-small');
        small.textContent = pattern.test(e.target.value) ? "Valid" : "Invalid";
       
        if(pattern.test(e.target.value)){
            e.target.classList.add("success");
            e.target.classList.remove("error");
        }else{
            e.target.classList.add("error");
            e.target.classList.remove("success");
        }
    }

    if (e.target.name === 'name') {
        pattern = /^[a-zA-Z ]{3,}$/;
        displayBorder();
    }else if (e.target.name === 'username') {
        pattern = /^[a-zA-Z0-9._%+-]{3,}$/;
        displayBorder();
    }else if (e.target.name === 'password') {
        pattern = /^[a-zA-Z0-9]{8,}$/;
        displayBorder();
    }else if (e.target.name === 'email') {
        pattern = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;
        displayBorder();
    }
}

form.addEventListener('keyup', liveFeedBack);
form.addEventListener('click', (e)=>{
    errorTest.push(e.target);
});
// form.addEventListener('submit', submitUserData);
