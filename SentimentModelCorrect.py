import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the crime dataset from the JSON file
with open("crime_dataset.json", "r") as json_file:
    crime_data = json.load(json_file)

# Extract descriptions and danger levels
descriptions = [entry["description"] for entry in crime_data]
danger_levels = [entry["danger_level"] for entry in crime_data]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(descriptions, danger_levels, test_size=0.5, random_state=42)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=1000)  # You can adjust max_features based on your dataset size

# Fit and transform the training data
X_train_tfidf = vectorizer.fit_transform(X_train)

# Transform the testing data
X_test_tfidf = vectorizer.transform(X_test)

# Create a RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=50, random_state=42)

# Train the classifier
classifier.fit(X_train_tfidf, y_train)

# Make predictions on the testing data
y_pred = classifier.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", report)

#export the model
joblib.dump(vectorizer, "tfidf_vectorizer.joblib")
joblib.dump(classifier, "random_forest_classifier.joblib")




# Test the model with a new crime description
new_crime_description = ""

# Transform the new description using the same vectorizer
new_description_tfidf = vectorizer.transform([new_crime_description])

# Predict the danger level for the new description
predicted_danger_level = classifier.predict(new_description_tfidf)[0]

print(f"Predicted Danger Level for the new crime: {predicted_danger_level}")