// DOM IMPLEMENTATION

const login_details = JSON.parse(localStorage.getItem('login_details'));
const allUsers = JSON.parse(localStorage.getItem("users"));

const chosenCategory = JSON.parse(localStorage.getItem("category"))

const userName = document.querySelector(".username");
const time = document.querySelector(".time");
let miniutes = 5;
let seconds = 00;

// Question & Options
const questionText = document.querySelector(".question-text");
const optionA = document.querySelector(".first-option .middle");
const optionB = document.querySelector(".second-option .middle");
const optionC = document.querySelector(".third-option .middle");
const optionD = document.querySelector(".fourth-option .middle");

const nxtBtn = document.querySelector(".next-btn");
let currentQuestion = 0;

let currentNumber = document.querySelector(".current-question");

const btn = document.querySelector(".btn");

let scores = 0;

// Visible score

let scorePlus = document.querySelector(".score-plus");
let scoreMinus = document.querySelector(".score-minus");
let middleDisplay = document.querySelector(".score-dis");

let scoreContent = document.querySelector(".score");

scoreContent.textContent = scores;



// To know which user logged in and display the user's name

for (let i = 0; i < allUsers.length; i++) {
    if (login_details.username === allUsers[i].username) {
        alert(login_details.name + ", the timer start counting immediately you click 'OK', get ready to set a record.");
        alert("Your chosen category is " + chosenCategory);
        console.log(allUsers);
        break;
    }    
}

userName.textContent = login_details.username;

// TIME EDITING

setInterval(()=>{
    if (seconds < 10) {
        let second = "0" + seconds;
        seconds = second;
    }
    if (seconds < 1) {
        seconds = 59;
        miniutes--;
    }
    time.textContent = miniutes + ":" + seconds
    seconds--;

    if (miniutes == '-1') {
        alert("Time up. Click 'OK' to view score dashboard")
    }
}, 1000);


// QUESTIONS, OPTIONS AND ANSWERS

if (chosenCategory == "General Studies") {


    const questions = [
        {
            number: 1,
            question: "When is Christmas Day",
            optionA: "Dec 23",
            optionB: "Dec 15",
            optionC: "Dec 25",
            optionD: "Dec 52",
            answer: "C"
        },
        {
            number: 2,
            question: "When is Boxing Day",
            optionA: "Dec 26",
            optionB: "Dec 16",
            optionC: "Dec 25",
            optionD: "Dec 19",
            answer: "A"
        },
        {
            number: 3,
            question: "What is full meaning of WHO",
            optionA: "World Human Organisation",
            optionB: "West Health Organisation",
            optionC: "World Health Organisation",
            optionD: "Wise Human Organisation",
            answer: "C"
        },
        {
            number: 4,
            question: "At what age did Adam die in the Bible",
            optionA: "900",
            optionB: "309",
            optionC: "911",
            optionD: "930",
            answer: "D"
        },
        {
            number: 5,
            question: "Which disney character left a glass shoe in front the palace",
            optionA: "Snow White",
            optionB: "Cinderella",
            optionC: "Sleeping Beauty",
            optionD: "Elsa",
            answer: "B"
        },
        {
            number: 6,
            question: "What does the word laquacious mean?",
            optionA: "Angry",
            optionB: "Chatty",
            optionC: "Beautiful",
            optionD: "Shy",
            answer: "B"
        },
        {
            number: 7,
            question: "In 1718, which pirate died in battle coast of what is now North Carolina",
            optionA: "Blackbeard",
            optionB: "Calico Jack",
            optionC: "Captain Kidd",
            optionD: "Bartholomew Rob",
            answer: "A"
        },
        {
            number: 8,
            question: "In UK, the abbreviation NHS stands for National _____ Service?",
            optionA: "Humanity",
            optionB: "Health",
            optionC: "Honour",
            optionD: "Household",
            answer: "B"
        },
        {
            number: 9,
            question: "Which of the following is correctly spelt",
            optionA: "Comitment",
            optionB: "Comittment",
            optionC: "Committment",
            optionD: "Commitment",
            answer: "D"
        },
        {
            number: 10,
            question: "What is full meaning of WHO",
            optionA: "World Human Organisation",
            optionB: "West Health Organisation",
            optionC: "World Health Organisation",
            optionD: "Wise Human Organisation",
            answer: "C"
        }
    ]
    

}else if (chosenCategory == "Mathematics") {

}else if (chosenCategory == "Current Affairs") {

}else if (chosenCategory == "History") {

}



