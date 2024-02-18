import numpy as np
import pandas as pd
     

file_name = "E:\Machine Learning(python)\Lab Session1 Data.xlsx"
df = pd.read_excel(file_name, sheet_name="IRCTC Stock Price")
     

df.head()
def calculate_mean_and_variance(data):
    """
    Calculate mean and variance of a given dataset.
    """
    mean = data.mean()
    variance = data.var()
    return mean, variance

def sample_mean(data, condition_column, condition_value):
    """
    Calculate the sample mean of a subset of data based on a given condition.
    """
    subset_mean = data[data[condition_column] == condition_value]['Price'].mean()
    return subset_mean

def probability_of_loss(data):
    """
    Calculate the probability of making a loss based on a given dataset.
    """
    loss_probability = len(data[data["Chg%"] < 0]) / len(data)
    return loss_probability

price_mean, price_variance = calculate_mean_and_variance(df["Price"])
wednesday_mean = sample_mean(df, 'Day', 'Wed')
april_mean = sample_mean(df, 'Month', 'Apr')
loss_probability = probability_of_loss(df)

print("Mean of Price:", price_mean)
print("Variance of Price:", price_variance)
print("Sample mean of Wednesday prices:", wednesday_mean)
print("Comparison with population mean for Wednesday prices:", wednesday_mean - price_mean)
print("Sample mean of April prices:", april_mean)
print("Comparison with population mean for April prices:", april_mean - price_mean)
print("Probability of making a loss:", loss_probability)
