// DOM IMPLEMENTATION

// Buttons
const aboutBtn = document.querySelector(".right-container nav ul .about");
const programBtn = document.querySelector(".right-container nav ul .program");
const contactBtn = document.querySelector(".right-container nav ul .contact-us");
const centerBtn = document.querySelector(".center button");
const closeDetails = document.querySelectorAll(".fa-circle-chevron-up");

// Extra Test
const extraText = document.querySelector(".extra-text");
const aboutUs = document.querySelector(".about-us-details");
const contactUs = document.querySelector(".contact-us-details");
const program = document.querySelector(".program-details");

// CONSTANTS FOR OPERATION

let isOpen = true;

// EXTRA DETAILS DISPLAY

function displayExtra(container){
    hideAll(); 
    if(isOpen === true){
        extraText.classList.add("show-details");
        container.classList.remove("hidden");
        container.classList.add("visible");


        centerBtn.style.transition = "all 2s";
        centerBtn.style.bottom = "-60vh";
        isOpen = false;
    }else{

        extraText.classList.remove("show-details");
        container.classList.add("hidden");
        container.classList.remove("visible");


        centerBtn.style.bottom = "";
        centerBtn.style.transition = "all .5s";
        isOpen = true;
    }
}

function hideAll() {
    extraText.classList.remove("show-details");
    aboutUs.classList.add("hidden");
    aboutUs.classList.remove("visible");
    contactUs.classList.add("hidden");
    contactUs.classList.remove("visible");
    program.classList.add("hidden");
    program.classList.remove("visible");


    centerBtn.style.bottom = "";
        centerBtn.style.transition = "all .5s";
    isOpen = true;
}


// Buttons Operation

aboutBtn.addEventListener("click", ()=>{
   displayExtra(aboutUs)
});

programBtn.addEventListener("click", ()=>{
   displayExtra(program)
});

contactBtn.addEventListener("click", ()=>{
   displayExtra(contactUs)
});

closeDetails.forEach(close =>{
    close.addEventListener("click", ()=>{
        hideAll();
    })
})

// NAV SLIDE IN

const faBar = document.querySelector(".fa-bars");
const mobileNav = document.querySelector(".mobile-nav");

faBar.addEventListener("click", (e)=>{
    mobileNav.classList.toggle("open");
    e.stopPropagation();
});

document.body.addEventListener("click", ()=>{
    mobileNav.classList.remove("open");
})

// DISPLAYING EXTRA ON MOBILE

const subOne = document.querySelector(".sub-one");
const subTwo = document.querySelector(".sub-two");

const mobileClick = document.querySelectorAll(".mobile");



mobileClick.forEach((click)=>{
    click.addEventListener("click", ()=>{
        if (click.classList.contains("about")) {
            subTwo.innerHTML = ` <h1>About Us</h1>

            <p>Do you like quizzes, quest and fun competitions? If yes, then you are in the right place. Josh-Quiz-App is dedicated to organising the most fun quizzes for everyone especially, you.</p>`;

            subOne.innerHTML = `<h1>
                    Welcome
                </h1>

                
                <p>Become the best and set a record that will leave a mark on this app.</p>
                <br>
                <button>View Categories</button>`;
        } else if (click.classList.contains("program")) {
            subTwo.innerHTML = `<h1>Program</h1>

            <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Possimus labore vero corrupti porro. Dolor quis eum iusto odio similique cupiditate harum mollitia excepturi perspiciatis! Dicta id molestias maiores maxime amet.
            </p>`;
        } else if (click.classList.contains("contact-us")) {
            subTwo.innerHTML = ` <h1>Contact Us</h1>

            <p>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Cum illum aspernatur reprehenderit repudiandae quaerat magni maxime enim officiis. Adipisci, quia laudantium commodi error aspernatur id voluptatum voluptatem illo sed qui?
            </p>`;
        }
    })
})