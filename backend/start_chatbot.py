#!/usr/bin/env python3
"""
Chatbot Backend Starter Script
This script starts the Flask chatbot server.
Make sure to install dependencies first: pip install -r requirements.txt
"""

import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['flask', 'flask_cors', 'sklearn', 'numpy']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install them with: pip install -r requirements.txt")
        return False
    
    print("✅ All required packages are installed!")
    return True

def main():
    print("🤖 Starting Event Management Chatbot Backend...")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check if required files exist
    required_files = ['intents.json', 'chatbot.py', 'app.py']
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Required file not found: {file}")
            sys.exit(1)
    
    print("✅ All required files found!")
    print("\n🚀 Starting Flask server on http://127.0.0.1:5000")
    print("📱 The chatbot will be available at: http://127.0.0.1:5000/chat")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Import and run the Flask app
    try:
        from app import app
        app.run(host="0.0.0.0", port=5000, debug=True)
    except KeyboardInterrupt:
        print("\n👋 Chatbot server stopped!")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
