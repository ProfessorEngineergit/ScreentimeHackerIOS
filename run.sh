#!/bin/bash
# Simple script to run the ScreenTime Hacker iOS web application

echo "🔓 Starting ScreenTime Hacker iOS..."
echo "=================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.7 or higher and try again."
    exit 1
fi

# Check if dependencies are installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip3 install -r requirements.txt
    echo ""
fi

echo "🚀 Starting web application..."
echo "📱 Open your browser and navigate to: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
