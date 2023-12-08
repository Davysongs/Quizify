// let no = 100.455999999999;
// console.log(no.toFixed(2));

// DOM IMPLEMENTATION

const form = document.querySelector(".login");
const male = document.querySelector('#Male');
const female = document.querySelector('#Female');
console.log(form.read);
let userFound;
let genderSelected = false;


male.addEventListener('click', ()=>{
    male.checked = true;
    female.checked = false;
    genderSelected = true;
})

female.addEventListener('click', ()=>{
    female.checked = true;
    male.checked = false;
    genderSelected = true;
})


function checkUserData(e) {
    e.preventDefault();

    if (form.username.value === "" || form.password.value === "" || form.read.checked === false || !genderSelected) {
        alert("All fields are required");
        let users = JSON.parse(localStorage.getItem("users"));
        console.log(users);
    }else{
        let users = JSON.parse(localStorage.getItem("users"));
        let user = {
            username: form.username.value,
            password: form.password.value
        }
        console.log(users);

        if (users === null) {
            alert("Account not registered. Click on sign up to register.")
        }

        localStorage.setItem("category", JSON.stringify(form.categories.value))

        for (let i = 0; i < users.length; i++) {
            if(user.username === users[i].username && user.password === users[i].password){
                userFound = true;
                if(userFound){
                    alert("Welcome " + users[i].name);
                    localStorage.setItem('login_details', JSON.stringify(users[i]));
                    location.href = "./quiz-page.html";
                    form.reset();
                }
                break;
            }else{
                userFound = false;
            }
        }
        if (!userFound) {
            alert('Incorrect username or password.');
        }

        
    }    
}


form.addEventListener('submit', checkUserData);


