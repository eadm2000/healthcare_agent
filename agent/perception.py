import whisper
import spacy

model = whisper.load_model("base")
nlp = spacy.load("en_core_web_sm")

def transcribe_audio(audio_path):
    return model.transcribe(audio_path)["text"]

def extract_events(transcript, llm_summary):
    doc = nlp(transcript)
    events = []

    if "bleeding" in transcript:
        events.append({"type": "emergency", "description": "Possible hemorrhage"})
    if "log clamp" in transcript.lower():
        events.append({"type": "command", "action": "LOG_CLAMP"})

    # You can enrich events with LLM interpretations here
    if "unexpected" in llm_summary.lower():
        events.append({"type": "warning", "description": "Unexpected event from LLM"})

    return events
