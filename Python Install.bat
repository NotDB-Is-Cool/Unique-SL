@echo off
set PYTHON_VERSION=3.11.4
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/python-%PYTHON_VERSION%-amd64.exe

echo Installing Python %PYTHON_VERSION%...

curl -o python_installer.exe %PYTHON_URL%
start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
del python_installer.exe

echo Python %PYTHON_VERSION% installed successfully.