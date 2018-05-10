@echo off
python setup.py bdist_wheel
python setup.py sdist

twine upload dist\*

rm -fr build/
rm -fr dist/
REM find . -name '*.egg-info' -exec rm -fr {} +
REM find . -name '*.egg' -exec rm -f {} +

REM python setup.py sdist
REM python setup.py bdist_wheel
