from tensorflow import keras
from keras.layers import Input, Lambda, Dense, Flatten
from keras.models import Model
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from keras.models import load_model
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

class IAML:
    def __init__(self):
        pass

    def ask(img_path,model_h5):
        model=load_model(f'{model_h5}')
        img=tf.keras.utils.load_img(img_path,target_size=(224,224))
        x = tf.keras.utils.img_to_array(img)
        x=np.expand_dims(x, axis=0)
        img_data=preprocess_input(x)
        classes=model.predict(img_data)
        # print(classes)
        result=int(classes[0][0])
        # print(result)
        if result==0:
            print("pne")
            return "BAD"
        else:
            print("Normal")
            return "GOOD"


    # def ask(img_path):
    #     model=load_model('chest_xray.h5')
    #     img=tf.keras.utils.load_img(img_path,target_size=(224,224))
    #     x = tf.keras.utils.img_to_array(img)
    #     x=np.expand_dims(x, axis=0)
    #     img_data=preprocess_input(x)
    #     classes=model.predict(img_data)
    #     # print(classes)
    #     result=int(classes[0][0])
    #     # print(result)
    #     if result==0:
    #         print("pne")
    #         return "Result is Pneumonia"
    #     else:
    #         print("Normal")
    #         return "Result is Normal"