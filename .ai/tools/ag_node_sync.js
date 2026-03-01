const fs = require('fs');
const path = require('path');

// --- CONFIG ---
const ROOT = path.resolve(__dirname, '../../');
const PKG_PATH = path.join(ROOT, 'package.json');

function analyzePackage() {
    console.log('--- AntiGravity Node.js Structural Analysis ---');
    if (!fs.existsSync(PKG_PATH)) {
        console.error('Error: package.json not found at ' + PKG_PATH);
        return;
    }

    const pkg = JSON.parse(fs.readFileSync(PKG_PATH, 'utf8'));
    console.log(`Project: ${pkg.name} v${pkg.version}`);
    console.log(`Architecture: ${pkg.description}`);

    const scripts = Object.keys(pkg.scripts || {});
    console.log(`Governed Scripts: ${scripts.join(', ')}`);

    // Structural Health Check
    const hasAI = fs.existsSync(path.join(ROOT, '.ai'));
    const hasExternal = fs.existsSync(path.join(ROOT, 'external_repos'));

    let auditStatus = 'UNKNOWN';
    const auditPath = path.join(ROOT, '.ai', 'dep_audit.json');
    if (fs.existsSync(auditPath)) {
        const audit = JSON.parse(fs.readFileSync(auditPath, 'utf8'));
        auditStatus = audit.status;
    }

    const health = {
        ai_integrity: hasAI,
        federation_ready: hasExternal,
        npm_governance: true,
        audit_status: auditStatus,
        timestamp: new Date().toISOString()
    };

    fs.writeFileSync(path.join(ROOT, '.ai', 'node_health.json'), JSON.stringify(health, null, 2));
    console.log('Structural Health Exported to .ai/node_health.json');
}

analyzePackage();
