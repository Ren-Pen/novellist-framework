@echo off
REM Tool runner — invoke a tool script using the project venv.
REM
REM Usage:
REM   .claude\tools\run.bat ^<tool-name^> [args...]

setlocal

set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%..\.."
set "VENV_PYTHON=%PROJECT_ROOT%\.venv\Scripts\python.exe"

if not exist "%VENV_PYTHON%" (
  echo error: venv not initialized at %PROJECT_ROOT%\.venv 1>&2
  echo run: %SCRIPT_DIR%setup.bat 1>&2
  exit /b 1
)

if "%~1"=="" (
  echo usage: %~nx0 ^<tool-name^> [args...] 1>&2
  exit /b 1
)

set "TOOL_NAME=%~1"
set "TOOL_PATH=%SCRIPT_DIR%%TOOL_NAME%.py"
shift

if not exist "%TOOL_PATH%" (
  echo error: tool not found: %TOOL_PATH% 1>&2
  exit /b 1
)

REM cd to project root so tools see consistent relative paths
cd /d "%PROJECT_ROOT%"

REM Forward all remaining args
set "ARGS="
:gather
if "%~1"=="" goto :run
set "ARGS=%ARGS% %1"
shift
goto :gather

:run
"%VENV_PYTHON%" "%TOOL_PATH%"%ARGS%
exit /b %ERRORLEVEL%

endlocal
