import numpy as np
import sklearn.svm as svm
import sklearn.cluster as cluster

from src.logger import log, file_log, log_inline
from src.image import images as db_images
from time import time
from math import floor

WRITERS = sorted(list(set([image.writer for image in db_images])))[:100]
TRAIN_IMAGES = [
    image for image in db_images if image.writer in WRITERS and image.version != '03']
TEST_IMAGES = [
    image for image in db_images if image.writer in WRITERS and image.version == '03']
VOCAB_SIZE = 16
OFFSET = 0


class Keys:
    TOTAL_TIME = "total"
    SIFT_TIME = "sift"
    CODEBOOK_TIME = "codebook"
    SVM_TIME = "svm"
    TEST_TIME = "test"
    ACCURACY = "accuracy"
    VOCAB_SIZE = "vocab_size"
    NUM_OF_WRITERS = "writers"
    OFFSET = "offset"


def main():
    for writers in [5, 10, 315]:
        for vocab_size in [2, 3, 4, 5, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300]:
            for i, offset in enumerate([i for i in range(315) if i % writers == 0]):
                log(f"Vocab Size: {vocab_size}, Writers: {writers} ({i+1}/{floor(315/writers)})")
                log('')

                SET_VOCAB_SIZE(vocab_size)
                SET_WRITERS(writers, offset)
                result = run()
                file_log(result, f"w{writers}_v{vocab_size}.txt")


def run() -> dict:
    timer = {}
    timer[Keys.TOTAL_TIME] = time()

    writers = [image.writer for image in TRAIN_IMAGES]

    log_inline("Setting SIFT features")
    timer[Keys.SIFT_TIME] = time()
    descriptors = set_sift_features(TRAIN_IMAGES)
    timer[Keys.SIFT_TIME] = time() - timer[Keys.SIFT_TIME]
    log(f" - {timer[Keys.SIFT_TIME]:.2f}s")

    log_inline("Calculating codebook")
    timer[Keys.CODEBOOK_TIME] = time()
    histograms, kmeans = calc_codebook(descriptors)
    timer[Keys.CODEBOOK_TIME] = time() - timer[Keys.CODEBOOK_TIME]
    log(f" - {timer[Keys.CODEBOOK_TIME]:.2f}s")

    log_inline("Training SVM")
    timer[Keys.SVM_TIME] = time()
    classifier = train_svm(histograms, writers)
    timer[Keys.SVM_TIME] = time() - timer[Keys.SVM_TIME]
    log(f" - {timer[Keys.SVM_TIME]:.2f}s")

    log_inline("Testing SVM")
    timer[Keys.TEST_TIME] = time()
    success = get_success_rate(kmeans, classifier)
    timer[Keys.TEST_TIME] = time() - timer[Keys.TEST_TIME]
    log(f" - {timer[Keys.TEST_TIME]:.2f}s")

    timer[Keys.TOTAL_TIME] = time() - timer[Keys.TOTAL_TIME]
    log(f"Total time: {timer[Keys.TOTAL_TIME]:.2f}s")

    print(f"Accuracy: {success/len(TEST_IMAGES)*100}% - Time: {timer}")

    log_values = {
        Keys.NUM_OF_WRITERS: len(WRITERS),
        Keys.OFFSET: OFFSET,
        Keys.VOCAB_SIZE: VOCAB_SIZE,
        Keys.ACCURACY: success/len(TEST_IMAGES)
    }

    result = {**log_values, **timer}
    log(result)

    log('')
    log("---------------------------------")
    log('')

    return result


def SET_VOCAB_SIZE(value):
    global VOCAB_SIZE
    VOCAB_SIZE = value


def SET_WRITERS(value, offset=0):
    global WRITERS
    WRITERS = sorted(list(set([image.writer for image in db_images])))[
        offset:offset+value]
    global TRAIN_IMAGES
    TRAIN_IMAGES = [
        image for image in db_images if image.writer in WRITERS and image.version != '03']
    global TEST_IMAGES
    TEST_IMAGES = [
        image for image in db_images if image.writer in WRITERS and image.version == '03']
    global OFFSET
    OFFSET = offset


def set_sift_features(images):
    descriptors = []
    for i, image in enumerate(images):
        # log(f"{i+1}/{len(images)}")
        descriptors.append(image.descriptors)

    return descriptors


def calc_codebook(descriptors):
    kmeans = cluster.KMeans(n_clusters=VOCAB_SIZE, n_init=10)
    # log("Fit kmeans")
    _ = kmeans.fit(np.concatenate(descriptors))

    # log("Predicting kmeans per image")
    histograms = []
    for descriptor in descriptors:
        prediction = kmeans.predict(descriptor)
        hist, _ = np.histogram(prediction, bins=VOCAB_SIZE)
        histograms.append(hist)

    return histograms, kmeans


def train_svm(x_values, y_values):
    clf = svm.SVC(kernel='linear')
    clf.fit(x_values, y_values)
    return clf


def classify(image, classifier, kmeans):
    kmeans_vocab = kmeans.predict(image.descriptors)
    histogram, _ = np.histogram(kmeans_vocab, bins=VOCAB_SIZE)
    return classifier.predict([histogram])[0]


def get_success_rate(kmeans, classifier):
    success = 0
    for image in TEST_IMAGES:
        prediction = classify(image, classifier, kmeans)
        # log(f"Predicted: {prediction} - Actual: {image.writer}")
        if prediction == image.writer:
            success += 1
    return success


if __name__ == '__main__':
    main()
