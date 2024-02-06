def create_label_mapping(unique_categories):
   #Create a mapping between unique categories and their corresponding numerical labels.
     return {category: label for label, category in enumerate(unique_categories)}
def label_encode_categorical(data, label_mapping):
    #Label encode categorical data using a pre-defined mapping.
   return [label_mapping[category] for category in data]t
if __name__ == "__main__":
    # Get user input for categorical data
    categorical_data = input("Enter categorical data (comma-separated): ").split(',')
   # Create a mapping for label encoding
    unique_categories = list(set(categorical_data))
    category_label_mapping = create_label_mapping(unique_categories)
   # Label encode the categorical data
    numeric_labels = label_encode_categorical(categorical_data, category_label_mapping)
   # Print
    print("Original Categorical Data:", categorical_data)
    print("Numeric Labels:", numeric_labels)
    print("Category to Label Mapping:", category_label_mapping)
