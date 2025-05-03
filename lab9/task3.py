import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import tree
import matplotlib.pyplot as plt

# Sample dataset - in practice you would load this from a CSV file
data = {
    'total_spending': [1200, 800, 1500, 600, 2000, 900, 1800, 500, 2200, 750],
    'age': [35, 28, 42, 25, 45, 30, 38, 22, 50, 27],
    'visits': [8, 5, 10, 3, 12, 6, 9, 2, 15, 4],
    'purchase_frequency': [4, 2, 6, 1, 8, 3, 5, 1, 10, 2],
    'value_category': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1=high-value, 0=low-value
}

df = pd.DataFrame(data)

# Feature scaling
scaler = StandardScaler()
X = df.drop('value_category', axis=1)
y = df['value_category']
X_scaled = scaler.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Train Decision Tree model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
tree.plot_tree(model, 
               feature_names=X.columns, 
               class_names=['Low', 'High'], 
               filled=True, 
               rounded=True)
plt.title("Decision Tree for Customer Value Classification")
plt.show()

# Feature importance
importance = model.feature_importances_
features = X.columns
plt.barh(features, importance)
plt.xlabel("Feature Importance")
plt.title("Feature Importance for Customer Value Prediction")
plt.show()

# Example of classifying a new customer
new_customer = np.array([[1800, 40, 10, 6]])  # total_spending, age, visits, purchase_frequency
new_customer_scaled = scaler.transform(new_customer)
prediction = model.predict(new_customer_scaled)
print(f"\nNew customer classification: {'High-value' if prediction[0] == 1 else 'Low-value'}")
