import numpy as np
import matplotlib.pyplot as plt

# Activation functions
def step_activation(x):
    return np.where(x >= 0, 1, -1)

def sigmoid(x):
    clipped_x = np.clip(x, -500, 500)  # Clip values to prevent overflow
    return 1 / (1 + np.exp(-clipped_x))


def relu(x):
    return np.maximum(0, x)

# Perceptron function
def perceptron(inputs, weights):
    weighted_sum = np.dot(inputs, weights[1:]) + weights[0]
    return step_activation(weighted_sum)

# Training function
def train_perceptron(training_inputs, training_outputs, weights, learning_rate, activation_function, max_epochs=1000):
    errors = []
    epochs = 0
    while True:
        total_error = 0
        for inputs, target in zip(training_inputs, training_outputs):
            prediction = activation_function(np.dot(inputs, weights[1:]) + weights[0])
            error = target - prediction
            total_error += np.sum(error ** 2)
            weights[1:] += learning_rate * np.dot(error, inputs)
            weights[0] += learning_rate * error.item() if np.isscalar(error) else error[0]  # Ensure error is a scalar
        errors.append(total_error)
        epochs += 1
        if total_error == 0 or epochs >= max_epochs:
            break
    return errors, epochs


# Plotting function
def plot_error(errors, epochs, activation_function_name):
    plt.plot(range(1, epochs + 1), errors)
    plt.xlabel('Epochs')
    plt.ylabel('Error')
    plt.title(f'Epochs vs Error ({activation_function_name} Activation)')
    plt.show()

def main():
    # AND gate truth table inputs and outputs
    training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    training_outputs = np.array([[-1, -1], [-1, 1], [-1, -1], [1, -1]])

    # Initial weights
    initial_weights = np.array([10, 0.2, -0.75])

    # Learning rate
    learning_rate = 0.05

    # Activation functions and their names
    activation_functions = [step_activation, sigmoid, relu]
    activation_function_names = ['Bi-Polar Step', 'Sigmoid', 'ReLU']

    for activation_function, activation_function_name in zip(activation_functions, activation_function_names):
        # Train the perceptron
        updated_weights = np.copy(initial_weights)
        errors, num_epochs = train_perceptron(training_inputs, training_outputs, updated_weights, learning_rate, activation_function)

        # Plot the errors
        plot_error(errors, num_epochs, activation_function_name)

        print(f"{activation_function_name} Activation - Converged in {num_epochs} epochs\nFinal Weights: {updated_weights}\n")

if __name__ == "__main__":
    main()
