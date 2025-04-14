import pandas as pd

def create_training_entry(transcript, events):
    return {
        "transcript": transcript,
        "events_detected": events
    }

# Save example
training_data = []
training_data.append(create_training_entry("He said oops and asked for suction", ["oops", "suction"]))
df = pd.DataFrame(training_data)
df.to_csv("training_dataset.csv", index=False)
