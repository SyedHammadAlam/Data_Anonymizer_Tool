import pandas as pd
import numpy as np
import random
import os
import sys

# Check if the dataset exists
if not os.path.exists('data.csv'):
    print(" Error! data.csv not found ")
    print("➡️  Please place data.csv in same folder")
    sys.exit(1)

# Load the dataset
df = pd.read_csv('data.csv')

numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()    # Separate numerical and categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

def apply_differential_privacy(column, epsilon):
    sensitivity = column.max() - column.min()      # Differential Privacy Function
    noise = np.random.laplace(0, sensitivity / epsilon, size=column.shape)
    return column + noise

def suppress_column(col):
    return col.apply(lambda x: '*' * len(str(x)))      # Suppression Function


def generalize_column(col):
    return col.apply(lambda x: str(x)[:3] + '***' if pd.notnull(x) else x)   # Generalization Function


def synthetic_replace_column(col):
    unique_vals = col.dropna().unique()       # Synthetic Replacement Function
    synthetic_vals = {val: f"Category_{i}" for i, val in enumerate(unique_vals)}
    return col.map(synthetic_vals)


print("\n Numerical Columns:", numerical_cols)   # User Inputs
num_privacy_settings = {}
for col in numerical_cols:
    while True:
        try:
            epsilon = float(input(f" Enter epsilon (privacy level) for numerical column '{col}': "))
            if epsilon <= 0:
                print(" Epsilon must be greater than 0.")
                continue
            num_privacy_settings[col] = epsilon
            break
        except ValueError:
            print(" Please enter a valid number for epsilon.")

print("\n Categorical Columns:", categorical_cols)
cat_privacy_settings = {}
for col in categorical_cols:
    print(f"\nChoose anonymization method used for '{col}':")
    print("1) Suppression ")
    print("2) Generalization ")
    print("3) Synthetic Replacement ")
    while True:
        choice = input("Enter choice  till 1 to 3")
        if choice in ['1', '2', '3']:
            cat_privacy_settings[col] = choice
            break
        else:
            print(" Invalid choice")


for col, epsilon in num_privacy_settings.items():   # Apply Differential Privacy
    df[col] = apply_differential_privacy(df[col], epsilon)


for col, method in cat_privacy_settings.items():   # Apply K-Anonymity 
    if method == '1':
        df[col] = suppress_column(df[col])
    elif method == '2':
        df[col] = generalize_column(df[col])
    elif method == '3':
        df[col] = synthetic_replace_column(df[col])

# Save the anonymized dataset
output_file = 'anonymized_pakistan_housing.csv'
df.to_csv(output_file, index=False)

print(f"\nAnonymized dataset saved as '{output_file}' successfully!")
