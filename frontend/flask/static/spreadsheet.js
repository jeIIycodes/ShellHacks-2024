// Path to your CSV file
const csvFilePath = '../static/student_spending.csv';

// Function to fetch and display CSV data
function displaySpreadsheet() {
    fetch(csvFilePath)
        .then(response => response.text())  // Read file as text
        .then(data => {
            const rows = data.split('\n');   // Split CSV into rows
            const table = document.createElement('table');
            table.classList.add('table', 'table-striped', 'table-hover');

            rows.forEach((row, index) => {
                const cells = row.split(',');
                const tableRow = table.insertRow();

                cells.forEach(cell => {
                    const cellElement = index === 0 ? tableRow.insertCell() : tableRow.insertCell();
                    cellElement.innerHTML = cell;  // Populate the cell with data
                });
            });

            // Append the table to the container div
            document.getElementById('spreadsheet-container').appendChild(table);
        })
        .catch(error => console.error('Error loading CSV file:', error));
}

// Run the function to display the spreadsheet
displaySpreadsheet();
