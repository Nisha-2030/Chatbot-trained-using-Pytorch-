#!/usr/bin/env python3
"""
Test script for the chatbot backend
This script tests the chatbot functionality without starting the Flask server
"""

import json
import sys
import os

def test_chatbot():
    """Test the chatbot functionality"""
    print("🧪 Testing Chatbot Functionality...")
    print("=" * 40)
    
    try:
        # Import the chatbot
        from chatbot import ChatbotAssistant
        
        # Initialize chatbot
        print("📚 Loading chatbot with intents...")
        bot = ChatbotAssistant('intents.json')
        bot.load_model('chatbot_model.pth')
        print("✅ Chatbot initialized successfully!")
        
        # Test cases
        test_cases = [
            "Hello",
            "When is the event?",
            "How can I register?",
            "What are the prizes?",
            "Where can I stay?",
            "What events are there?",
            "Tell me the rules",
            "Who to contact?",
            "Thank you"
        ]
        
        print("\n💬 Testing responses:")
        print("-" * 40)
        
        for i, test_input in enumerate(test_cases, 1):
            try:
                response = bot.process_message(test_input)
                print(f"{i:2d}. Input:  '{test_input}'")
                print(f"    Output: '{response}'")
                print()
            except Exception as e:
                print(f"{i:2d}. Input:  '{test_input}'")
                print(f"    Error:  {e}")
                print()
        
        print("✅ All tests completed!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all dependencies are installed: pip install -r requirements.txt")
        return False
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        print("Make sure you're running this from the backend directory")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_api_endpoint():
    """Test the API endpoint (requires server to be running)"""
    print("\n🌐 Testing API Endpoint...")
    print("=" * 40)
    
    try:
        import requests
        
        # Test the API endpoint
        url = "http://127.0.0.1:5000/chat"
        test_data = {"message": "Hello"}
        
        print("📡 Sending request to API...")
        response = requests.post(url, json=test_data, timeout=5)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ API Response: {result.get('reply', 'No reply')}")
            return True
        else:
            print(f"❌ API Error: HTTP {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API server")
        print("Make sure the chatbot server is running: python app.py")
        return False
    except ImportError:
        print("❌ requests library not found")
        print("Install it with: pip install requests")
        return False
    except Exception as e:
        print(f"❌ API test error: {e}")
        return False

def main():
    print("🤖 Chatbot Integration Test Suite")
    print("=" * 50)
    
    # Test chatbot functionality
    chatbot_ok = test_chatbot()
    
    # Test API endpoint (optional)
    print("\n" + "=" * 50)
    api_ok = test_api_endpoint()
    
    # Summary
    print("\n📊 Test Summary:")
    print("-" * 20)
    print(f"Chatbot Logic: {'✅ PASS' if chatbot_ok else '❌ FAIL'}")
    print(f"API Endpoint:  {'✅ PASS' if api_ok else '❌ FAIL'}")
    
    if chatbot_ok and api_ok:
        print("\n🎉 All tests passed! The chatbot is ready to use.")
        return 0
    elif chatbot_ok:
        print("\n⚠️  Chatbot logic works, but API server is not running.")
        print("Start the server with: python app.py")
        return 1
    else:
        print("\n❌ Some tests failed. Check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
