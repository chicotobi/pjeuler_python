#!/bin/sh
rm dist/*
python setup.py sdist bdist_wheel
python -m twine upload --repository pypi dist/*
pip install --upgrade pjeuler-chicotobi
