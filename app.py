from flask import Flask
import joblib
app = Flask(__name__)
model = joblib.load("model.pkl")
@app.route("/")
def home():
  return "ML Model Deployed!"
app.run(host="0.0.0.0", port=8080)