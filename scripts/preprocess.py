import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample

# Load datasets
fake_users = pd.read_csv("fusers.csv")
real_users = pd.read_csv("users.csv")

# Add labels
fake_users["label"] = 1
real_users["label"] = 0

# Merge datasets
data = pd.concat([fake_users, real_users], ignore_index=True)

# Map language codes to numbers
lang_mapping = {"de": 1, "en": 2, "es": 3, "fr": 4, "gl": 5, "it": 6, "nl": 7, "tr": 8}
data["lang"] = data["lang"].map(lang_mapping)

# Select only numerical columns
columns_to_keep = ["fav_number", "statuses_count", "followers_count", 
                   "friends_count", "favourites_count", "listed_count", "lang", "label"]
data = data[columns_to_keep]

# Handle missing values (fill with mean for numerical columns)
numerical_features = [col for col in columns_to_keep if col != "label"]
data[numerical_features] = data[numerical_features].fillna(data[numerical_features].mean())

# Balance dataset
fake_count = data[data["label"] == 1].shape[0]
real_count = data[data["label"] == 0].shape[0]
if fake_count < real_count:
    real_downsampled = resample(data[data["label"] == 0],
                                replace=False,
                                n_samples=fake_count,
                                random_state=42)
    data = pd.concat([real_downsampled, data[data["label"] == 1]])

# Split data
X = data.drop("label", axis=1)
y = data["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize numerical features
scaler = StandardScaler()
X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])
X_test[numerical_features] = scaler.transform(X_test[numerical_features])

# Hyperparameter tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring='accuracy')
grid_search.fit(X_train, y_train)

# Train model with best parameters
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

# Save the trained model and scaler
with open("fake_user_detector.pkl", "wb") as model_file:
    pickle.dump(best_model, model_file)

with open("scaler.pkl", "wb") as scaler_file:
    pickle.dump(scaler, scaler_file)

# Predict and evaluate
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))

data.to_csv("preprocessed_data.csv", index=False)
