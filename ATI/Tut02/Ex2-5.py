import numpy as np

# The data points you will make a prediction for
input_data = np.array([1, 2, 3])
# The target values, used to calculate the error
target = 0
# A sample set of weights
weights = np.array([0, 2, 1])

# Calculate the predictions: preds
preds = (input_data * weights).sum()

# Calculate the error: error
error = preds - target

# Calculate the slope: slope
slope = 2 * error * input_data

# Print the slope
print(slope)