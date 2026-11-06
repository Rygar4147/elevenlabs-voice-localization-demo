import os
from pathlib import Path
from elevenlabs.client import ElevenLabs

def generate_speech_demo():
    # 1. Check for API key with error handling
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise ValueError(
            "Error: ELEVENLABS_API_KEY environment variable is missing. "
            "Please set it using your terminal before running the script:\n"
            "  export ELEVENLABS_API_KEY='your_api_key_here'"
        )

    # 2. Initialize the ElevenLabs client
    client = ElevenLabs(api_key=api_key)

    # 3. Ensure the input file exists
    input_file = Path("script.txt")
    if not input_file.exists():
        raise FileNotFoundError(
            f"Error: Could not find '{input_file}'. Please create a 'script.txt' file in this directory."
        )

    # Read text from input file
    text_content = input_file.read_text(encoding="utf-8").strip()
    if not text_content:
        raise ValueError("Error: 'script.txt' is empty. Please add text to convert.")

    # 4. Ensure the output folder exists
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # 5. Define target configurations (English and Spanish)
    # Using 'eleven_multilingual_v2' which supports high-fidelity generation across multiple languages
    languages = {
        "english": "en",
        "spanish": "es"
    }

    # Using a popular default voice ID (e.g., "Rachel" or standard default voice)
    # You can replace this with any custom voice ID from your ElevenLabs library
    voice_id = "21m00Tcm4TlvDq8ikWAM" 

    print(f"Loaded script from '{input_file}'. Starting audio generation...\n")

    for lang_name, lang_code in languages.items():
        try:
            print(f"Generating audio for [{lang_name.upper()} ({lang_code})]...")
            
            # Call the ElevenLabs Text-to-Speech API
            audio_stream = client.text_to_speech.convert(
                voice_id=voice_id,
                output_format="mp3_44100_128",
                text=text_content,
                model_id="eleven_multilingual_v2",
            )

            # Define output file path
            output_path = output_dir / f"script_{lang_name}.mp3"

            # Collect the audio generator bytes and write to file
            with open(output_path, "wb") as f:
                for chunk in audio_stream:
                    if chunk:
                        f.write(chunk)

            print(f"Successfully saved: {output_path}")

        except Exception as e:
            print(f"Failed to generate audio for {lang_name}: {e}")

    print("\nAll tasks completed! Check the 'output/' folder for your MP3 files.")

if __name__ == "__main__":
    generate_speech_demo()