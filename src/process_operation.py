def process_operation(audio_path, patient_id, vitals=None, video_events=None):
    transcript = transcribe_audio(audio_path)
    print("📝 Transcript:", transcript)

    alerts = check_for_alerts(transcript)
    print("🚨 Alerts:", alerts)

    commands = extract_commands(transcript)
    print("🎙 Commands Detected:", commands)

    report = generate_surgical_report(transcript)
    print("📋 Surgical Report:", report)

    safety_issues = detect_safety_issues(transcript)
    print("⚠️ Safety Issues:", safety_issues)

    update_ehr(patient_id, report)

    risk_score = predict_risk(transcript)
    print("🧮 Risk Score:", risk_score)

    if vitals and video_events:
        fused = fuse_modalities(transcript, vitals, video_events)
        print("🧠 Fused Data Snapshot:", fused)

    patient_friendly = explain_for_patient(transcript)
    print("👩‍⚕️ Patient Explanation:", patient_friendly)

    return {
        "alerts": alerts,
        "commands": commands,
        "report": report,
        "risk_score": risk_score,
        "safety_issues": safety_issues,
        "patient_friendly": patient_friendly
    }
