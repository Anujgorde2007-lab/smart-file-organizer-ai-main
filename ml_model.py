from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data (simple but effective)
files = [
    "resume.pdf",
    "cv.docx",
    "invoice.jpg",
    "bill.pdf",
    "photo.png",
    "image.jpg",
    "report.docx"
]

labels = [
    "Career",
    "Career",
    "Finance",
    "Finance",
    "Images",
    "Images",
    "Documents"
]

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(files)

# Train model
model = MultinomialNB()
model.fit(X, labels)


def predict_category(filename):
    X_test = vectorizer.transform([filename])
    return model.predict(X_test)[0]
