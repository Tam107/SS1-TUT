import numpy as np
import matplotlib.pyplot as plt

# Define get_slope() function
def get_slope(input_data, target, weights):
  # Calculate the predictions: preds
  preds = (input_data * weights).sum()

  # Calculate the error: error
  error = preds - target

  # Calculate the slope: slope
  slope = input_data * error * 2

  return(slope)

# Define get_mse() function
def get_mse(input_data, target, weights):
  # Calculate the predictions: preds
  preds = (input_data * weights).sum()

  # Calculate the mean squared error
  mse = (preds - target) ** 2

  return(mse)

# The data points you will make a prediction for
input_data = np.array([1, 2, 3])
# The target values, used to calculate the error
target = 0
# A sample set of weights
weights = np.array([0, 2, 1])

# Set the learning rate: learning_rate
learning_rate = 0.01

# Set the number of weights updated to 20
n_updates = 20

# MSE history values
mse_hist = []

# Iterate over the number of updates
for i in range(n_updates):
    # Calculate the slope: slope
    slope = get_slope(input_data, target, weights)

    # Update the weights: weights
    weights = weights - ( learning_rate * slope)

    # Calculate mse with new weights: mse
    mse = get_mse(input_data, target, weights)

    # Append the mse to mse_hist
    mse_hist.append(mse)

# Plot the mse history
plt.plot(mse_hist)
plt.xlabel('Iterations')
plt.ylabel('Mean Squared Error')
plt.show()