import numpy as np

from ATI.Tut1.example import hidden_layer_outputs


def relu(input):
    output = max(0, input)
    return output


def predict_with_network(input_data_row, weights):
    # calculate node 0 value
    node_0_input = (input_data_row * weights['node_0']).sum()
    node_0_output = relu(node_0_input)

    # calculate node 1 value
    node_1_input = (input_data_row * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    hidden_layer_outputs = np.array([node_0_output, node_1_output])
    input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
    output = relu(input_to_final_layer)

    return output


input_data = [np.array([3, 5]), np.array([1, -1]),
              np.array([0, 0]), np.array([8, 4])]

# Assign weights
weights = {'node_0': np.array([2, 4]),
           'node_1': np.array([4, -5]),
           'output': np.array([2, 7])}

results = []
for input_data_row in input_data:
    # Append prediction to results
    results.append(predict_with_network(input_data_row, weights))

# Print results
print(results)
