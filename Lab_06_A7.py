import numpy as np

# Initialize weights randomly
def initialize_weights(input_size, hidden_size, output_size):
    np.random.seed(0)
    weights_input_hidden = np.random.uniform(size=(input_size, hidden_size))
    weights_hidden_output = np.random.uniform(size=(hidden_size, output_size))
    return weights_input_hidden, weights_hidden_output

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Forward pass through the network
def forward_pass(inputs, weights_input_hidden, weights_hidden_output):
    hidden_input = np.dot(inputs, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)
    output_input = np.dot(hidden_output, weights_hidden_output)
    output = sigmoid(output_input)
    return output, hidden_output

# Backward pass through the network and weight update
def backward_pass(inputs, output, target, hidden_output, weights_hidden_output, weights_input_hidden, learning_rate):
    output_error = target - output
    output_delta = output_error * sigmoid_derivative(output)
    
    hidden_error = np.dot(output_delta, weights_hidden_output.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)
    
    # Reshape hidden_output to match the expected shape
    hidden_output = hidden_output.reshape(-1, 1)
    
    # Update weights
    weights_hidden_output += learning_rate * np.outer(hidden_output, output_delta)

    weights_input_hidden += learning_rate * np.dot(inputs.T, hidden_delta)

# Training the neural network
def train(X, y, weights_input_hidden, weights_hidden_output, learning_rate, epochs, convergence_threshold):
    for epoch in range(epochs):
        total_error = 0
        for i in range(len(X)):
            output, hidden_output = forward_pass(X[i], weights_input_hidden, weights_hidden_output)
            backward_pass(X[i], output, y[i], hidden_output, weights_hidden_output, weights_input_hidden, learning_rate)
            total_error += np.mean(np.square(y[i] - output))
        if total_error <= convergence_threshold:
            print(f"Converged after {epoch + 1} iterations.")
            break
        elif epoch == epochs - 1:
            print("Did not converge within specified iterations.")

# Testing the trained network
def test(X, weights_input_hidden, weights_hidden_output):
    print("Input\tOutput")
    for i in range(len(X)):
        output, _ = forward_pass(X[i], weights_input_hidden, weights_hidden_output)
        print(f"{X[i]}\t{output}")

def main():
    # Define the AND gate truth table
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [0], [0], [1]])

    # Hyperparameters
    input_size = 2
    hidden_size = 2
    output_size = 1
    learning_rate = 0.05
    epochs = 1000
    convergence_threshold = 0.002

    # Initialize weights
    weights_input_hidden, weights_hidden_output = initialize_weights(input_size, hidden_size, output_size)

    # Train the neural network
    train(X, y, weights_input_hidden, weights_hidden_output, learning_rate, epochs, convergence_threshold)

    # Test the trained network
    test(X, weights_input_hidden, weights_hidden_output)

if __name__ == "__main__":
    main()
