const tableData = document.getElementById("table").querySelector("tbody");
const paginationLinks = document.getElementById("pagination-links");

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
    $.ajax({
        type: 'GET',
        url: `/results/?page=${page}`,
        success: function(response) {
            const results = response.result;
            console.log(results)
            const currentPage = response.page;
            const totalPages = response.total_pages;
            populateTable(results);
            renderPaginationLinks(currentPage, totalPages);
        },
        error: function(error) {
            console.log('Error:', error);
        }
    });
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