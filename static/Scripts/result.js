const tableData = document.getElementById("table")

//check if the response is none and display a message for that
//display all results in a table

$.ajax({
    type:'GET',
    url:`/results/`,
    success: function(ele){
        console.log(ele.result)
        tableData.innerHTML += `
        <table width="100%" style="text-align: left;">
        <tr>
            <th>User</th> 
            <th>Quiz</th> 
            <th>Score</th>
            <th>Result ID</th>
            <th>Quiz Date</th> 
            <th></th>
        </tr>
        <tr>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td id = ><a> </a></td>
        </tr>
    </table>`
    },
    error: function (error){
        console.log(error)
    }    
})

// detail.addEventListener('click', function (event) {
//     window.location.href =(`/results/{resultID}`)
// })