# House Price Prediction Model

This is a simple linear regression model that predicts house prices based on the square footage of the living area, number of bedrooms and bathrooms, and the year the house was built. The model is trained on a dataset of house prices from a certain area, and can be used to predict the price of a house with similar features.

## Getting Started

To get started with this project, you'll need to have Python 3 and the following packages installed:

- pandas
- numpy
- scikit-learn

You can install these packages using pip:
```
pip install pandas numpy scikit-learn
```
Once you have these packages installed, you can run the model using the following command:
```
python house_price_prediction.py
```

## Data

The dataset used to train the model is stored in a CSV file called `house_prices.csv`. This file contains the following columns:

- `date`: the date the house was sold
- `price`: the price of the house in dollars
- `sqft_living`: the square footage of the living area
- `bedrooms`: the number of bedrooms
- `bathrooms`: the number of bathrooms
- `year`: the year the house was built

## Model

The model used in this project is a simple linear regression model. It takes in the square footage of the living area, number of bedrooms and bathrooms, and the year the house was built as input, and predicts the price of the house as output.

The model is trained on a randomly selected 80% of the data, and tested on the remaining 20%. The mean squared error (MSE) of the model on the test data is used as a measure of its performance.

## Results

The mean squared error (MSE) of the model on the test data is XXXXX. This indicates that the model is able to predict the price of a house with reasonable accuracy based on its features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details
