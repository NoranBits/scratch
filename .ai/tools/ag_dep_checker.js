const fs = require('fs');
const path = require('path');

// --- CONFIG ---
const ROOT = path.resolve(__dirname, '../../');
const PKG_PATH = path.join(ROOT, 'package.json');

/**
 * Tool: Dependency Checker
 * Purpose: Audits package.json for common issues and enforces patterns.
 */
function auditDependencies() {
    console.log('--- AntiGravity Node.js Dependency Audit ---');
    if (!fs.existsSync(PKG_PATH)) {
        console.error('Error: package.json not found.');
        return;
    }

    const pkg = JSON.parse(fs.readFileSync(PKG_PATH, 'utf8'));
    const deps = pkg.dependencies || {};
    const devDeps = pkg.devDependencies || {};

    console.log(`Found ${Object.keys(deps).length} dependencies and ${Object.keys(devDeps).length} devDependencies.`);

    // Pattern Checks
    const issues = [];

    // Check for large or risky dependencies (example)
    const risky = ['moment', 'lodash', 'axios']; // Just examples
    Object.keys(deps).forEach(dep => {
        if (risky.includes(dep)) {
            issues.push(`Warning: Consider modular alternatives to '${dep}'.`);
        }
    });

    // Check for missing engines field
    if (!pkg.engines || !pkg.engines.node) {
        issues.push("Recommendation: Add an 'engines' field to package.json to specify Node.js version.");
    }

    if (issues.length === 0) {
        console.log('No immediate issues found. High structural integrity.');
    } else {
        issues.forEach(issue => console.log(`[!] ${issue}`));
    }

    // Export Findings
    const findings = {
        issues: issues,
        audit_time: new Date().toISOString(),
        status: issues.length > 5 ? 'CRITICAL' : (issues.length > 0 ? 'WARNING' : 'HEALTHY')
    };

    fs.writeFileSync(path.join(ROOT, '.ai', 'dep_audit.json'), JSON.stringify(findings, null, 2));
    console.log('Audit results exported to .ai/dep_audit.json');
}

auditDependencies();
