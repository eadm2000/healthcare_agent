from transformers import pipeline

summarizer = pipeline("summarization")

def generate_surgical_report(transcript):
    return summarizer(transcript, max_length=200, min_length=30, do_sample=False)[0]['summary_text']
