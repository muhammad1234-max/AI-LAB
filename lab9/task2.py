import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset - in practice you would load this from a CSV file
data = {
    'email_text': [
        'win money now click here',
        'meeting scheduled for tomorrow',
        'free offer limited time',
        'project update attached',
        'congratulations you won',
        'status report due Friday',
        'claim your prize today',
        'team lunch next week',
        'exclusive deal for you',
        'monthly newsletter attached'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1=spam, 0=not spam
}

df = pd.DataFrame(data)

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(df['email_text'])
y = df['label']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train SVM model
model = SVC(kernel='linear', probability=True)
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
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Example of classifying a new email
new_email = ["free money click now"]
new_email_vec = vectorizer.transform(new_email)
prediction = model.predict(new_email_vec)
print(f"\nNew email classification: {'Spam' if prediction[0] == 1 else 'Not Spam'}")
