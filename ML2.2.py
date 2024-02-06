import numpy as np
def euclidean_distance(point1, point2):
    #Calculate the Euclidean distance between two points.
    return np.sqrt(np.sum((point1 - point2) ** 2))
def find_neighbors(training_data, test_point, k):

    #Find the k nearest neighbors of a test point in the training data.
    
    distances = np.array([euclidean_distance(test_point, x) for x in training_data])
    return np.argsort(distances)[:k]

def kNN_classifier(training_data, labels, test_point, k):
    
    #Implement the k-NN classifier for a test point.
    
    neighbors = find_neighbors(training_data, test_point, k)
    neighbor_labels = labels[neighbors]
    unique_labels, counts = np.unique(neighbor_labels, return_counts=True)
    return unique_labels[np.argmax(counts)]
if __name__ == "__main__":
    # training data and labels
    training_data = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    labels = np.array([0, 0, 1, 1])
    test_point = np.array([4.5, 5])
    k_value = 3

    # Classify the test point using k-NN classifier
    predicted_label = kNN_classifier(training_data, labels, test_point, k_value)
    print(f"Predicted Label: {predicted_label}")
