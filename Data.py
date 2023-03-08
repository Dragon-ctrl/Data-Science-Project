import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

# Load the data from CSV file
data = pd.read_csv("Data/house_prices.csv")

# Convert "date" column to datetime object and extract year
data["date"] = pd.to_datetime(data["date"])
data["year"] = data["date"].dt.year

# Define the input and output variables for the linear regression model
input_cols = ["sqft_living", "bedrooms", "bathrooms", "year"]
output_cols = ["price"]
input_data = data[input_cols]
output_data = data[output_cols]

# Scale the input features
scaler = StandardScaler()
input_data = scaler.fit_transform(input_data)

# Train the linear regression model using cross-validation
model = LinearRegression()
scores = cross_val_score(model, input_data, output_data, cv=5, scoring='neg_mean_squared_error')
mean_mse = -np.mean(scores)
print("Mean squared error:", mean_mse)

# Fit the model to the full dataset
model.fit(input_data, output_data)

# Make predictions on new data
new_data = pd.DataFrame({'sqft_living': [2000], 'bedrooms': [3], 'bathrooms': [2], 'year': [2010]})
new_data_scaled = scaler.transform(new_data)
prediction = model.predict(new_data_scaled)
print("Price prediction:", prediction)
