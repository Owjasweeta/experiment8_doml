from flask import Flask
import joblib
app = Flask(__name__)
model = joblib.load("model.pkl")
@app.route("/")
def home():
  return "ML Model Deployed!"
app.run(host="127.0.0.1", port=5001)
