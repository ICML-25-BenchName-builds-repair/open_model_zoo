#!/bin/bash
cd /lca-workspace/repos/openvinotoolkit__open_model_zoo/tools/accuracy_checker
python3 -m pip install pylint==2.10.2
PYTHONPATH=. python3 -m pylint --rcfile=.pylintrc openvino/tools/accuracy_checker/evaluators/model_evaluator.py