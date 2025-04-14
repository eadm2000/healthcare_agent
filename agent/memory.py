class AgentMemory:
    def __init__(self):
        self.transcripts = []
        self.events = []

    def log_transcript(self, text):
        self.transcripts.append(text)

    def log_event(self, event, action):
        self.events.append({"event": event, "action": action})
