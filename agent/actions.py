def take_action(action, patient_id):
    if action == "RAISE_ALERT":
        print(f"🚨 Alert raised for patient {patient_id}!")
    elif action == "LOG_CLAMP":
        print(f"📝 Clamp time logged for patient {patient_id}.")
    else:
        print(f"ℹ️ No action needed.")
