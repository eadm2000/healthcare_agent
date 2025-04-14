def update_ehr(patient_id, report):
    # Mock EHR API call
    print(f"📤 Sending report to EHR for patient {patient_id}...")
    print(report)
    return {"status": "success"}
