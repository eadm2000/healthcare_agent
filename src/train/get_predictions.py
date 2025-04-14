from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
classifier = LogisticRegression()

# Training phase
X_train = vectorizer.fit_transform(["minor bleeding", "heavy bleeding", "routine", "complication occurred"])
y_train = [0, 1, 0, 1]
classifier.fit(X_train, y_train)

# Prediction
def predict_risk(transcript):
    x = vectorizer.transform([transcript])
    return classifier.predict_proba(x)[0][1]  # Probability of complication
