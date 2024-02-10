const quizData = document.getElementById("result-data");
const qdata = document.getElementById("data");
const page = window.location.href;

$.ajax({
    type: 'GET',
    url: page,
    success: function (ele) {
        var results = ele.result;
        let pair;
        for (let i = 0; i < results.length; i++) {
            const score = results[i].score;
            const quiz = results[i].quiz;
            const resid = results[i].resid;
            const status = results[i].status;
            const ans = results[i].ans;
            pair = results[i].pair      
        
       
            //     <div>
            //         <h2>${ans}</h2>
            //         <h3>${JSON.stringify(pair)}</h3>
            //     </div>
            // `;
        }    
        
    },
    error: function (error) {
        console.log(error);
    }
});

    

