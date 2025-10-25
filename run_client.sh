#!/bin/bash
# Tortoise TTS Client Runner
# This script helps you run the Python clients with the correct interpreter

PYTHON_PATH="/Users/joshbeard/code/tortoise-tts/.venv/bin/python"

echo "🎤 Tortoise TTS Client Runner"
echo "=============================="
echo ""
echo "Available clients:"
echo "1. Minimal Client (quick test)"
echo "2. Simple Client (with interactive mode)"
echo "3. Examples Client (multiple examples)"
echo ""

read -p "Choose a client (1-3): " choice

case $choice in
    1)
        echo "🚀 Running Minimal Client..."
        $PYTHON_PATH minimal_client.py
        ;;
    2)
        echo "🚀 Running Simple Client..."
        $PYTHON_PATH simple_client.py
        ;;
    3)
        echo "🚀 Running Examples Client..."
        $PYTHON_PATH examples_client.py
        ;;
    *)
        echo "Invalid choice. Running Minimal Client by default..."
        $PYTHON_PATH minimal_client.py
        ;;
esac