def detect_safety_issues(transcript):
    red_flags = ["oops", "mistake", "wrong", "problem", "emergency"]
    return [flag for flag in red_flags if flag in transcript]
