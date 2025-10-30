@echo off
REM Simple script to run the ScreenTime Hacker iOS web application on Windows

echo 🔓 Starting ScreenTime Hacker iOS...
echo ==================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed.
    echo Please install Python 3.7 or higher and try again.
    pause
    exit /b 1
)

REM Check if dependencies are installed
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo 📦 Installing dependencies...
    pip install -r requirements.txt
    echo.
)

echo 🚀 Starting web application...
echo 📱 Open your browser and navigate to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py
pause
