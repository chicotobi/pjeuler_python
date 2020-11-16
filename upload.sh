#!/bin/sh
./build.sh
python -m twine upload --repository pypi dist/*
pip install --upgrade pjeuler-chicotobi
