import tensorflow as tf
import pandas as pd
import numpy as np
from keras.utils import to_categorical
import os
import matplotlib.pyplot as plt
from plotter import plot_residuals

df_url = f'Data/time_series_data.csv'
df = pd.read_csv(df_url)


def split_dataset(dataset, test_ratio=.1):
    test_indices = np.random.rand(len(dataset)) < test_ratio
    return dataset[~test_indices], dataset[test_indices]


train_ds_pd, test_ds_pd = split_dataset(df)
print(len(train_ds_pd), len(test_ds_pd))
test_labels = test_ds_pd.reset_index()
train_names = train_ds_pd.pop('name')
test_names = test_ds_pd.pop('name').reset_index()
target_train = train_ds_pd.pop('total_points')
target_train = to_categorical(target_train, num_classes=40)
target_test = test_ds_pd.pop('total_points')
target_test = to_categorical(target_test, num_classes=40)

tf.convert_to_tensor(test_ds_pd)
tf.convert_to_tensor(train_ds_pd)
# Normalizes the data
normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(train_ds_pd)

# Sets up model for the neural network


def get_basic_model():
    model = tf.keras.Sequential([
        normalizer,
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(40)
    ])
# Compiles the model
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    return model


# Sets up the location for storing the weights
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
# Sets up callback for saving weights while training
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)
# Creates model
model = get_basic_model()
# Loads in the weights for the model
model.load_weights(checkpoint_path)
# Trains the model
model.fit(train_ds_pd, target_train, epochs=20, callbacks=[cp_callback])
print(model.layers[0].weights)
print(train_ds_pd.columns)
probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])
predictions = probability_model.predict(test_ds_pd)
team_list_url = f'Data/team_list.csv'
team_list = pd.read_csv(team_list_url)
team_dict = team_list.to_dict()
team_dict = team_dict['0']
i = 146
print(f'Player: {test_names["name"][i]}')
if test_labels['team_x'][i] == -1:
    print('Team: Unknown')
else:
    print(f'Team: {team_dict[test_labels["team_x"][i]]}')
print(f'Prediction: {np.argmax(predictions[i])-7}')
print(f'True Value: {np.argmax(target_test[i])-7}')
plot_residuals(predictions, target_test)
