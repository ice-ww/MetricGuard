@echo off
setlocal
set PYTHONUTF8=1
if not exist "%~dp0.venv\Scripts\python.exe" (
    echo Python/project environment missing. Install Python 3.12 and uv.
    echo In this project run: uv sync --locked --python 3.12
    where uv >nul 2>nul
    if errorlevel 1 echo uv missing from PATH. Install uv, then reopen this terminal.
    pause
    exit /b 1
)
"%~dp0.venv\Scripts\python.exe" "%~dp0start.py" %*
set "startup_exit=%errorlevel%"
if not "%startup_exit%"=="0" pause
exit /b %startup_exit%
