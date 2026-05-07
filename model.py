import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_category(filename):
    X = vectorizer.transform([filename])
    return model.predict(X)[0]
