def count_highest_occurrence(input_string):
    """
    Parameters:
    - input_string (str): The input string.

    """
    #Occurrences of alphabets
    alphabet_count = {}
    for char in input_string:
        if char.isalpha():
            char_lower = char.lower()
            alphabet_count[char_lower] = alphabet_count.get(char_lower, 0) + 1

    # Finding the maximum occurrence count
    max_count = max(alphabet_count.values())

    # Filter characters with the same maximum occurrence count
    repeating_chars = [(char, count) for char, count in alphabet_count.items() if count == max_count]

    return repeating_chars

def main():
    #User input for the input string
    input_str = input("Enter a string: ")

    #Function to count characters with the same occurrence count
    repeating_chars = count_highest_occurrence(input_str)

   
    if not repeating_chars:
        print("No repeating characters found.")
    else:
        print("Characters repeating: ")
        for char, count in repeating_chars:
            print(f"'{char}' - {count} times.")

if __name__ == "__main__":
    main()
