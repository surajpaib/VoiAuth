# Run file to clean slate the model

from scripts import ModuleML
from cPickle import dump
import numpy as np
model = ModuleML()


class_1 = model.get_mfcc_feature_vectors('authentication/samples/kunaltrain1.wav')
class_1 = class_1[0:3000][:]
class_2 = model.get_mfcc_feature_vectors('authentication/samples/kanthitrain1.wav')
class_2 = class_2[0:3000][:]
train_x = np.append(class_1, class_2, axis=0)
train_y = np.append(np.full(np.shape(class_1)[0], 1), np.full(np.shape(class_2)[0], 2), axis=0)
class_values = [2]
dump(train_x, open('authentication/pickled_data/train_x', "w"))
dump(train_y, open('authentication/pickled_data/train_y', "w"))
dump(class_values, open('authentication/pickled_data/class', "w"))
