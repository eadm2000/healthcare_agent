from .perception import transcribe_audio, extract_events
from .memory import AgentMemory
from .llm_agent import analyze_with_llm
from .actions import take_action

class SurgicalAgent:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.memory = AgentMemory()

    def run_cycle(self, audio_input):
        transcript = transcribe_audio(audio_input)
        self.memory.log_transcript(transcript)

        llm_analysis = analyze_with_llm(transcript)
        events = extract_events(transcript, llm_analysis)

        for event in events:
            action = self.decide_action(event)
            take_action(action, self.patient_id)
            self.memory.log_event(event, action)

    def decide_action(self, event):
        if event["type"] == "emergency":
            return "RAISE_ALERT"
        elif event["type"] == "command":
            return event["action"]
        return "NO_ACTION"
