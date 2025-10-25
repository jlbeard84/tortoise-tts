import tortoise.socket_client
import sys

def test_tortoise_tts():
    """
    Simple test client for Tortoise TTS socket server
    """
    # Available voices (you can check tortoise/voices/ directory for more)
    available_voices = [
        "angie", "applejack", "daniel", "deniro", "emma", "freeman",
        "geralt", "halle", "jlaw", "lj", "mol", "pat", "rainbow", 
        "snakes", "tim_reynolds", "tom", "weaver", "william"
    ]
    
    # Configuration
    voice = "deniro"  # Change this to any available voice
    text = "Hello world, this is a test of Tortoise TTS. How does this sound?"
    server_ip = "192.168.253.242"  # Change to your server IP
    server_port = 5000
    
    print(f"Connecting to Tortoise TTS server at {server_ip}:{server_port}")
    print(f"Using voice: {voice}")
    print(f"Text to speak: {text}")
    print("-" * 50)
    
    try:
        # Send text to server and play audio
        tortoise.socket_client.send_text_to_server(voice, text, server_ip, server_port)
        print("✓ Audio generation and playback completed successfully!")
        
    except ConnectionRefusedError:
        print(f"❌ Error: Could not connect to server at {server_ip}:{server_port}")
        print("Make sure the Tortoise TTS socket server is running.")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False
        
    return True

def interactive_mode():
    """
    Interactive mode where you can test different voices and text
    """
    available_voices = [
        "angie", "applejack", "daniel", "deniro", "emma", "freeman",
        "geralt", "halle", "jlaw", "lj", "mol", "pat", "rainbow", 
        "snakes", "tim_reynolds", "tom", "weaver", "william"
    ]
    
    print("🎤 Tortoise TTS Interactive Test Client")
    print("=" * 40)
    
    # Get server details
    server_ip = input("Enter server IP (default: localhost): ").strip() or "localhost"
    server_port = input("Enter server port (default: 5000): ").strip() or "5000"
    
    try:
        server_port = int(server_port)
    except ValueError:
        print("Invalid port number, using default 5000")
        server_port = 5000
    
    print(f"\nAvailable voices: {', '.join(available_voices)}")
    
    while True:
        print("\n" + "-" * 40)
        voice = input("Enter voice name (or 'quit' to exit): ").strip().lower()
        
        if voice == 'quit':
            break
            
        if voice not in available_voices:
            print(f"❌ Voice '{voice}' not found. Available voices: {', '.join(available_voices)}")
            continue
            
        text = input("Enter text to speak: ").strip()
        if not text:
            print("❌ Text cannot be empty")
            continue
            
        print(f"\n🔄 Generating speech with voice '{voice}'...")
        
        try:
            tortoise.socket_client.send_text_to_server(voice, text, server_ip, server_port)
            print("✓ Success!")
            
        except ConnectionRefusedError:
            print(f"❌ Could not connect to server at {server_ip}:{server_port}")
            print("Make sure the Tortoise TTS socket server is running.")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    print("Tortoise TTS Test Client")
    print("1. Run simple test")
    print("2. Interactive mode")
    
    choice = input("Choose option (1 or 2): ").strip()
    
    if choice == "1":
        test_tortoise_tts()
    elif choice == "2":
        interactive_mode()
    else:
        print("Running simple test by default...")
        test_tortoise_tts()