@echo off

REM Command file for 

if "%1" == "init" (
    python3 -m venv venv
    .\Script\activate.bat
)

if "%1" == "install" (
    pip install -r requirements.txt
)

if "%1" == "test" (
    python -m unittest test/test_breakfast.py
)