import h5py
import numpy as np
from scipy.stats import skew

# Open the HDF5 file
with h5py.File('./accelerometer_data.h5', 'r') as hdf:
    # Get the dataset containing the time windows and labels
    windows_and_labels = hdf['dataset/train/walking'][:]

    # Split the dataset into windows and labels
    windows = windows_and_labels[:, :, :-1]
    labels = windows_and_labels[:, :, -1]
    print(labels)

    # Create an empty array to hold the feature vectors
    num_labels = np.unique(labels).size
    features = np.zeros((num_labels, 10))

    # Iterate over each label and extract the features
    for i, label in enumerate(np.unique(labels)):
        # Find the windows corresponding to the current label
        windows_for_label = windows[labels == label]

        # Flatten the windows into a single array for easier computation
        flattened_windows = windows_for_label.reshape((-1, windows.shape[-1]))

        # Compute the features for the flattened windows
        max_val = np.max(flattened_windows, axis=1)
        min_val = np.min(flattened_windows, axis=1)
        range_val = np.ptp(flattened_windows, axis=1)
        mean_val = np.mean(flattened_windows, axis=1)
        median_val = np.median(flattened_windows, axis=1)
        var_val = np.var(flattened_windows, axis=1)
        skew_val = skew(flattened_windows, axis=1)
        rms_val = np.sqrt(np.mean(flattened_windows ** 2, axis=1))
        kurt_val = np.mean((flattened_windows - np.mean(flattened_windows, axis=1, keepdims=True)) ** 4, axis=1) / (np.var(flattened_windows, axis=1, keepdims=True) ** 2)
        std_val = np.std(flattened_windows, axis=1)

        # Compute the mean and variance of the features for the current label
        feature_means = np.mean([max_val, min_val, range_val, mean_val, median_val, var_val, skew_val, rms_val, kurt_val, std_val], axis=1)
        feature_variances = np.var([max_val, min_val, range_val, mean_val, median_val, var_val, skew_val, rms_val, kurt_val, std_val], axis=1)

        # Store the mean and variance of the features for the current label in the features array
        features[i] = np.concatenate((feature_means, feature_variances))

# Save the features to a CSV file
np.savetxt('features.csv', features, delimiter=',')
