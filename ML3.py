import numpy as np

def matrix_power(mat, exp):
    """
    Parameters:
    - mat (numpy.ndarray): The input square matrix.
    - exp (int): The positive integer exponent.
    """
    result = np.linalg.matrix_power(mat, exp)
    return result

def main():
    # User input for the elements of the square matrix
    rows = int(input("Enter the number of rows in the square matrix: "))
    cols = int(input("Enter the number of columns in the square matrix: "))

    mat_A = []
    for i in range(rows):
        row = [int(x) for x in input(f"Enter elements for row {i + 1} separated by spaces: ").split()]
        mat_A.append(row)

    mat_A = np.array(mat_A)

    # User input for the positive integer exponent
    exp_m = int(input("Enter the positive integer exponent: "))

    # Calling the function to compute Am
    result_matrix = matrix_power(mat_A, exp_m)

    # Printing the result
    print(f"A raised to the power of {exp_m} is:\n{result_matrix}")

if __name__ == "__main__":
    main()
