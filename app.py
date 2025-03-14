from flask import Flask, request, jsonify, render_template_string
import pickle

app = Flask(__name__)

@app.route("/")
def index():

    return render_template_string(open("template/index.html").read())

@app.route('/predict', methods=['POST'])
def predict():
    """Predict if a news article is fake or real."""
    json_data = request.json
    text = json_data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided."}), 400

    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    transformed_text = vectorizer.transform([text]).toarray()

    prediction = model.predict(transformed_text)
    result = "Real" if prediction[0] == 1 else "Fake"
    return jsonify({"prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
