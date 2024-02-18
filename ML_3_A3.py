import pandas as pd

def categorize_customers(payment_values, threshold=200):
    
    #Categorize customers as RICH or POOR based on payment values.

    categories = ["RICH" if payment > threshold else "POOR" for payment in payment_values]
    return categories

if __name__ == "__main__":
    # Main program
    file_path = "E:\Machine Learning(python)\Lab Session1 Data.xlsx"
    sheet_name = "Purchase data"

    # Load data
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Categorize customers
    payment_values = df.iloc[:, 4].values
    customer_categories = categorize_customers(payment_values)

    # Print customer categories
    print("Customer Categories:", customer_categories)
