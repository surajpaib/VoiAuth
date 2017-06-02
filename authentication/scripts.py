from python_speech_features import mfcc
import scipy.io.wavfile as wav
from sklearn import svm
import numpy as np
from cPickle import dump, load


class ModuleML(object):
    def __init__(self):
        self.model = None
        self.train_x = None
        self.train_y = None
        self.predict_data = None
        self.feature_vec = None



    def get_mfcc_feature_vectors(self, filepath):
        (rate, signal) = wav.read(filepath)
        feature_vectors_mfcc1 = mfcc(signal, rate, winlen=0.040)
        self.feature_vec = feature_vectors_mfcc1
        return feature_vectors_mfcc1

    def train_model(self, filepath):
        train_x = load(open('authentication/pickled_data/train_x', "r"))
        train_y = load(open('authentication/pickled_data/train_y', "r"))
        class_values = load(open('authentication/pickled_data/class', "r"))
        self.vectors = self.get_mfcc_feature_vectors(filepath)
        vectors = self.feature_vec
        train_x = np.append(train_x, vectors, axis=0)
        filter_size = np.shape(vectors)[0]
        class_values.append(class_values[-1] + 1)
        y = np.full(filter_size, int(class_values[-1]))
        train_y = np.append(train_y, y, axis=0)
        self.train_x = train_x
        self.train_y = train_y
        dump(train_x, open('authentication/pickled_data/train_x', "w"))
        dump(train_y, open('authentication/pickled_data/train_y', "w"))
        dump(class_values, open('authentication/pickled_data/class', "w"))
        return train_x, train_y, int(class_values[-1])

    def svm_run(self):
        model = svm.SVC()
        model.fit(self.train_x, self.train_y)
        self.model = model
        dump(model, open('authentication/pickled_data/model', "w"))


    def predict(self, filepath):
        model = load(open('authentication/pickled_data/model', "r"))
        test_vectors = self.get_mfcc_feature_vectors(filepath)
        val = model.predict(test_vectors)
        (values, counts) = np.unique(val, return_counts=True)
        label = values[np.argmax(counts)]
        total = 0
        for c in counts:
            total += c
        return val, total, label, counts, values



