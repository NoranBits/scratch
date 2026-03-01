#!/usr/bin/env python3
import sys
import argparse
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ag_core import run_workplace_verify

def main():
    parser = argparse.ArgumentParser(description="AG Digest Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # M3: verify command
    verify_parser = subparsers.add_parser("verify", help="Workplace drift report + config presence")
    
    args = parser.parse_args()
    
    if args.command == "verify":
        report = run_workplace_verify()
        print("Workplace Verification Report:")
        print(f"Status: {report['status']}")
        print(f"Present: {', '.join(report['present'])}")
        if report['missing']:
            print(f"Missing: {', '.join(report['missing'])}")
        else:
            print("No critical layers missing.")
            
        sys.exit(0 if report["status"] == "PASS" else 1)

if __name__ == "__main__":
    main()
