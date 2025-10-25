#!/usr/bin/env python3
"""
Tortoise TTS Socket Client Examples

This file shows different ways to use the Tortoise TTS socket client
for testing and development purposes.
"""

import tortoise.socket_client
import time
import random

def basic_example():
    """
    Basic example - just send one text with one voice
    """
    print("🔤 Basic Example")
    print("-" * 30)
    
    voice = "deniro"
    text = "This is a basic example of Tortoise TTS."
    server_ip = "localhost"  # Change to your server IP
    server_port = 5000
    
    try:
        tortoise.socket_client.send_text_to_server(voice, text, server_ip, server_port)
        print("✓ Basic example completed!")
    except Exception as e:
        print(f"❌ Error: {e}")

def multiple_voices_example():
    """
    Test multiple different voices with the same text
    """
    print("\n🎭 Multiple Voices Example")
    print("-" * 30)
    
    voices = ["deniro", "freeman", "emma", "daniel"]
    text = "Testing different voices with the same text."
    server_ip = "localhost"  # Change to your server IP
    server_port = 5000
    
    for voice in voices:
        print(f"🔄 Testing voice: {voice}")
        try:
            tortoise.socket_client.send_text_to_server(voice, text, server_ip, server_port)
            print(f"✓ Voice '{voice}' completed!")
            time.sleep(1)  # Small pause between voices
        except Exception as e:
            print(f"❌ Error with voice '{voice}': {e}")

def different_texts_example():
    """
    Test the same voice with different types of text
    """
    print("\n📝 Different Texts Example")
    print("-" * 30)
    
    voice = "freeman"  # Morgan Freeman voice
    texts = [
        "Hello, this is a simple greeting.",
        "The quick brown fox jumps over the lazy dog.",
        "To be or not to be, that is the question.",
        "In a world where AI can speak, anything is possible.",
        "Testing numbers: one, two, three, four, five."
    ]
    server_ip = "localhost"  # Change to your server IP
    server_port = 5000
    
    for i, text in enumerate(texts, 1):
        print(f"🔄 Testing text {i}/{len(texts)}: {text[:30]}...")
        try:
            tortoise.socket_client.send_text_to_server(voice, text, server_ip, server_port)
            print(f"✓ Text {i} completed!")
            time.sleep(1)  # Small pause between texts
        except Exception as e:
            print(f"❌ Error with text {i}: {e}")

def random_combinations_example():
    """
    Test random combinations of voices and texts
    """
    print("\n🎲 Random Combinations Example")
    print("-" * 30)
    
    voices = ["deniro", "freeman", "emma", "daniel", "halle"]
    texts = [
        "Random testing is fun!",
        "This voice sounds interesting.",
        "Let's see how this combination works.",
        "Artificial intelligence is amazing.",
        "Welcome to the future of text-to-speech."
    ]
    server_ip = "localhost"  # Change to your server IP
    server_port = 5000
    
    # Generate 3 random combinations
    for i in range(3):
        voice = random.choice(voices)
        text = random.choice(texts)
        
        print(f"🔄 Random test {i+1}: voice='{voice}', text='{text[:30]}...'")
        try:
            tortoise.socket_client.send_text_to_server(voice, text, server_ip, server_port)
            print(f"✓ Random test {i+1} completed!")
            time.sleep(1)
        except Exception as e:
            print(f"❌ Error in random test {i+1}: {e}")

def custom_server_example():
    """
    Example for connecting to a custom server (different IP/port)
    """
    print("\n🌐 Custom Server Example")
    print("-" * 30)
    
    # Customize these values for your setup
    voice = "deniro"
    text = "Testing connection to a custom server."
    server_ip = "192.168.1.100"  # Change to your actual server IP
    server_port = 8080           # Change to your actual server port
    
    print(f"Attempting to connect to {server_ip}:{server_port}")
    
    try:
        tortoise.socket_client.send_text_to_server(voice, text, server_ip, server_port)
        print("✓ Custom server example completed!")
    except ConnectionRefusedError:
        print(f"❌ Could not connect to {server_ip}:{server_port}")
        print("Make sure the server is running and the IP/port are correct.")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """
    Main function to run all examples
    """
    print("🎤 Tortoise TTS Socket Client Examples")
    print("=" * 50)
    print("Choose which example to run:")
    print("1. Basic example")
    print("2. Multiple voices example")
    print("3. Different texts example")
    print("4. Random combinations example")
    print("5. Custom server example")
    print("6. Run all examples")
    
    choice = input("\nEnter your choice (1-6): ").strip()
    
    if choice == "1":
        basic_example()
    elif choice == "2":
        multiple_voices_example()
    elif choice == "3":
        different_texts_example()
    elif choice == "4":
        random_combinations_example()
    elif choice == "5":
        custom_server_example()
    elif choice == "6":
        print("🚀 Running all examples...")
        basic_example()
        multiple_voices_example()
        different_texts_example()
        random_combinations_example()
        print("\n⚠️  Skipping custom server example (requires manual configuration)")
    else:
        print("Invalid choice. Running basic example...")
        basic_example()

if __name__ == "__main__":
    main()