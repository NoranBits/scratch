import os
import re
import argparse
import json

class AgSecurityScanner:
    """Zero-Trust Security Scanner for AntiGravity Repositories."""
    
    SECRET_PATTERNS = [
        r"(?:key|password|secret|token|pw|auth)[-_\s]*[:=]\s*['\"]?([a-zA-Z0-9\._-]{16,})['\"]?",
        r"AIza[0-9A-Za-z-_]{35}", # Google API Key
        r"sk-[a-zA-Z0-9]{48}", # OpenAI Key
        r"-----BEGIN [A-Z ]+ PRIVATE KEY-----", # Private Keys
    ]
    
    PII_PATTERNS = [
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", # Emails
        r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", # IP Addresses
    ]
    
    PATH_LEAK_PATTERNS = [
        r"[a-zA-Z]:\\Users\\[a-zA-Z0-9._-]+\\", # Windows User Paths
        r"file:///+[a-zA-Z]:/", # Absolute file URIs
        r"/home/[a-zA-Z0-9._-]+/", # Linux Home Paths
    ]

    def __init__(self, root_dir):
        self.root_dir = root_dir

    def scan_file(self, file_path):
        findings = []
        try:
            with open(file_path, 'r', errors='ignore') as f:
                content = f.read()
                
                for pattern in self.SECRET_PATTERNS:
                    if re.search(pattern, content, re.IGNORECASE):
                        findings.append({"type": "SECRET", "path": file_path, "pattern": pattern})
                
                for pattern in self.PII_PATTERNS:
                    if re.search(pattern, content):
                        findings.append({"type": "PII", "path": file_path, "pattern": pattern})
                
                for pattern in self.PATH_LEAK_PATTERNS:
                    if re.search(pattern, content, re.IGNORECASE):
                        findings.append({"type": "PATH_LEAK", "path": file_path, "pattern": pattern})
        except Exception:
            pass
        return findings

    def scan_directory(self, dir_path):
        all_findings = []
        for root, _, files in os.walk(dir_path):
            if ".git" in root or "node_modules" in root:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                all_findings.extend(self.scan_file(file_path))
        return all_findings

def main():
    parser = argparse.ArgumentParser(description="AntiGravity Security Scanner")
    parser.add_argument("--path", type=str, default=".", help="Path to scan")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()
    scanner = AgSecurityScanner(os.getcwd())
    
    findings = scanner.scan_directory(args.path)
    
    if args.json:
        print(json.dumps(findings, indent=2))
    else:
        if not findings:
            print("No security violations found. Environment is CLEAN.")
        else:
            print(f"CRITICAL: Found {len(findings)} security violations!")
            for f in findings:
                print(f"- [{f['type']}] in {f['path']}")

if __name__ == "__main__":
    main()
