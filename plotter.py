import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def plot_residuals(predicted_array, true_array):
    diff_arr = []
    predicted_labels = np.argmax(predicted_array, axis=1)
    true_labels = np.argmax(true_array, axis=1)
    for i in range(0, len(predicted_labels)):
        diff_arr.append(abs(true_labels[i] - predicted_labels[i]))
    plt.hist(diff_arr, bins=max(diff_arr) -
             min(diff_arr)+1, align='left', rwidth=0.8)

    # Set labels and title
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram of Values')

    # Show the plot
    plt.show()
