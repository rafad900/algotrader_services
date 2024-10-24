#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt
echo "Run fastapi server "
fastapi run main.py
