#!/usr/bin/env python3
"""
Check all Python files in the accuracy_checker directory for line length violations
"""

import os
import glob

def check_all_python_files():
    """Check all Python files for line length violations"""
    
    base_dir = "tools/accuracy_checker"
    pattern = os.path.join(base_dir, "**/*.py")
    
    all_violations = []
    
    for file_path in glob.glob(pattern, recursive=True):
        # Skip test files and build files as per the CI command
        if "/tests/" in file_path or "/build/" in file_path:
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    line_content = line.rstrip('\n\r')
                    if len(line_content) > 120:
                        all_violations.append({
                            'file': file_path,
                            'line_number': line_num,
                            'length': len(line_content),
                            'content': line_content
                        })
        except (UnicodeDecodeError, PermissionError):
            # Skip files that can't be read
            continue
    
    return all_violations

if __name__ == "__main__":
    violations = check_all_python_files()
    
    if violations:
        print(f"Found {len(violations)} line length violations:")
        for violation in violations:
            print(f"{violation['file']}:{violation['line_number']} ({violation['length']} chars)")
            print(f"  {violation['content'][:100]}...")
            print()
    else:
        print("No line length violations found in any Python files!")