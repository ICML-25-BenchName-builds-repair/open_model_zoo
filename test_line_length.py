#!/usr/bin/env python3
"""
Script to test line length in amazon.py file
"""

def check_line_length(file_path, max_length=120):
    """Check if any lines exceed the maximum length"""
    violations = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            # Remove newline for accurate character count
            line_content = line.rstrip('\n\r')
            if len(line_content) > max_length:
                violations.append({
                    'line_number': line_num,
                    'length': len(line_content),
                    'content': line_content
                })
    
    return violations

if __name__ == "__main__":
    file_path = "tools/accuracy_checker/openvino/tools/accuracy_checker/annotation_converters/amazon.py"
    violations = check_line_length(file_path)
    
    if violations:
        print(f"Found {len(violations)} line length violations:")
        for violation in violations:
            print(f"Line {violation['line_number']}: {violation['length']} characters")
            print(f"Content: {violation['content']}")
            print()
    else:
        print("No line length violations found!")