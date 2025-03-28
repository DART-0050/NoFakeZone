import pickle
import numpy as np

# Load the trained model and scaler
with open("models/fake_user_detector.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("models/scaler.pkl", "rb") as scaler_file:
    scaler = pickle.load(scaler_file)

# Function to test the model
def predict_fake_user(features):
    """
    Predict whether a user is fake or real.
    :param features: List of numerical features in the same order as the training data.
    :return: "Fake User" or "Real User"
    """
    features = np.array(features).reshape(1, -1)
    features = scaler.transform(features)  # Normalize input
    prediction = model.predict(features)
    return "Fake User" if prediction[0] == 1 else "Real User"

# Example test case
sample_user = [4754,574,112,359,39,0,6]  # Modify values as needed
result = predict_fake_user(sample_user)
print(f"Prediction: {result}")
