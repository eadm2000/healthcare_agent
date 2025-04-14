import streamlit as st
import os
import sys
sys.path.append(os.path.abspath('/Users/sarahlenet/Desktop/Surgical Agent/surgical_env/lib/python3.11/site-packages'))
import whisper
from transformers import pipeline
import spacy
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

# --- Load Models ---
st.cache_resource
def load_models():
    whisper_model = whisper.load_model("base")
    summarizer = pipeline("summarization")
    nlp = spacy.load("en_core_web_sm")
    return whisper_model, summarizer, nlp

whisper_model, summarizer, nlp = load_models()

# --- Classifier Mock Training ---
@st.cache_resource
def train_classifier():
    vectorizer = TfidfVectorizer()
    classifier = LogisticRegression()
    X_train = vectorizer.fit_transform(["minor bleeding", "heavy bleeding", "routine", "complication occurred"])
    y_train = [0, 1, 0, 1]
    classifier.fit(X_train, y_train)
    return vectorizer, classifier

vectorizer, classifier = train_classifier()

# --- Functions ---
def transcribe_audio(audio):
    return whisper_model.transcribe(audio)['text']

def check_for_alerts(transcript):
    return [a for a in ["bleeding", "clamp", "emergency"] if a in transcript.lower()]

def extract_commands(transcript):
    doc = nlp(transcript.lower())
    if "log clamp" in transcript:
        return ["LOG_CLAMP_TIME"]
    if "show pressure" in transcript:
        return ["SHOW_BLOOD_PRESSURE"]
    return []

def generate_surgical_report(transcript):
    return summarizer(transcript, max_length=200, min_length=30, do_sample=False)[0]['summary_text']

def explain_for_patient(transcript):
    return summarizer("Explain this for a patient: " + transcript, max_length=100, min_length=20, do_sample=False)[0]['summary_text']

def predict_risk(transcript):
    x = vectorizer.transform([transcript])
    return classifier.predict_proba(x)[0][1]

def detect_safety_issues(transcript):
    return [word for word in ["oops", "mistake", "wrong", "problem", "emergency"] if word in transcript.lower()]

def update_ehr(patient_id, report):
    return f"✅ Report sent to EHR for patient {patient_id}."

# --- Streamlit App ---
st.title("🩺 Surgical Assistant Agent (Prototype)")

audio_file = st.file_uploader("Upload Surgical Audio (WAV/MP3)", type=["wav", "mp3"])
patient_id = st.text_input("Patient ID", "patient_001")

if audio_file and st.button("🧠 Process Audio"):
    with st.spinner("Transcribing..."):
        transcript = transcribe_audio(audio_file)

    st.subheader("📝 Transcript")
    st.text_area("Full Transcript", transcript, height=200)

    st.subheader("🚨 Alerts")
    st.write(check_for_alerts(transcript))

    st.subheader("🎙 Voice Commands")
    st.write(extract_commands(transcript))

    st.subheader("📋 Surgical Report")
    st.write(generate_surgical_report(transcript))

    st.subheader("👩‍⚕️ Patient Explanation")
    st.write(explain_for_patient(transcript))

    st.subheader("⚠️ Safety Issues")
    st.write(detect_safety_issues(transcript))

    st.subheader("🧮 Complication Risk")
    st.progress(predict_risk(transcript))

    st.subheader("📤 EHR Integration")
    st.success(update_ehr(patient_id, generate_surgical_report(transcript)))

    # Option to save to dataset
    if st.button("💾 Save Transcript to Training Dataset"):
        df = pd.DataFrame([{"transcript": transcript, "alerts": check_for_alerts(transcript)}])
        df.to_csv("training_data.csv", mode='a', header=False, index=False)
        st.success("Saved to training_data.csv!")

