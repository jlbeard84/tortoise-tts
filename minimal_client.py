#!/usr/bin/env python3
"""
Minimal Tortoise TTS Client

This is the simplest possible client that uses the configuration file.
Perfect for quick testing or as a starting point for your own client.
"""

import tortoise.socket_client
from client_config import SERVER_IP, SERVER_PORT, DEFAULT_VOICE, DEFAULT_TEXT

def quick_test():
    """
    Quick test using configuration file settings
    """
    print("🎤 Quick Tortoise TTS Test")
    print("=" * 30)
    print(f"Server: {SERVER_IP}:{SERVER_PORT}")
    print(f"Voice: {DEFAULT_VOICE}")
    print(f"Text: {DEFAULT_TEXT}")
    print("-" * 30)
    
    try:
        print("🔄 Generating speech...")
        tortoise.socket_client.send_text_to_server(
            DEFAULT_VOICE, 
            DEFAULT_TEXT, 
            SERVER_IP, 
            SERVER_PORT
        )
        print("✓ Success! Audio should have played.")
        
    except ConnectionRefusedError:
        print(f"❌ Could not connect to server at {SERVER_IP}:{SERVER_PORT}")
        print("💡 Tips:")
        print("   - Make sure the Tortoise TTS socket server is running")
        print("   - Check the SERVER_IP and SERVER_PORT in client_config.py")
        print("   - Verify the server is accessible from this machine")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    quick_test()