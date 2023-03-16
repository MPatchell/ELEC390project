import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

member_walking_data = pd.read_csv('walking_combined_data.csv')
member_jumping_data = pd.read_csv('jumping_combined_data.csv')

'''
test_data = pd.read_csv('test_combined_data.csv')
fig, ax = plt.subplots(figsize=(10, 10))
axTest = np.arange(0, len(test_data)/100, 0.01)
ax.plot(axTest, test_data.iloc[:, 1], label='x')
ax.plot(axTest, test_data.iloc[:, 2], label='y')
ax.plot(axTest, test_data.iloc[:, 3], label='z')
ax.set_title('Test Data')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Acceleration (m/s^2)')
ax.legend()
plt.show()
'''
# Plot acceleration vs. time for walking and jumping data
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Walking data
axZero = np.arange(0, len(member_walking_data)/100, 0.01)
axs[0].plot(axZero, member_walking_data.iloc[:, 1], label='x')
axs[0].plot(axZero, member_walking_data.iloc[:, 2], label='y')
axs[0].plot(axZero, member_walking_data.iloc[:, 3], label='z')
axs[0].set_title('Walking Data')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Acceleration (m/s^2)')
axs[0].legend()

# Jumping data
axOne = np.arange(0, len(member_walking_data)/100, 0.01)
axs[1].plot(axOne, member_jumping_data.iloc[:, 1], label='x')
axs[1].plot(axOne, member_jumping_data.iloc[:, 2], label='y')
axs[1].plot(axOne, member_jumping_data.iloc[:, 3], label='z')
axs[1].set_title('Jumping Data')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Acceleration (m/s^2)')
axs[1].legend()

plt.show()
