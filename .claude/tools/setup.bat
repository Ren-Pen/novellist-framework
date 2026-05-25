@echo off
REM Setup script — create the project's Python venv for tools/ scripts.
REM
REM Usage:
REM   .claude\tools\setup.bat
REM   .claude\tools\setup.bat python3.11
REM
REM Idempotent: if .venv\ already exists, this script does nothing.

setlocal

REM Locate project root (grandparent of this script)
set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%..\.."
set "VENV_DIR=%PROJECT_ROOT%\.venv"

REM Default Python interpreter; optional first argument overrides.
set "PYTHON_BIN=python"
if not "%~1"=="" set "PYTHON_BIN=%~1"

if exist "%VENV_DIR%" (
  echo venv already exists at %VENV_DIR%
  echo to recreate: rmdir /s /q "%VENV_DIR%" ^&^& %~nx0
  exit /b 0
)

echo creating venv at %VENV_DIR% using %PYTHON_BIN%
"%PYTHON_BIN%" -m venv "%VENV_DIR%"
if errorlevel 1 (
  echo error: failed to create venv with %PYTHON_BIN%
  exit /b 1
)

REM Check Python version is >= 3.9
for /f "delims=" %%V in ('"%VENV_DIR%\Scripts\python.exe" -c "import sys; print(sys.version_info >= (3, 9))"') do set "VERSION_OK=%%V"
if not "%VERSION_OK%"=="True" (
  for /f "delims=" %%V in ('"%VENV_DIR%\Scripts\python.exe" --version') do set "ACTUAL=%%V"
  echo error: tools/ scripts require Python 3.9+, got %ACTUAL%
  echo re-run with: %~nx0 python3.11
  rmdir /s /q "%VENV_DIR%"
  exit /b 1
)

echo venv ready. Python version:
"%VENV_DIR%\Scripts\python.exe" --version

endlocal