const questions = [
    {
        number: 1,
        question: "When is Christmas Day",
        optionA: "Dec 23",
        optionB: "Dec 15",
        optionC: "Dec 25",
        optionD: "Dec 52",
        answer: "C"
    },
    {
        number: 2,
        question: "When is Boxing Day",
        optionA: "Dec 26",
        optionB: "Dec 16",
        optionC: "Dec 25",
        optionD: "Dec 19",
        answer: "A"
    },
    {
        number: 3,
        question: "What is full meaning of WHO",
        optionA: "World Human Organisation",
        optionB: "West Health Organisation",
        optionC: "World Health Organisation",
        optionD: "Wise Human Organisation",
        answer: "C"
    },
    {
        number: 4,
        question: "At what age did Adam die in the Bible",
        optionA: "900",
        optionB: "309",
        optionC: "911",
        optionD: "930",
        answer: "D"
    },
    {
        number: 5,
        question: "Which disney character left a glass shoe in front the palace",
        optionA: "Snow White",
        optionB: "Cinderella",
        optionC: "Sleeping Beauty",
        optionD: "Elsa",
        answer: "B"
    },
    {
        number: 6,
        question: "What does the word laquacious mean?",
        optionA: "Angry",
        optionB: "Chatty",
        optionC: "Beautiful",
        optionD: "Shy",
        answer: "B"
    },
    {
        number: 7,
        question: "In 1718, which pirate died in battle coast of what is now North Carolina",
        optionA: "Blackbeard",
        optionB: "Calico Jack",
        optionC: "Captain Kidd",
        optionD: "Bartholomew Rob",
        answer: "A"
    },
    {
        number: 8,
        question: "In UK, the abbreviation NHS stands for National _____ Service?",
        optionA: "Humanity",
        optionB: "Health",
        optionC: "Honour",
        optionD: "Household",
        answer: "B"
    },
    {
        number: 9,
        question: "Which of the following is correctly spelt",
        optionA: "Comitment",
        optionB: "Comittment",
        optionC: "Committment",
        optionD: "Commitment",
        answer: "D"
    },
    {
        number: 10,
        question: "What is full meaning of WHO",
        optionA: "World Human Organisation",
        optionB: "West Health Organisation",
        optionC: "World Health Organisation",
        optionD: "Wise Human Organisation",
        answer: "C"
    }
]

questionText.textContent = questions[0].question;
optionA.textContent = questions[0].optionA;
optionB.textContent = questions[0].optionB;
optionC.textContent = questions[0].optionC;
optionD.textContent = questions[0].optionD;

let moved = true;

function moveToNext() {
    if (!moved) {
        clicked = true;
        for (let i = 0; i < options.length; i++) {
            options[i].querySelector(".left").classList.remove('correct');
            options[i].querySelector(".middle").classList.remove('correct');
            options[i].querySelector(".right").classList.remove('correct');

            options[i].querySelector(".left").classList.remove('wrong');
            options[i].querySelector(".middle").classList.remove('wrong');
            options[i].querySelector(".right").classList.remove('wrong');

            options[i].querySelector(".left").setAttribute("hover", false)
            options[i].querySelector(".middle").setAttribute("hover", false)
            // console.log(options[i].querySelector(".right").getAttribute("hover")); 
        }

        currentQuestion++;
        questionText.textContent = questions[currentQuestion].question;
        optionA.textContent = questions[currentQuestion].optionA;
        optionB.textContent = questions[currentQuestion].optionB;
        optionC.textContent = questions[currentQuestion].optionC;
        optionD.textContent = questions[currentQuestion].optionD;

        currentNumber.textContent = currentQuestion + 1;

        scorePlus.classList.add("hidden");
        scoreMinus.classList.add("hidden");
        middleDisplay.classList.remove("to-top");
        middleDisplay.classList.add("back-to-norm");
        // middleDisplay.classList.remove("no-trans");
    }
   moved = true;
}

// nxtBtn.addEventListener("click", ()=>{
//     moveToNext();
    
// })



// ANSWER SELECTION AND VERIFYING

const options = document.querySelectorAll(".options");

let chosenOption;
let clicked = true;


options.forEach((option)=>{
    option.addEventListener("click", ()=>{
        if (clicked) {
            moved = false;
            clicked = false;
            if (option.classList.contains("A")) {
                chosenOption = "A";
            }else if (option.classList.contains("B")) {
                chosenOption = "B";
            }else if (option.classList.contains("C")) {
                chosenOption = "C";
            }else if (option.classList.contains("D")) {
                chosenOption = "D";
            }
    
            if (chosenOption === questions[currentQuestion].answer) {
                option.querySelector(".left").classList.add("correct");
                option.querySelector(".middle").classList.add("correct");
                option.querySelector(".right").classList.add("correct");
                document.querySelector(`.btn-${currentQuestion + 1}`).classList.add("correct");

                nxtBtn.innerHTML = `<i class=" fa-solid fa-check"></i>`;

                scores += 200;

                scorePlus.classList.remove("hidden");
                middleDisplay.classList.add("to-top");
                // setTimeout(()=>{
                //     middleDisplay.classList.add("no-trans");
                // },1000);
            }else{
                option.querySelector(".left").classList.add("wrong");
                option.querySelector(".middle").classList.add("wrong");
                option.querySelector(".right").classList.add("wrong");
                document.querySelector(`.btn-${currentQuestion + 1}`).classList.add("wrong");
                setTimeout(()=>{
                    document.querySelector("." + questions[currentQuestion].answer).querySelector(".left").classList.add("correct");
                    document.querySelector("." + questions[currentQuestion].answer).querySelector(".middle").classList.add("correct");
                    document.querySelector("." + questions[currentQuestion].answer).querySelector(".right").classList.add("correct");
                }, 1000);

                scoreMinus.classList.remove("hidden");
                middleDisplay.classList.add("to-top");
                // setTimeout(()=>{
                //     middleDisplay.classList.add("no-trans");
                // },1000);

                nxtBtn.innerHTML = `<i class=" fa-solid fa-xmark"></i>`;

                scores -= 100;

            }

            setTimeout(()=>{
                if (!currentQuestion <= 9) {
                    moveToNext();
                }
            },1500);

            if (scores < 0) {
                scores = 0;
            }
        }

        if (currentQuestion >= 9) {
            nxtBtn.textContent = "Finish";
        
            nxtBtn.addEventListener('click', ()=>{
                // alert("You score is " + scores + " points");

                window.confirm("You score is " + scores + " points");
                window.location = "index.html"
            })
        }
        scoreContent.textContent = scores;
    })
})