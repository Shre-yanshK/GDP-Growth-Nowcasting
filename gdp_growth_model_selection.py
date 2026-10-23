# Checking files availability
import os
print(os.listdir('.'))

# Import required libraries for data manipulation, statistical modeling, and evaluation
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the training, testing, and variable description datasets
train = pd.read_csv("ex1_train.csv")
test = pd.read_csv("ex1_test.csv")
variables = pd.read_csv("ex1_variables.csv")

# Check the dimensions of the loaded datasets to ensure proper loading
print("Train shape:", train.shape)
print("Test shape:", test.shape)
print("Variables shape:", variables.shape)

# Separate the independent predictor variables (features) from the target variable y
feature_cols = [c for c in train.columns if c not in ['id', 'y']]
y_train = train['y']

# Add an intercept constant and fit a full OLS regression on all 12 indicators
X_full = sm.add_constant(train[feature_cols])
full_model = sm.OLS(y_train, X_full).fit()

# Display the full OLS regression summary to examine initial coefficients, R-squared, and p-values
print(full_model.summary())

# Run best subset selection across all 4,095 variable combinations
from itertools import combinations

results = []

for k in range(1, len(feature_cols) + 1):
    for combo in combinations(feature_cols, k):
        X_sub = sm.add_constant(train[list(combo)])
        model_sub = sm.OLS(y_train, X_sub).fit()

        results.append({
            "k": k,
            "features": list(combo),
            "aic": model_sub.aic,
            "bic": model_sub.bic,
            "r2_adj": model_sub.rsquared_adj
        })

res_df = pd.DataFrame(results)

# Confirm that all 4,095 models were evaluated
print("Number of models evaluated:", len(res_df))
print("Best-subset results are ready.")

# Find the models with the lowest AIC and BIC scores
best_bic_row = res_df.loc[res_df["bic"].idxmin()]
best_aic_row = res_df.loc[res_df["aic"].idxmin()]

# Print the best feature sets selected by BIC and AIC along with their scores
print("=== BEST BIC MODEL ===")
print(f"Number of features (k): {best_bic_row['k']}")
# Create the required two-column prediction file
submission = pd.DataFrame({
    "id": test["id"],
    "prediction": test_predictions
})

# Save the file as a CSV
submission.to_csv("ex1_Kumar_Shreyansh.csv", index=False)
print("Prediction CSV saved!")
