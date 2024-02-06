const tableData = document.getElementById("table")
const rows = document.getElementById("rows")
page = window.location.href

//check if the response is none and display a message for that
//display all results in a table

let resID;
$.ajax({
    type:'GET',
    url:page,
    success: function(ele){
        const results = ele.result
        console.log(results)
    },
    error: function (error){
        console.log(error)
    }    
})