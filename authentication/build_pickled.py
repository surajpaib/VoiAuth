from scripts import ModuleML
from cPickle import dump
import numpy as np
model = ModuleML()


class_1 = model.get_mfcc_feature_vectors('samples/surajaudio1.wav')
class_2 = model.get_mfcc_feature_vectors('samples/nayanaudio1.wav')
train_x = np.append(class_1, class_2, axis=0)
train_y = np.append(np.full(np.shape(class_1)[0], 1), np.full(np.shape(class_2)[0], 2), axis=0)
class_values = [2]
dump(train_x, open('pickled_data/train_x', "w"))
dump(train_y, open('pickled_data/train_y', "w"))
dump(class_values, open('pickled_data/class', "w"))
