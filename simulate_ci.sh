#!/bin/bash
cd /lca-workspace/repos/openvinotoolkit__open_model_zoo/tools/accuracy_checker
# Check for trailing whitespace in all Python files (excluding tests and build directories)
if find -wholename '?*/**/*.py' -not -path "./tests/*" -not -path "./build/*" | xargs grep -l "\\s$"; then
  echo "Trailing whitespace found in some files"
  exit 1
else
  echo "No trailing whitespace found in any files"
  exit 0
fi