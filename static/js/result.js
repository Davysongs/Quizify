const tableData = document.getElementById("table").querySelector("tbody");
const paginationLinks = document.getElementById("pagination-links");
const table = document.getElementById("tablesection");

// Function to populate table data
function populateTable(results) {
    tableData.innerHTML = '';
    if (results){
    for (let i = 0; i < results.length; i++) {
        const score = results[i].score;
        const quiz = results[i].quiz;
        const resid = results[i].resid;
        const date = results[i].date;
        const status = results[i].status;
        tableData.innerHTML += `
        <tr>            
        <td>${date}</td>
        <td>${quiz}</td>
        <td>${score}%</td>
        <td>${status}</td>
        <td><button type="button" class="res btn btn-primary" id="${resid}">Details</button></td>
        </tr>`;
    }}
}
// Event delegation to handle click events on buttons
tableData.addEventListener('click', function(event) {
    if (event.target.classList.contains('res')) {
        // Get the result ID from the button's ID attribute
        const resid = event.target.id
        window.location.href = `/results/${resid}`
    }
});

// Function to render pagination links
function renderPaginationLinks(currentPage, totalPages) {
    paginationLinks.innerHTML = '';
    for (let i = 1; i <= totalPages; i++) {
        paginationLinks.innerHTML += `
        <li class="page-item ${i === currentPage ? 'active' : ''}">
            <a class="page-link" href="?page=${i}">${i}</a>
        </li>`;
    }
}

// AJAX request to fetch initial page data
function fetchData(page) {
    if (navigator.onLine) {
        $.ajax({
            type: 'GET',
            url: `/results/?page=${page}`,
            success: function(response) {
                const results = response.result;
                const currentPage = response.page;
                const totalPages = response.total_pages;
                if (results == ""){
                    table.innerHTML = `
                    <div>
                    <b> No Results Found!</b>
                    </div>   `          
                }else{
                    populateTable(results);
                    renderPaginationLinks(currentPage, totalPages);
                }
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    } else {
        // Offline case here...
        alert("You are currently offline.");
        }
}

// Event delegation to handle click events on pagination links
paginationLinks.addEventListener('click', function(event) {
    if (event.target.tagName === 'A') {
        event.preventDefault();
        const page = parseInt(event.target.getAttribute('href').split('=')[1]);
        fetchData(page);
    }
});

// Fetch initial page data
fetchData(1);