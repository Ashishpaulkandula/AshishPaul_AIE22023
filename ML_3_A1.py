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

if _name_ == "_main_":
    file_path = "C:\python\Machine_Learning\Lab Session1 Data.xlsx"
    sheet_name = "Purchase data"

    df = load_data(file_path, sheet_name)
    A, C = segregate_data(df)
    cost_vector = compute_cost_vector(A, C)

    dimensionality = A.shape[1]
    num_vectors = A.shape[0]
    rank_A = np.linalg.matrix_rank(A)

    print("Dimensionality of the vector space:", dimensionality)
    print("Number of vectors in the vector space:", num_vectors)
    print("Rank of Matrix A:", rank_A)
    print("Cost of each product:", cost_vector)
