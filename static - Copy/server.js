const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware to parse JSON requests
app.use(bodyParser.json());

// Serve the form HTML when accessing the root URL
app.get('/', (req, res) => {
    const formPath = path.join(__dirname, 'index.html'); // Adjust path if `index.html` is in a subdirectory
    res.sendFile(formPath);
});

// Endpoint to handle form submission
app.post('/submit', (req, res) => {
    console.log("Received data:", req.body);

    const data = req.body;

    // File path for saving CSV data
    const filePath = path.join(__dirname, 'respiratory_data.csv');

    // Convert data to CSV format
    const csvRow = Object.values(data).join(',') + '\n';

    // Append data to CSV file
    fs.appendFile(filePath, csvRow, (err) => {
        if (err) {
            console.error('Error writing to file:', err);
            return res.status(500).send('Error saving data.');
        }
        console.log('Data saved successfully.');
        res.status(200).send('Data saved successfully.');
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}`);
});
