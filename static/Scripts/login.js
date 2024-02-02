const message = document.getElementById("messages")
// Define the URL for your JSON API
$.ajax({
    dataType:"json",
    type:'GET',
    async: false,
    url:`/login`,
    success : function(response){
        console.log(response.messages)
    }
})