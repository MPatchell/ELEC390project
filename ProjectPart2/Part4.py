# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['agg.path.chunksize'] = 200
mpl.rcParams['path.simplify_threshold'] = 0.2

dataRange = 11500

# Member 1: MP

# Adjust Data to 100 Hz with a factor
M1DataCheck = pd.read_csv('MPWalkingBackPocket.csv')
M1SamplingFactor = round(len(M1DataCheck)/(100*M1DataCheck.iloc[-1, 0]))

# Walking Data
member1_walking_data = pd.concat([
    pd.read_csv('MPWalkingBackPocket.csv', nrows=M1SamplingFactor*dataRange), pd.read_csv('MPWalkingFrontPocket.csv', nrows=M1SamplingFactor*dataRange),
    pd.read_csv('MPWalkingJacketPocket.csv', nrows=dataRange), pd.read_csv('MPWalkingHand.csv', nrows=dataRange)
], ignore_index=True)

# Jumping Data
member1_jumping_data = pd.concat([
    pd.read_csv('MPJumpingBackPocket.csv', nrows=M1SamplingFactor*dataRange), pd.read_csv('MPJumpingFrontPocket.csv', nrows=M1SamplingFactor*dataRange),
    pd.read_csv('MPJumpingJacketPocket.csv', nrows=M1SamplingFactor*dataRange), pd.read_csv('MPJumpingHand.csv', nrows=M1SamplingFactor*dataRange)
], ignore_index=True)

if M1SamplingFactor > 1:
    member1_jumping_data = member1_jumping_data.drop(member1_jumping_data.index[1::M1SamplingFactor])
    member1_walking_data = member1_walking_data.drop(member1_walking_data.index[1::M1SamplingFactor])

# Member 2: AM
M2DataCheck = pd.read_csv('AMWalkingBackPocket.csv')
M2SamplingFactor = round(len(M2DataCheck)/(100*M2DataCheck.iloc[-1, 0]))

member2_walking_data = pd.concat([
    pd.read_csv('AMWalkingBackPocket.csv', nrows=M2SamplingFactor*dataRange), pd.read_csv('AMWalkingFrontPocket.csv', nrows=M2SamplingFactor*dataRange),
    pd.read_csv('AMWalkingJacketPocket.csv', nrows=M2SamplingFactor*dataRange), pd.read_csv('AMWalkingHand.csv', nrows=M2SamplingFactor*dataRange)
], ignore_index=True)

member2_jumping_data = pd.concat([
    pd.read_csv('AMJumpingBackPocket.csv', nrows=M2SamplingFactor*dataRange), pd.read_csv('AMJumpingFrontPocket.csv', nrows=M2SamplingFactor*dataRange),
    pd.read_csv('AMJumpingJacketPocket.csv', nrows=M2SamplingFactor*dataRange), pd.read_csv('AMJumpingHand.csv', nrows=M2SamplingFactor*dataRange)
], ignore_index=True)

if M2SamplingFactor > 1:
    member2_jumping_data = member2_jumping_data.drop(member2_jumping_data.index[1::M2SamplingFactor])
    member2_walking_data = member2_walking_data.drop(member2_walking_data.index[1::M2SamplingFactor])

# Member 3: XZ
M3DataCheck = pd.read_csv('XZWalkingBackPocket.csv')
M3SamplingFactor = round(len(M3DataCheck)/(100*M3DataCheck.iloc[-1, 0]))

member3_walking_data = pd.concat([
    pd.read_csv('XZWalkingBackPocket.csv', nrows=M3SamplingFactor*dataRange), pd.read_csv('XZWalkingFrontPocket.csv', nrows=M3SamplingFactor*dataRange),
    pd.read_csv('XZWalkingJacketPocket.csv', nrows=M3SamplingFactor*dataRange), pd.read_csv('XZWalkingHand.csv', nrows=M3SamplingFactor*dataRange)
], ignore_index=True)


member3_jumping_data = pd.concat([
    pd.read_csv('XZJumpingBackPocket.csv', nrows=2*dataRange), pd.read_csv('XZJumpingFrontPocket.csv', nrows=2*dataRange),
    pd.read_csv('XZJumpingJacketPocket.csv', nrows=2*dataRange), pd.read_csv('XZJumpingHand.csv', nrows=2*dataRange)
], ignore_index=True)

if M3SamplingFactor > 1:
    member3_jumping_data = member3_jumping_data.drop(member3_jumping_data.index[1::M3SamplingFactor])
    member3_walking_data = member3_walking_data.drop(member3_walking_data.index[1::M3SamplingFactor])

all_data = pd.concat([
    member1_walking_data, member1_jumping_data, member2_walking_data, member2_jumping_data, member3_walking_data,
    member3_jumping_data
], ignore_index=True)

all_data_array = all_data.to_numpy()
np.random.shuffle(all_data_array)
num_train = int(0.9 * len(all_data_array))
train_data = all_data_array[:num_train]
train_df = pd.DataFrame(train_data, columns=all_data.columns)

train_data = train_df.iloc[:, 0:-1]
labels = train_df.iloc[:, -1]

window_size = 500
train_New = train_data.rolling(window_size).mean()

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(20, 10))
for i in range(0, 4):
    ax.flatten()[i].scatter(train_data.iloc[:, 0], train_data.iloc[:, 1])
    ax.flatten()[i].set_title(train_data.columns[i] + ' vs ' + train_data.columns[0], fontsize=15)
fig.tight_layout()
plt.show()


'''

ax.plot(train_data.iloc[:, 0], train_data.iloc[:, 1])
ax.plot(train_New.iloc[:, 0], train_New.iloc[:, 1])

ax.set_xlabel('t')
ax.set_ylabel('x acceleration')
plt.show()
'''