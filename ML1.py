def count_pairs(lst,target_sum):
    """
    Parameters:
    - lst (list): The input list of integers.
    - target_sum (int): The target sum to check for.

    """
    count = 0

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target_sum:
                count += 1

    return count

def main():
    #input for the list of integers
    given_list = input("Enter a list of integers separated by spaces: ")
    given_list = [int(x) for x in given_list.split()]

    #input for the target sum
    target_sum = int(input("Enter the target sum: "))

    # Calling the function to count pairs with the specified sum
    result = count_pairs(given_list, target_sum)

    print(f"Number of pairs with sum {target_sum}: {result}")

if __name__ == "__main__":
    main()
