#!/bin/bash -x


PYTEST="${HOME}/miniconda/envs/pic2pola/bin/pytest"
PYTHONPATH="${HOME}/git/pic2pola" 

cov_report_dir='./tests/pytest-covreport'

if test -n "$1"; then
    files="$1"
else
    files="./tests/*.py"
fi

if ! test -d $cov_report_dir; then
    echo "Cov report dir "${cov_report_dir}" is not exist."
    exit 1
fi

find ./ -name '*.pyo' -o -name '*.pyc' -delete

PYTHONPATH=$PYTHONPATH $PYTEST -vvv --cov ./src --cov-report term --cov-report html:${cov_report_dir} ${files}

if test -f /usr/bin/open; then
    /usr/bin/open ${cov_report_dir}/index.html
fi
