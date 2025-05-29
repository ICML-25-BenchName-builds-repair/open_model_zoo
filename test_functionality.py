#!/usr/bin/env python3
"""
Test to verify that the modified code maintains functionality
"""

def test_code_structure():
    """Test that the modified code structure is correct"""
    
    # Read the modified file
    file_path = "tools/accuracy_checker/openvino/tools/accuracy_checker/annotation_converters/amazon.py"
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Check that the essential parts are still there
    assert "self.source_dicts.append(" in content, "append call missing"
    assert "pickle.load(source_content, encoding='UTF-8')" in content, "pickle.load call missing"
    assert "# nosec B301" in content, "Security comment missing"
    assert "# disable pickle check" in content, "Pylint disable comment missing"
    
    # Check that the line break is properly formatted
    lines = content.split('\n')
    
    # Find the lines with our modification
    append_line_idx = None
    pickle_line_idx = None
    
    for i, line in enumerate(lines):
        if "self.source_dicts.append(" in line and line.strip().endswith("("):
            append_line_idx = i
        elif "pickle.load(source_content, encoding='UTF-8'))" in line:
            pickle_line_idx = i
    
    assert append_line_idx is not None, "Could not find append line"
    assert pickle_line_idx is not None, "Could not find pickle line"
    assert pickle_line_idx == append_line_idx + 1, "Lines should be consecutive"
    
    # Check line lengths
    for i, line in enumerate(lines):
        line_content = line.rstrip()
        assert len(line_content) <= 120, f"Line {i+1} still too long: {len(line_content)} chars"
    
    print("All functionality tests passed!")

if __name__ == "__main__":
    test_code_structure()