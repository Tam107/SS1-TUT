import numpy as np

# Assign input data
# Dữ liệu đầu vào: # Accounts = 3, # Children = 5
input_data = np.array([3, 5])

# Assign weights
# Trọng số được lấy từ các đường nối trên sơ đồ
weights = {'node_0': np.array([2, 4]),
           'node_1': np.array([4, -5]),
           'output': np.array([2, 7])}

# Calculate node value: node_0_value
# Giá trị của node_0 = (3 * 2) + (5 * 4) = 26
node_0_value = (input_data * weights['node_0']).sum()

# Calculate node value: node_1_value
# Giá trị của node_1 = (3 * 4) + (5 * -5) = -13
node_1_value = (input_data * weights['node_1']).sum()

# Put node values into array: hidden_layer_outputs
# Tập hợp các giá trị đầu ra của tầng ẩn
hidden_layer_outputs = np.array([node_0_value, node_1_value])

# Calculate output: output
# Giá trị đầu ra cuối cùng = (26 * 2) + (-13 * 7) = -39
output = (hidden_layer_outputs * weights['output']).sum()

# Print output
print(output)