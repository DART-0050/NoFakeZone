import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model and scaler
with open("models/fake_user_detector.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("models/scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get input values from form
            fav_number = int(request.form['fav_number'])
            statuses_count = int(request.form['statuses_count'])
            followers_count = int(request.form['followers_count'])
            friends_count = int(request.form['friends_count'])
            favourites_count = int(request.form['favourites_count'])
            listed_count = int(request.form['listed_count'])
            lang = int(request.form['lang'])

            # Prepare input for model
            user_data = np.array([[fav_number, statuses_count, followers_count,
                                   friends_count, favourites_count, listed_count, lang]])
            user_data = scaler.transform(user_data)
            
            # Predict
            result = model.predict(user_data)[0]
            prediction = "Fake User" if result == 1 else "Real User"
        except Exception as e:
            prediction = f"Error: {str(e)}"
        
        return render_template('result.html', prediction=prediction)

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
