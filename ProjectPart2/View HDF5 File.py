import h5py

# Open the HDF5 file in read-only mode
with h5py.File('accelerometer_data.h5', 'r') as f:
    # List all the top-level groups
    print("Top-level groups:")
    for group_name in f.keys():
        print(group_name)

    # List all the datasets in the 'dataset' group
    print("\nDatasets in the 'dataset' group:")
    dataset_group = f['./dataset/train']
    for dataset_name in dataset_group.keys():
        print(dataset_name)

    # Print the shape and contents of a specific dataset
    print("\nContents of the 'data' dataset for MP's walking activity:")
    data_dataset = f['./dataset/test/data']
    print(data_dataset.shape)
    print(data_dataset[:])