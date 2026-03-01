import os
import re
import argparse

class AgEnvSanitizer:
    """Tool to scrub local environment signatures and absolute paths from files."""
    
    def __init__(self, root_dir):
        self.root_dir = os.path.abspath(root_dir)
        # Pattern to find the current local absolute path root
        # This will escape the path for regex use
        self.root_pattern = re.escape(self.root_dir).replace(r'\\', r'[\/\\]')
        # Also handle potential URI format
        self.uri_pattern = re.escape("file:///" + self.root_dir.replace("\\", "/")).replace(r'\/', r'[\/\\]')

    def sanitize_content(self, content):
        """Replaces absolute path signatures with relative root markers."""
        # Replace absolute file:/// URIs (with trailing slash if present)
        content = re.sub(self.uri_pattern + r'[/\\]?', "./", content, flags=re.IGNORECASE)
        # Replace absolute filesystem paths (with trailing slash if present)
        content = re.sub(self.root_pattern + r'[/\\]?', "./", content, flags=re.IGNORECASE)
        
        # Specific cleanup for any leftover double slashes introduced by replacement
        content = content.replace("./", "./")
        content = content.replace("./", "./")
        
        return content

    def sanitize_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            sanitized = self.sanitize_content(content)
            
            if sanitized != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(sanitized)
                return True
        except Exception as e:
            print(f"Error sanitizing {file_path}: {e}")
        return False

    def walk_and_sanitize(self, target_dir):
        count = 0
        for root, _, files in os.walk(target_dir):
            if ".git" in root or "node_modules" in root:
                continue
            for file in files:
                if file.endswith(('.html', '.md', '.json', '.py', '.txt', '.js', '.ts')):
                    if self.sanitize_file(os.path.join(root, file)):
                        count += 1
        return count

def main():
    parser = argparse.ArgumentParser(description="AntiGravity Environment Sanitizer")
    parser.add_argument("--path", type=str, default=".", help="Directory to sanitize")
    parser.add_argument("--root", type=str, default=None, help="Force a specific root to scrub")

    args = parser.parse_args()
    root = args.root if args.root else os.getcwd()
    sanitizer = AgEnvSanitizer(root)
    
    print(f"Scrubbing absolute paths relative to: {root}")
    count = sanitizer.walk_and_sanitize(args.path)
    print(f"Sanitization complete. Cleaned {count} files.")

if __name__ == "__main__":
    main()
