
const url = window.location.href
console.log("url")

$.ajax({
    type: 'GET',
    url: `${url}/data`,
    success: function(response){
        console.log(response)
    },
    error: function (error){
        console.log(error)
    }
})