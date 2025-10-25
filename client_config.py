# Tortoise TTS Client Configuration
# Edit these values to match your setup

# Server settings
SERVER_IP = "localhost"      # Change to your server's IP address
SERVER_PORT = 5000          # Change to your server's port

# Default voice to use
DEFAULT_VOICE = "deniro"    # Available voices: angie, applejack, daniel, deniro, 
                           # emma, freeman, geralt, halle, jlaw, lj, mol, pat, 
                           # rainbow, snakes, tim_reynolds, tom, weaver, william

# Default text for testing
DEFAULT_TEXT = "Hello world, this is a test of Tortoise TTS."

# Audio settings (these are handled by the socket_client, just for reference)
SAMPLE_RATE = 24000        # Audio sample rate
CHANNELS = 1               # Mono audio
AUDIO_DTYPE = "float32"    # Audio data type