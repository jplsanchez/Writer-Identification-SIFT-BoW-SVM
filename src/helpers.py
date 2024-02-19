import cv2
import pickle
import winsound
import numpy as np
from matplotlib import pyplot as plt


def display(img):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.xticks([]), plt.yticks([])
    plt.show()


def read_gray(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


def alert():
    dur = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, dur)
    winsound.Beep(int(freq / 2), dur)
    winsound.Beep(int(freq / 3), dur * 2)


def load_stored_data(var_name):
    with open(f'store/{var_name}.pkl', 'rb') as f:
        return pickle.load(f)


def average(key_name, list_of_dicts):
    values = [dict[key_name] for dict in list_of_dicts]
    return np.mean(values)


def error(key_name, list_of_dicts):
    values = [dict[key_name] for dict in list_of_dicts]
    return np.sqrt(np.var(values))
