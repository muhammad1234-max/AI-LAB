import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt

# Load the dataset (assuming it's in a CSV file)
# For demonstration, I'll create a sample dataset
data = {
    'square_footage': [1500, 2000, 1750, 2200, 1900, 2400, 2100, 1800, 2300, 2500],
    'bedrooms': [2, 3, 3, 4, 3, 4, 3, 2, 4, 4],
    'bathrooms': [1.5, 2, 2, 2.5, 2, 3, 2, 1.5, 2.5, 3],
    'age': [10, 5, 8, 3, 7, 2, 6, 12, 4, 1],
    'neighborhood': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C', 'A'],
    'price': [250000, 350000, 300000, 420000, 320000, 450000, 380000, 280000, 400000, 480000]
}

df = pd.DataFrame(data)

# Data preprocessing
# Handle categorical variables (neighborhood) using one-hot encoding
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), ['neighborhood'])],
    remainder='passthrough'
)
X = ct.fit_transform(df.drop('price', axis=1))
y = df['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")
print(f"R-squared: {r2:.2f}")

# Predict price for a new house
new_house = pd.DataFrame({
    'square_footage': [2100],
    'bedrooms': [3],
    'bathrooms': [2],
    'age': [5],
    'neighborhood': ['B']
})

new_house_encoded = ct.transform(new_house)
predicted_price = model.predict(new_house_encoded)
print(f"Predicted price for new house: ${predicted_price[0]:,.2f}")

# Visualize actual vs predicted prices
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red')  # Perfect prediction line
plt.show()
