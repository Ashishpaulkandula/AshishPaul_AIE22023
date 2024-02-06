import math

def euclidean_distance(vector1, vector2):
    """Calculating the euclidean distance between two vectors
    (x2-x1)^2+(y2-y1)^2
     """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors should have the same dimension for distance calculation.")
    
    squared_distance = sum((v1 - v2) ** 2 for v1, v2 in zip(vector1, vector2))
    return (squared_distance)**0.5

def manhattan_distance(vector1, vector2):
    """
    Calculating the Manhattan distance between two vectors.
    |x2-x1+|y2-y1|
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimension for distance calculation.")
    
    distance = sum(abs(v1 - v2) for v1, v2 in zip(vector1, vector2))
    return distance

if __name__ == "__main__":
   
    vector_a = [float(x) for x in input("Enter values for vector_a (comma-separated): ").split(',')]
    vector_b = [float(x) for x in input("Enter values for vector_b (comma-separated): ").split(',')]

    # Calculate Euclidean distance
    euclidean_dist = euclidean_distance(vector_a, vector_b)
    print(f"Euclidean Distance: {euclidean_dist}")

    # Calculate Manhattan distance
    manhattan_dist = manhattan_distance(vector_a, vector_b)
    print(f"Manhattan Distance: {manhattan_dist}")
