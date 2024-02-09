const quizData = document.getElementById("result-data")
page = window.location.href

//check if the response is none and display a message for that
//display all results in a table

let resID;
$.ajax({
    type:'GET',
    url:page,
    success: function(ele){
        const results = ele.result
        quizData.innerHTML = `
        <div>
        <p> ${results}<p> 
        <div>`
    },
    error: function (error){
        console.log(error)
    }    
})