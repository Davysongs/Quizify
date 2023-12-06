const form = document.querySelector(".form");


const namePattern = /^[a-zA-Z ]{3,}$/;
const passwordPattern = /^[a-zA-Z0-9]{8,}$/;
const emailPattern = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/;

let errorTest = [];
let error;
let userExist;


function submitUserData(e) {
    e.preventDefault();

    if (form.name.value === "" || form.password.value === "" || form.email.value === "" || form.accept.checked === false) {
        alert("All fields are required")
    }else{
        for (let i = 0; i < errorTest.length; i++) {
            // console.log(errorTest[i].classList.contains("error"));
            if (errorTest[i].classList.contains("error")) {
                error = true;
                break;
            }else{
                error = false;
            }
        }
        if (error) {
            alert("Fix all errors!")
        }else{
            const user = {
                name: form.name.value,
                username: form.username.value,
                password: form.password.value,
                email: form.email.value,
                accept: form.accept.checked
            }
            saveUser(user);
        }
        
    }    
}




function saveUser(user) {
    let data = localStorage.getItem('users');  
    let users = JSON.parse(data);

    if(users === null){
        localStorage.setItem('users', JSON.stringify([user]));
        alert(`A new account has been successfully created for ${user.name}`);

        location.href = "./login.html";
        form.reset(); 
    } else {
        for (let i = 0; i < users.length; i++) {
            // console.log(users[i].username, user.username);
            if (users[i].username === user.username) {
                userExist = true;
                break;
            }else{
                userExist = false;
            }
        }
        if (userExist) {
            alert("Username has already been used.");
          }else{
            users.push(user);
            localStorage.setItem("users", JSON.stringify(users));

            alert(`A new account has been successfully created for ${user.name}`);

            location.href = "./login.html";
            form.reset();  

        }
    }
}

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
form.addEventListener('submit', submitUserData);
