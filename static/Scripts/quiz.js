
const url = window.location.href
const quizform = document.getElementById("quiz-form")
const csrf = document.getElementsByName("csrfmiddlewaretoken")
const quizBox = document.getElementById('quiz-box')
const timerBox = document.getElementById('timer-box')
const Activatetimer = (time) =>{
    if (time.toString().length <2){
        timerBox.innerHTML =` <b>0${time}:00</b>`
    }else{
        timerBox.innerHTML=`<b>${time}</b>`
    }
    let minutes = time - 1
    let seconds = 60 
    let displaySeconds
    let displayMinutes    
    const timer = setInterval(() => {
        seconds --
        if (seconds< 0){
            seconds = 59
            minutes --
        }  
        if (minutes.toString().length < 2 ){
            displayMinutes = "0" + minutes
        }else{
            displayMinutes = minutes
        }
        if (seconds.toString().length < 2){
            displaySeconds = "0" + seconds
        }else{
            displaySeconds = seconds
        }
        if (minutes<1 && seconds < 31){
            timerBox.style.color = 'red';
            timerBox.style.fontSize = '30px';
        }
        if (minutes ===0 && seconds === 0){
            timerBox.innerHTML = "<b>00:00</b>"
            setTimeout(()=>{
                clearInterval(timer)
                alert("Time's up")
                sendData()
            }, 500)
        }
        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000);
}

$.ajax({
    type: 'GET',
    url: `${url}/data`,
    success: function(response){
       const data= response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
               quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                
                answers.forEach(answer=>{
                    quizBox.innerHTML += `
                        <div>
                            <input type="radio" class = "ans" id = "${question}-${answer}" name ="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>
                    `
                })
            }
        });
        Activatetimer(response.time)
    },
    error: function (error){
        console.log(error)
    }
})

const  sendData = () =>{
    const elements = [...document.getElementsByClassName("ans")]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked) {
            data[el.name] = el.value
        }
        else{
            if (!data[el.name]){
                data[el.name] = null
            }
        }
    })
    $.ajax({
        type: 'POST',
        url: `${url}/save`,
        data: data,
        success: function(response){
            console.log(response)
        },
        error: function(error){
            console.log(error)
        }
    })
}


quizform.addEventListener('submit', e=>{
    e.preventDefault()
    sendData()
})