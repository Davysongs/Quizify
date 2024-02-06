const tableData = document.getElementById("table")
const rows = document.getElementById("rows")

//check if the response is none and display a message for that
//display all results in a table
let resID;
$.ajax({
    type:'GET',
    url:`/results/`,
    success: function(ele){
        const results = ele.result
        for (var i = 0; i < results.length; i++) {
            var score = results[i].score;
            var quiz = results[i].quiz;
            var resid = results[i].resid;
            var date = results[i].date;
            var status = results[i].status;
            tableData.innerHTML += `
            <table width="100%" style="text-align: center;">
            <tr>
                <th>User</th> 
                <th>Quiz</th> 
                <th>Score</th>
                <th>Result ID</th>
                <th>Quiz Date</th> 
                <th></th>
            </tr>
            <tr>            
            <td>${date}</td>
            <td>${quiz}</td>
            <td>${score}</td>
            <td>${status}</td>
            <td>${resid}</td>
            <td><a href="http://127.0.0.1:8000/results/${resID}"><button>view details</button></a></td>
            </tr>
            `
        
        }

    },
    error: function (error){
        console.log(error)
    }    
})

detail.addEventListener('click', function (event) {
    window.location.href =(`/results/${resID}`)
})