#!/bin/sh
rm dist/*
python setup.py sdist bdist_wheel
pip install --upgrade dist/*
