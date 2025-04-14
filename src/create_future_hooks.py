def fuse_modalities(transcript, vitals, video_events):
    return {
        "summary": generate_surgical_report(transcript),
        "vitals_snapshot": vitals,
        "video_events": video_events
    }
