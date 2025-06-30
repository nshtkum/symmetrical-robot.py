from gtts import gTTS

def generate_tts_audio(text, language='en', output_file='output_audio.mp3'):
    try:
        tts = gTTS(text=text, lang=language)
        tts.save(output_file)
        print(f"[✓] Audio saved as: {output_file}")
        return output_file
    except Exception as e:
        print(f"[!] Error in TTS generation: {e}")
        return None
