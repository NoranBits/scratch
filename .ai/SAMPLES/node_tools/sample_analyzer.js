const fs = require('fs');
const path = require('path');

/**
 * Sample Tool: File Analyzer
 * Purpose: Demonstrates how to read and analyze files using Node.js.
 */
function analyzeFiles(dir) {
    console.log(`--- Analyzing Files in: ${dir} ---`);
    const files = fs.readdirSync(dir);

    files.forEach(file => {
        const fullPath = path.join(dir, file);
        const stats = fs.statSync(fullPath);
        if (stats.isFile()) {
            console.log(`- ${file} (${stats.size} bytes)`);
        }
    });
}

const targetDir = process.argv[2] || '.';
analyzeFiles(targetDir);
