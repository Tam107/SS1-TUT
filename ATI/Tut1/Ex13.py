import numpy as np

def relu(input):
    '''Define your relu activation function here'''
    # Calculate the value for the output of the relu function: output
    output = max(0, input)

    # Return the value just calculated
    return(output)

# Assign input data
input_data = np.array([3, 5])

# Assign weights
weights = {'node_0': np.array([2, 4]),
           'node_1': np.array([4, -5]),
           'output': np.array([2, 7])}

# Calculate node value: node_0_value
node_0_input = (input_data * weights['node_0']).sum()
node_0_output = np.tanh(node_0_input)

# Calculate node value: node_1_value
node_1_input = (input_data * weights['node_1']).sum()
node_1_output = np.tanh(node_1_input)

# Put node values into array: hidden_layer_outputs
hidden_layer_outputs = np.array([node_0_output, node_1_output])

# Calculate output: output
input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
output = input_to_final_layer

# Print output
print(output)
