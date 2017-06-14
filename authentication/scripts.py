
from python_speech_features import mfcc
import scipy.io.wavfile as wav
from sklearn import svm
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
import numpy as np
from cPickle import dump, load
import boto3
import os




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
        with open('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/train_x', 'wb') as data:
            bucket.download_fileobj('train_x', data)
        train_x = load(open('authentication/pickled_data/train_x', "r"))
        with open('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/train_y', 'wb') as data:
            bucket.download_fileobj('train_y', data)

        print np.shape(train_x)
        train_y = load(open('authentication/pickled_data/train_y', "r"))
        print np.shape(train_y)
        with open('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/class', 'wb') as data:
            bucket.download_fileobj('class', data)
        class_values = load(open('authentication/pickled_data/class', "r"))
        print class_values
        self.vectors = self.get_mfcc_feature_vectors(filepath)
        vectors = self.feature_vec
        vectors = vectors[0:3000][:]
        train_x = np.append(train_x, vectors, axis=0)
        print np.shape(train_x)
        filter_size = np.shape(vectors)[0]
        class_values.append(class_values[-1] + 1)
        print class_values
        y = np.full(filter_size, int(class_values[-1]))
        train_y = np.append(train_y, y, axis=0)
        print np.shape(train_y)
        self.train_x = train_x
        self.train_y = train_y
        dump(train_x, open('authentication/pickled_data/train_x', "w"))
        dump(train_y, open('authentication/pickled_data/train_y', "w"))
        dump(class_values, open('authentication/pickled_data/class', "w"))
        dump(train_x, open('authentication/pickled_data/train_x', "w"))
        with open('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/train_x', "rb") as data2:
            bucket.upload_fileobj(data2, 'train_x')
        dump(train_y, open('authentication/pickled_data/train_y', "w"))
        with open('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/train_y', "rb") as data2:
            bucket.upload_fileobj(data2, 'train_y')
        dump(class_values, open('authentication/pickled_data/class', "w"))
        with open('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/class', "rb") as data2:
            bucket.upload_fileobj(data2, 'class')

        try:
            os.remove('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/train_x')
            os.remove('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/train_y')
            os.remove('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/class')
        except:
            print "Delete failed"
        return train_x, train_y, int(class_values[-1])

    def GBM_run(self):
        model = RandomForestClassifier(n_jobs=-1, n_estimators=500, verbose=1)
        model.fit(self.train_x, self.train_y)
        self.model = model
        dump(model, open('authentication/pickled_data/model', "w"))
        with open('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/model', "rb") as data2:
            bucket.upload_fileobj(data2, 'model')
        os.remove('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/model')

    def predict(self, filepath, actual):
        with open('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/model', 'wb') as data:
            bucket.download_fileobj('model', data)
        model = load(open('authentication/pickled_data/model', "r"))
        os.remove('/home/suraj/Repositories/VoiAuth/authentication/pickled_data/model')
        test_vectors = self.get_mfcc_feature_vectors(filepath)
        print np.shape(test_vectors)
        test_y = np.full(np.shape(test_vectors)[0], actual)
        val = model.predict(test_vectors)
        print val
        (values, counts) = np.unique(val, return_counts=True)
        label = values[np.argmax(counts)]
        confidence = model.score(test_vectors, test_y)
        print confidence
        print label
        return val, label, confidence



