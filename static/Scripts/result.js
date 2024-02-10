const tableData = document.getElementById("table");

// Event delegation to handle click events on buttons
tableData.addEventListener('click', function(event) {
    if (event.target.classList.contains('res')) {
        // Get the result ID from the button's ID attribute
        const resid = event.target.id
        const url = `/results/${resid}`
        window.location.href = url
    }
});

$.ajax({
    type:'GET',
    url:`/results/`,
    success: function(ele){
        const results = ele.result
        tableData.innerHTML +=`
        <tr>
        <th>Date</th> 
        <th>Quiz</th> 
        <th>Score</th>
        <th>Result </th>
        <th>Quiz-ID</th> 
        <th></th>
        </tr>`
        for (var i = 0; i < results.length; i++) {
            var score = results[i].score;
            var quiz = results[i].quiz;
            var resid = results[i].resid;
            var date = results[i].date;
            var status = results[i].status;
            tableData.innerHTML += `
            <tr>            
            <td>${date}</td>
            <td>${quiz}</td>
            <td>${score}%</td>
            <td>${status}</td>
            <td>${resid}</td>
            <td><button type = "button" class="res" id="${resid}" >view details</button></td>
            </tr>
            `;
        }
    },
    error: function (error){
        console.log(error);
    }    
});
