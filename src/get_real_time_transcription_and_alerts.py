import whisper

# Load Whisper model (for transcription)
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

# Example alert trigger
def check_for_alerts(transcript):
    alerts = []
    if "bleeding" in transcript or "clamp" in transcript:
        alerts.append("⚠️ Alert: Potential complication or tool request.")
    return alerts
