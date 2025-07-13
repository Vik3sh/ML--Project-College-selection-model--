from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load model
model = joblib.load('admission_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    try:
        gre = float(data['gre'])
        toefl = float(data['toefl'])
        university_rating = float(data['university_rating'])
        sop = float(data['sop'])
        lor = float(data['lor'])
        cgpa = float(data['cgpa'])
        research = int(data['research'])

        features = np.array([[gre, toefl, university_rating, sop, lor, cgpa, research]])
        prediction = model.predict(features)[0]

        return jsonify({'admission_chance': round(prediction, 2)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
