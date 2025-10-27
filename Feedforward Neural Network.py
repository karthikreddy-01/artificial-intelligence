import numpy as np

# ----- Activation Function (Sigmoid) -----
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of Sigmoid (used for learning, not needed here but shown for clarity)
def sigmoid_derivative(x):
    return x * (1 - x)

# ----- Define Input and Output for XOR -----
# Input dataset (XOR inputs)
inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected output (XOR outputs)
expected_output = np.array([[0], [1], [1], [0]])

# ----- Network Parameters -----
np.random.seed(42)
inputLayerNeurons = 2     # two inputs
hiddenLayerNeurons = 2    # two neurons in hidden layer
outputLayerNeurons = 1    # one output

# Random weights and biases
weights_input_hidden = np.random.uniform(size=(inputLayerNeurons, hiddenLayerNeurons))
bias_hidden = np.random.uniform(size=(1, hiddenLayerNeurons))
weights_hidden_output = np.random.uniform(size=(hiddenLayerNeurons, outputLayerNeurons))
bias_output = np.random.uniform(size=(1, outputLayerNeurons))

# ----- Forward Propagation -----
hidden_input = np.dot(inputs, weights_input_hidden) + bias_hidden
hidden_output = sigmoid(hidden_input)

final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
final_output = sigmoid(final_input)

# ----- Print Results -----
print("Input:\n", inputs)
print("\nHidden Layer Output:\n", hidden_output)
print("\nFinal Output (Predicted XOR):\n", final_output)

