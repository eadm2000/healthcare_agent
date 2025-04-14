from agent.base_agent import SurgicalAgent

agent = SurgicalAgent(patient_id="12345")
agent.run_cycle(audio_input="audio/surgery.wav")
