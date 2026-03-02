import subprocess
import os
import sys
from pathlib import Path

GPG_PATH = r"C:\Program Files\Git\usr\bin\gpg.exe"

def run_gpg(args):
    env = os.environ.copy()
    gpg_home = Path(".ai/GPG")
    gpg_home.mkdir(parents=True, exist_ok=True)
    # Remove problematic config if it exists
    conf = gpg_home / "gpg.conf"
    if conf.exists(): os.remove(conf)
    
    env["GNUPGHOME"] = str(gpg_home)
    
    full_args = [GPG_PATH] + args
    try:
        result = subprocess.run(full_args, env=env, capture_output=True, text=True, timeout=30)
        return result.stdout or result.stderr
    except Exception as e:
        print(f"GPG Error: {e}")
        return None

def generate_key(name, email):
    print(f"Generating GPG key for {name} <{email}>...")
    batch_config = f"""
    Key-Type: RSA
    Key-Length: 4096
    Subkey-Type: RSA
    Subkey-Length: 4096
    Name-Real: {name}
    Name-Email: {email}
    Expire-Date: 0
    %no-protection
    %commit
    """
    config_path = Path("TEMP/gpg_batch.conf")
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with open(config_path, "w") as f:
        f.write(batch_config)
    
    out = run_gpg(["--batch", "--generate-key", str(config_path)])
    print(out)
    if config_path.exists(): os.remove(config_path)

def get_keys():
    output = run_gpg(["--list-secret-keys", "--keyid-format", "LONG"])
    if not output: return []
    keys = []
    for line in output.splitlines():
        if line.startswith("sec"):
            try:
                if "/" in line:
                    key_id = line.split("/")[1].split()[0]
                    if key_id not in keys: keys.append(key_id)
            except: continue
    return keys

def main():
    if not os.path.exists(GPG_PATH):
        print(f"CRITICAL: GPG not found at {GPG_PATH}")
        sys.exit(1)

    existing_keys = get_keys()
    if not existing_keys:
        name = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True).stdout.strip() or "AntiGravity Dev"
        email = subprocess.run(["git", "config", "user.email"], capture_output=True, text=True).stdout.strip() or "dev@antigravity.ai"
        generate_key(name, email)
        existing_keys = get_keys()

    if existing_keys:
        key_id = existing_keys[0]
        print(f"Key Ready: {key_id}")
        
        # Configure Git
        subprocess.run(["git", "config", "--global", "user.signingkey", key_id], check=True)
        subprocess.run(["git", "config", "--global", "commit.gpgsign", "true"], check=True)
        subprocess.run(["git", "config", "--global", "gpg.program", GPG_PATH], check=True)
        
        # Export Public Key
        pub_key = run_gpg(["--armor", "--export", key_id])
        if pub_key:
            with open(".ai/GPG_PUBLIC_KEY.txt", "w") as f:
                f.write(pub_key)
            print("[SUCCESS] GPG Security Protocol Active.")
    else:
        print("Failed to detect or generate GPG key.")

if __name__ == "__main__":
    main()
