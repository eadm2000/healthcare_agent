def explain_for_patient(transcript):
    return summarizer("Explain this to a patient: " + transcript, max_length=100, min_length=20, do_sample=False)[0]['summary_text']
