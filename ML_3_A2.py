import pandas as pd
import numpy as np

def load_data(file_path, sheet_name):
    return pd.read_excel(file_path, sheet_name=sheet_name)

def segregate_data(df):
    A = df.iloc[:, 1:4].values
    C = df.iloc[:, 4].values
    return A, C

def compute_cost_vector(A, C):
    pseudo_inverse_A = np.linalg.pinv(A)
    return np.dot(pseudo_inverse_A, C)

if __name__ == "__main__":
    file_path = "E:\Machine Learning(python)\Lab Session1 Data.xlsx"
    sheet_name = "Purchase data"

    df = load_data(file_path, sheet_name)
    A, C = segregate_data(df)
    cost_vector = compute_cost_vector(A, C)

    print("Cost of each product:", cost_vector)
