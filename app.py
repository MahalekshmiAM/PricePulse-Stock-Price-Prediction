from flask import Flask, render_template, request
import joblib
import pandas as pd
import datetime

app = Flask(__name__)
model = joblib.load(r'C:\Users\maha\OneDrive\Desktop\stock\stock_price_prediction_model.pkl')
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [
        'Volume', 'Day', 'Month', 'Year', 'Price_Range', 'Daily_Change',
         'Percent_Change', 'Quarter'
    ]
    
    data = {feature: float(request.form.get(feature, 0)) for feature in features}
    
    input_data = pd.DataFrame([data])
    predicted_price = model.predict(input_data)[0]
    recommendation = stock_recommendation(predicted_price)
    return render_template('result.html', input_data=data, predicted_price=predicted_price, recommendation=recommendation)

def stock_recommendation(predicted_price):
    if predicted_price < 1000:
        return "Buy"
    elif predicted_price > 2000:
        return "Sell"
    else:
        return "Hold"

if __name__ == '__main__':
    app.run(debug=True)
nb 