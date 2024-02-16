const tableData = document.getElementById("table");
const paginationLinks = document.getElementById("pagination-links");

// Event delegation to handle click events on buttons
tableData.addEventListener('click', function(event) {
    if (event.target.classList.contains('res')) {
        // Get the result ID from the button's ID attribute
        const resid = event.target.id
        const url = `/results/${resid}`
        window.location.href = url
    }
});

function fetchData(page) {
    $.ajax({
        type:'GET',
        url: `/results/?page=${page}`,
        success: function(ele){
            const results = ele.result
            const currentPage = ele.page;
            const totalPages = ele.total_pages;
            tableData.innerHTML +=``
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
            paginationLinks.innerHTML = '';
            for (let i = 1; i <= totalPages; i++) {
                paginationLinks.innerHTML += `
                <li class="page-item ${i === currentPage ? 'active' : ''}">
                    <a class="page-link" href="?page=${i}">${i}</a>
                </li>`;
            }
        },
        error: function (error){
            console.log(error);
        }    
    })
}        
// Event delegation to handle click events on pagination links
paginationLinks.addEventListener('click', function(event) {
    if (event.target.tagName === 'A') {
        event.preventDefault();
        const page = parseInt(event.target.getAttribute('href').split('=')[1]);
        fetchData(page);
    }
});
fetchData(1);