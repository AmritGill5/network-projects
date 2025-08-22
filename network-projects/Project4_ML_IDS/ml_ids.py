import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample dataset (replace with real dataset if available)
data = {
    "duration": [0, 2, 0, 3, 0, 1],
    "src_bytes": [181, 239, 235, 0, 5450, 0],
    "dst_bytes": [5450, 486, 1337, 0, 239, 123],
    "label": ["normal", "attack", "normal", "attack", "normal", "attack"]
}
df = pd.DataFrame(data)

# Split data
X = df.drop("label", axis=1)
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Test on new traffic
new_data = [[2, 300, 200]]  # duration, src_bytes, dst_bytes
print("Prediction:", model.predict(new_data))
