import h5py
with h5py.File('./accelerometer_data.h5', 'r') as hdf:

    activity_names = list(hdf.keys())
    print(activity_names)