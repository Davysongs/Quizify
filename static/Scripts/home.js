const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById("modal-body-confirm")
const startBtn = document.getElementById("start-button")
modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click',()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name =modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty =modalBtn.getAttribute('data-difficulty')
    const passMark = modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML=`
    <div class= "H5 mb-3">Are you ready to begin "<b>${name}</b>" quiz?</div>
    <div class="text-muted">
        <ul>
            <li>Number of questions: ${numQuestions}</li>
            <li>Difficulty: ${difficulty}</li>
            <li>Required Score: ${passMark}</li>
            <li>Time: ${time}</li>
        </ul>
    </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href =("/quiz/" + pk)
    })
}))