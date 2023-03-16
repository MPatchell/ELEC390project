import h5py
import numpy as np
from scipy.stats import skew

# Open the HDF5 file
with h5py.File('./accelerometer_data.h5', 'r') as hdf:
    # Get the dataset containing the time windows
    windows = hdf['dataset/train/walking'][:]
    print(windows.shape)

    # Create an empty array to hold the feature vectors
    features = np.zeros((windows.shape[0], 10))

    # Iterate over each time window and extract the features
    for i in range(windows.shape[0]):
        # Extract the data from the window
        window_data = windows[i]

        # Compute the features
        max_val = np.max(window_data)
        min_val = np.min(window_data)
        range_val = max_val - min_val
        mean_val = np.mean(window_data)
        median_val = np.median(window_data)
        var_val = np.var(window_data)
        skew_val = skew(window_data)
        rms_val = np.sqrt(np.mean(window_data ** 2))
        kurt_val = np.mean((window_data - np.mean(window_data)) ** 4) / (np.var(window_data) ** 2)
        std_val = np.std(window_data)

        # Store the features in the features array
        features[i] = (max_val, min_val, range_val, mean_val, median_val, var_val, skew_val, rms_val, kurt_val, std_val)

# Save the features to a CSV file
np.savetxt('features.csv', features, delimiter=',')
