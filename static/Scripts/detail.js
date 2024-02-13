const container = document.getElementById("result-data");
const qdata = document.getElementById("data");
const tbody = document.getElementById('data-body');
const page = window.location.href;

$.ajax({
    type: 'GET',
    url: page,
    success: function (ele) {
        var results = ele.result;
        let pair;
        let ans;
        for (let i = 0; i < results.length; i++) {
            const score = results[i].score;
            const quiz = results[i].quiz;
            const resid = results[i].resid;
            const status = results[i].status;
            ans = results[i].ans;
            pair = results[i].pair    
        } 
        displayData(pair, ans)  
    },
    error: function (error) {
        console.log(error);
    }
});


// Function to create HTML elements and append them to the document
function displayData(pair, ans) {
    pair.forEach((item, index) => {
        // Create a new row for each key-value pair
        const row = document.createElement('tr');

        // Create a cell for the question (key)
        const questionCell = document.createElement('td');
        questionCell.textContent = Object.keys(item)[0]; // Get the key of the object
        row.appendChild(questionCell);

        // Create a cell for the answer (value)
        const answerCell = document.createElement('td');
        answerCell.textContent = item[Object.keys(item)[0]]; // Get the value of the object
        row.appendChild(answerCell);

        // Create a cell for the object
        const objectCell = document.createElement('td');
        if (ans[index] == "True") {
            objectCell.innerHTML = '<i class="fa fa-check-circle" style="color:green"></i>'; 
        } else {
            // Display red checkbox if condition is not met
            objectCell.innerHTML = '<i class="fa fa-check-circle" style="color:red"></i>'; 
        }
        row.appendChild(objectCell);

        // Append the row to the table body
        tbody.appendChild(row);
    });
}
    

