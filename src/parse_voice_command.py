import spacy

nlp = spacy.load("en_core_web_sm")

def extract_commands(transcript):
    doc = nlp(transcript.lower())
    commands = []
    if "show" in transcript and "pressure" in transcript:
        commands.append("SHOW_BLOOD_PRESSURE")
    if "log" in transcript and "clamp" in transcript:
        commands.append("LOG_CLAMP_TIME")
    return commands
