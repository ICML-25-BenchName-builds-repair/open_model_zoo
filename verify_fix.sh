#!/bin/bash
cd /lca-workspace/repos/openvinotoolkit__open_model_zoo/tools/accuracy_checker
# Check for trailing whitespace in the file
if grep -q "\\s$" openvino/tools/accuracy_checker/evaluators/model_evaluator.py; then
  echo "Trailing whitespace found in the file"
  exit 1
else
  echo "No trailing whitespace found in the file"
  exit 0
fi