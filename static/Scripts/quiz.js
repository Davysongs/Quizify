const url = window.location.href;
const quizBox = document.getElementById('quiz-box');

$.ajax({
    type: 'GET',
    url: `${url}/data`,
    success: function(response) {
        const data = response.data;

        data.forEach(questionData => {
            const question = Object.keys(questionData)[0];
            const answers = questionData[question];

            quizBox.innerHTML += `
                <hr>
                <div class="mb-2">
                    <b>${question}</b>
                </div>
            `;

            answers.forEach(answer => {
                const answerId = `${question}-${answer}`;

                quizBox.innerHTML += `
                    <div>
                        <input type="radio" class="ans" id="${answerId}" name="${question}" value="${answer}">
                        <label for="${answerId}">${answer}</label>
                    </div>
                `;
            });
        });
    },
    error: function(error) {
        console.log(error);
    }
});
