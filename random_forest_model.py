import tensorflow_decision_forests as tfdf


import numpy as np
import pandas as pd


data_url = f'Data/time_series_data.csv'
data = pd.read_csv(data_url)


def split_dataset(dataset, test_ratio=.1):
    test_indices = np.random.rand(len(dataset)) < test_ratio
    return dataset[~test_indices], dataset[test_indices]


train_ds_pd, test_ds_pd = split_dataset(data)
print(len(train_ds_pd), len(test_ds_pd))

train_ds = tfdf.keras.pd_dataframe_to_tf_dataset(
    train_ds_pd, label='total_points')
test_ds = tfdf.keras.pd_dataframe_to_tf_dataset(
    test_ds_pd, label='total_points')

model_1 = tfdf.keras.RandomForestModel(verbose=2)
model_1.fit(train_ds)
model_1.compile(metrics=["accuracy"])
evaluation = model_1.evaluate(test_ds)
print()
print(evaluation)
