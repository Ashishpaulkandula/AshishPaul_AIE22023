def create_one_hot_mapping(unique_categories):
    #Create a mapping between unique categories and their corresponding one-hot encoding vectors.
    return {category: [1 if category == unique_category else 0 for unique_category in unique_categories] for category in unique_categories}

def one_hot_encode_categorical(data, one_hot_mapping):
   
    #One-hot encode categorical data using a pre-defined mapping.
    return [one_hot_mapping[category] for category in data]
if __name__ == "__main__":
    # categorical data
    categorical_data = ["red", "green", "blue", "red", "green"]

    # Create a mapping for one-hot encoding
    unique_categories = list(set(categorical_data))
    one_hot_mapping = create_one_hot_mapping(unique_categories)

    # One-hot encode the categorical data
    one_hot_encoded_data = one_hot_encode_categorical(categorical_data, one_hot_mapping)

   
    print("Original Categorical Data:", categorical_data)
    print("One-Hot Encoded Data:")
    for category, one_hot_vector in zip(categorical_data, one_hot_encoded_data):
        print(f"{category}: {one_hot_vector}")
