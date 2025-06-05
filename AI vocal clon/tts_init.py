from TTS.api import TTS

def initialize_tts():
    try:
        # List all available models
        available_models = TTS.list_models()
        print("Available TTS Models:")
        for model in available_models:
            print(f"- {model}")
        
        # Initialize TTS with a suitable model for voice cloning
        # We'll use the YourTTS model which is good for voice cloning
        tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=True)
        return tts, True
    except Exception as e:
        print(f"Error initializing TTS: {str(e)}")
        return None, False

if __name__ == "__main__":
    tts, success = initialize_tts()
    if success:
        print("TTS initialized successfully!")
    else:
        print("Failed to initialize TTS system.")