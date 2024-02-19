import json
import cv2
from src.helpers import read_gray
from os import walk
import numpy as np


__BASE_PATH = "./assets/BFL/"


def __load_images():
    paths = []
    for (dirpath, dirnames, filenames) in walk(__BASE_PATH):
        paths.extend(filenames)
        break

    list = []
    for path in paths:
        list.append(Image(path))

    return list


class Image(object):
    __BASE_PATH = "./assets/BFL/"

    writer: str
    version: str
    path: str

    def __init__(self, path):
        self.path = path
        (self.writer, self.version) = tuple(
            path.replace('.', '_').split('_')[0:2])

        self.__gray = np.empty(0)
        self.__descriptors = np.empty(0)
        self.__keypoints = ()

    def __compute_sift(self):
        sift = cv2.SIFT_create()
        self.__keypoints, self.__descriptors = sift.detectAndCompute(
            self.gray, None)

    @property
    def gray(self):  # -> MatLike | list:
        if not self.__gray.any():
            self.__gray = read_gray(self.__BASE_PATH+self.path)
        return self.__gray

    @property
    def descriptors(self):
        if not self.__descriptors.any():
            self.__compute_sift()
        return self.__descriptors

    @property
    def keypoints(self):
        if not self.__keypoints:
            self.__compute_sift()
        return self.__keypoints

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


images = __load_images()
