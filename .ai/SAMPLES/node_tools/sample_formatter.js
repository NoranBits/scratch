const fs = require('fs');

/**
 * Sample Tool: JSON Formatter
 * Purpose: Demonstrates how to read, modify, and write JSON files.
 */
function formatJson(filePath) {
    if (!fs.existsSync(filePath)) {
        console.error(`Error: File not found: ${filePath}`);
        return;
    }

    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    console.log(`--- Formatting ${filePath} ---`);

    // Example modification: add a timestamp
    data._last_formatted = new Date().toISOString();

    fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
    console.log('Done.');
}

const targetFile = process.argv[2];
if (targetFile) {
    formatJson(targetFile);
} else {
    console.log('Usage: node sample_formatter.js <file.json>');
}
