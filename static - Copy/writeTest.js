const fs = require('fs');
const path = require('path');

const filePath = path.join(__dirname, 'test.csv');
const testRow = 'Test,Data,1\n';

fs.appendFile(filePath, testRow, (err) => {
    if (err) {
        console.error('Error writing test file:', err);
    } else {
        console.log('Test file written successfully at:', filePath);
    }
});
