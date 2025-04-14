from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_with_llm(transcript):
    prompt = f"""You are a surgical AI assistant. Analyze this transcript for:
1. Emergencies or complications
2. Any medical instructions or anomalies
Transcript:
\"\"\"
{transcript}
\"\"\"
Respond with key points in a human-readable summary.
"""
    response = OpenAI().chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content
