# 📰 Fake News Detection using Flask & Machine Learning  

This is a Flask-based web application that predicts whether a given news article is **Real** or **Fake** using a trained machine learning model.  

---

## ✨ Features  
✅ Train a **Logistic Regression** model on a dataset of news articles  
✅ Use **TF-IDF Vectorization** for text processing  
✅ Save and load the trained model for predictions  
✅ Flask-based **API with a simple front-end** for making predictions  

---

## 📦 Prerequisites  
Ensure you have the following installed:  
🔹 **Python 3.x**  
🔹 **Flask**  
🔹 **Scikit-learn**  
🔹 **Pandas**  
🔹 **Numpy**  

Install dependencies using:  
```sh
pip install flask scikit-learn pandas numpy
```

---

## ⚡ Training the Model  
Before running the Flask app, you need to train the model:  

1. Place your dataset (`news.csv`) in the correct path:  
   ```
   C:\projects\machine learning\fake-news-detect\dataset\news.csv
   ```

2. Run the training script:  
   ```sh
   python train-model.py
   ```

3. This will:  
   ✅ Train the model using **TF-IDF Vectorization** and **Logistic Regression**  
   ✅ Save the trained model as **`model.pkl`**  
   ✅ Save the vectorizer as **`vectorizer.pkl`**  

**📌 `model.pkl` and `vectorizer.pkl` are required to run the Flask app!**  

---

## 🚀 Running the Flask App  
Once the model is trained, start the Flask application:  

```sh
python app.py
```

Then, open your browser and go to:  
```
http://127.0.0.1:5000/
```

---

## 📂 Project Structure  
```
fake-news-detection/
│── dataset/
│   ├── news.csv  # 📰 Training dataset
│── templates/
│   ├── index.html  # 🎨 Frontend for user input
│── app.py          # 🚀 Flask application
│── train-model.py  # 🏋️ Model training script
│── model.pkl       # 🔥 Trained machine learning model
│── vectorizer.pkl  # 📖 TF-IDF vectorizer for text transformation
│── README.md       # 📖 Project documentation
```

---

## 🎯 How It Works  
1️⃣ The user enters a news article in the **frontend** (index.html).  
2️⃣ The Flask API receives the text and processes it using `vectorizer.pkl`.  
3️⃣ The transformed text is passed to the trained model (`model.pkl`) for prediction.  
4️⃣ The result is returned as **"Real"** or **"Fake"**.  

---

## 🔥 Notes  
⚠️ **Ensure you train the model first before running `app.py`.**  
⚠️ **Make sure `model.pkl` and `vectorizer.pkl` are present in the project directory.**  

