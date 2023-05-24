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

# IMAGE_SIZE = [224, 224]

# train_path = 'archive/BoneFractureDataset/training'
# valid_path = 'archive/BoneFractureDataset/testing'

# vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

# for layer in vgg.layers:
#     layer.trainable = False

# folders = glob('archive/BoneFractureDataset/training/*')
# x = Flatten()(vgg.output)


# prediction = Dense(len(folders), activation='softmax')(x)
# # create a model object
# model = Model(inputs=vgg.input, outputs=prediction)
# # view the structure of the model
# model.summary()

# model.compile(
#   loss='categorical_crossentropy',
#   optimizer='adam',
#   metrics=['accuracy']
# )

# from keras.preprocessing.image import ImageDataGenerator

# train_datagen = ImageDataGenerator(rescale = 1./255,
#                                    shear_range = 0.2,
#                                    zoom_range = 0.2,
#                                    horizontal_flip = True)

# test_datagen = ImageDataGenerator(rescale = 1./255)

# # Make sure you provide the same target size as initialied for the image size
# training_set = train_datagen.flow_from_directory('archive/BoneFractureDataset/training',
#                                                  target_size = (224, 224),
#                                                  batch_size = 10,
#                                                  class_mode = 'categorical')

# test_set = test_datagen.flow_from_directory('archive/BoneFractureDataset/testing',
#                                             target_size = (224, 224),
#                                             batch_size = 10,
#                                             class_mode = 'categorical')



# r = model.fit(
#   training_set,
#   validation_data=test_set,
#   epochs=20,#epochs=1,
#   steps_per_epoch=len(training_set),
#   validation_steps=len(test_set)
# )



import tensorflow as tf
from keras.models import load_model

# model.save('bones.h5') # chest_xray

from keras.models import load_model

from keras.preprocessing import image

from keras.applications.vgg16 import preprocess_input

import numpy as np

model=load_model('bones.h5')

import os

list_tup = []
nomal = []
wrong = 0
for filename in os.walk('/home/arnaualbert/Desktop/pneumonia_dl/archive/BoneFractureDataset/testing/TUMOR/'):
    for f in filename[2]:
        route = '/home/arnaualbert/Desktop/pneumonia_dl/archive/BoneFractureDataset/testing/TUMOR/'+f
        img=tf.keras.utils.load_img(route,target_size=(224,224))

        x = tf.keras.utils.img_to_array(img)

        x=np.expand_dims(x, axis=0)

        img_data=preprocess_input(x)

        classes=model.predict(img_data)
        print(classes)

        result=int(classes[0][0])
        print(result)

        if result==0:
            wrong += 1
            # nomal.append(route)
                        # wrong += 1
        else:
            nomal.append(route)


print(nomal)
print(wrong)

# TUMOR 150 WRONG BRAIN_2.h5 
# tumor = ['/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_278.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_178.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_93.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_196.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_116.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_195.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_229.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_163.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_228.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_263.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_86.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_108.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_243.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_145.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_177.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_180.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_166.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_13.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_246.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_224.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_106.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_279.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_240.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_164.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_49.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_124.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_190.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_154.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_105.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_127.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_70.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_260.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_214.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_126.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_262.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_221.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_61.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_103.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_174.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_129.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_237.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_185.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_210.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_16.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_212.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_157.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_179.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_146.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_269.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_6.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_281.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_284.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_199.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_41.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_219.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_59.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_255.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_140.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_156.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_19.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_162.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_1.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_275.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_33.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_37.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_209.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_282.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_66.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_161.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_204.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_120.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_288.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_4.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_213.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_193.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_241.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_191.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_115.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_128.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_57.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_171.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_155.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_56.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_143.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_184.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_188.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_72.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_271.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_139.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_58.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_216.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_159.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_231.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_47.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_32.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_245.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_147.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_208.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_165.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_225.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_8.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_169.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_254.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_141.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_142.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_238.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_130.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_258.jpg']
# # NORMAL 24 WRONG BRAIN_2.h5
# normal = ['/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(68).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(81).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(12).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(33).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(60).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(29).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(22).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(57).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(82).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(16).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(11).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(14).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(102).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(17).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(64).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(62).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(67).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(78).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(94).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(51).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(26).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(5).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(86).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(85).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(70).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(80).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(44).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(45).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(3).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(88).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(99).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(24).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(32).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(20).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(28).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(39).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(91).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(65).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(38).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(21).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(40).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(23).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(71).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(103).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(2).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(104).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(31).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(47).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(6).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(84).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(72).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(36).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(13).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(74).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(15).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(53).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(34).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(95).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(98).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(19).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(59).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(55).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(93).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(9).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(90).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(4).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(96).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(77).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(18).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(56).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(49).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(76).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(66).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(61).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(63).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(73).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(25).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(10).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(97).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(69).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(101).jpg']


# NORMAL 15 WRONG BRAIN.H5
# normal = ['/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(68).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(75).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(81).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(12).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(52).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(33).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(60).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(37).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(79).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(29).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(22).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(57).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(82).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(16).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(11).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(14).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(100).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(102).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(17).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(64).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(42).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(41).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(62).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(67).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(78).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(51).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(26).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(5).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(86).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(85).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(70).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(80).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(44).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(45).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(3).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(88).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(99).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(24).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(32).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(20).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(28).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(39).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(35).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(91).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(65).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(38).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(21).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(40).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(23).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(71).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(103).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(2).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(104).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(48).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(8).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(31).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(47).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(27).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(6).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(84).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(72).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(36).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(13).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(74).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(15).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(53).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(34).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(95).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(98).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(19).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(59).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(55).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(93).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(9).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(4).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(96).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(43).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(18).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(56).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(49).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(76).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(66).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(61).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(63).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(73).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(25).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(10).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(97).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(69).jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/NORMAL/image(101).jpg']
# TUMOR 110 WRONG BRAIN.H5
# tumor = ['/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_278.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_178.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_93.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_244.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_9.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_150.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_195.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_22.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_163.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_228.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_263.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_86.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_108.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_152.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_110.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_243.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_270.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_177.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_180.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_17.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_173.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_246.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_222.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_224.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_106.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_215.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_192.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_240.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_203.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_40.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_164.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_2.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_49.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_170.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_137.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_131.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_124.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_194.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_190.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_154.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_105.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_52.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_127.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_70.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_18.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_260.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_214.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_126.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_262.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_221.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_272.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_15.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_174.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_129.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_237.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_185.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_210.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_167.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_247.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_212.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_157.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_265.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_146.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_7.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_189.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_242.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_6.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_281.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_284.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_199.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_266.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_41.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_219.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_255.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_44.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_140.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_156.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_19.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_0.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_162.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_187.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_71.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_1.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_257.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_267.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_275.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_33.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_37.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_21.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_209.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_148.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_282.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_181.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_161.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_64.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_20.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_35.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_204.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_288.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_4.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_213.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_193.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_241.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_65.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_10.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_123.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_115.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_128.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_43.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_57.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_119.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_171.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_155.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_285.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_136.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_42.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_143.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_45.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_184.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_139.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_232.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_58.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_216.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_159.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_231.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_182.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_47.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_32.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_245.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_144.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_160.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_147.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_208.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_165.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_225.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_31.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_8.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_122.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_67.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_169.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_135.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_34.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_175.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_141.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_142.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_238.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_130.jpg', '/home/arnaualbert/Desktop/pneumonia_dl/brain/Testing/TUMOR/image_258.jpg']



# for route in tumor:
        # img=tf.keras.utils.load_img(route,target_size=(224,224))

        # x = tf.keras.utils.img_to_array(img)

        # x=np.expand_dims(x, axis=0)

        # img_data=preprocess_input(x)

        # classes=model.predict(img_data)
        # print(classes)

        # result=int(classes[0][0])
        # print(result)

        # if result==0:
            # print("tumor")
        # else:
            # print("Result is normal")






# tumor = ['image_278.jpg', 'image_178.jpg', 'image_93.jpg', 'image_196.jpg', 'image_116.jpg', 'image_195.jpg', 'image_229.jpg', 'image_163.jpg', 'image_228.jpg', 'image_263.jpg', 'image_86.jpg', 'image_108.jpg', 'image_243.jpg', 'image_145.jpg', 'image_177.jpg', 'image_180.jpg', 'image_166.jpg', 'image_13.jpg', 'image_246.jpg', 'image_224.jpg', 'image_106.jpg', 'image_279.jpg', 'image_240.jpg', 'image_164.jpg', 'image_49.jpg', 'image_124.jpg', 'image_190.jpg', 'image_154.jpg', 'image_105.jpg', 'image_127.jpg', 'image_70.jpg', 'image_260.jpg', 'image_214.jpg', 'image_126.jpg', 'image_262.jpg', 'image_221.jpg', 'image_61.jpg', 'image_103.jpg', 'image_174.jpg', 'image_129.jpg', 'image_237.jpg', 'image_185.jpg', 'image_210.jpg', 'image_16.jpg', 'image_212.jpg', 'image_157.jpg', 'image_179.jpg', 'image_146.jpg', 'image_269.jpg', 'image_6.jpg', 'image_281.jpg', 'image_284.jpg', 'image_199.jpg', 'image_41.jpg', 'image_219.jpg', 'image_59.jpg', 'image_255.jpg', 'image_140.jpg', 'image_156.jpg', 'image_19.jpg', 'image_162.jpg', 'image_1.jpg', 'image_275.jpg', 'image_33.jpg', 'image_37.jpg', 'image_209.jpg', 'image_282.jpg', 'image_66.jpg', 'image_161.jpg', 'image_204.jpg', 'image_120.jpg', 'image_288.jpg', 'image_4.jpg', 'image_213.jpg', 'image_193.jpg', 'image_241.jpg', 'image_191.jpg', 'image_115.jpg', 'image_128.jpg', 'image_57.jpg', 'image_171.jpg', 'image_155.jpg', 'image_56.jpg', 'image_143.jpg', 'image_184.jpg', 'image_188.jpg', 'image_72.jpg', 'image_271.jpg', 'image_139.jpg', 'image_58.jpg', 'image_216.jpg', 'image_159.jpg', 'image_231.jpg', 'image_47.jpg', 'image_32.jpg', 'image_245.jpg', 'image_147.jpg', 'image_208.jpg', 'image_165.jpg', 'image_225.jpg', 'image_8.jpg', 'image_169.jpg', 'image_254.jpg', 'image_141.jpg', 'image_142.jpg', 'image_238.jpg', 'image_130.jpg', 'image_258.jpg']


    # for f in filename:
        # print(f)



# while True:
#     input_img = input("Enter the image path: ")
#     img=tf.keras.utils.load_img(input_img,target_size=(224,224))

#     x = tf.keras.utils.img_to_array(img)

#     x=np.expand_dims(x, axis=0)

#     img_data=preprocess_input(x)

#     classes=model.predict(img_data)
#     print(classes)

#     result=int(classes[0][0])
#     print(result)

#     if result==0:
#         print("Tumor")
#     else:
#         print("Result is Normal")






# img_path = "/home/arnaualbert/Desktop/pneumonia_dl/chest_xray_pneumonia/chest_xray/val/PNEUMONIA/person1952_bacteria_4883.jpeg"  # Replace with the path to your image
# img = image.load_img(img_path, target_size=(224, 224))
# img_array = image.img_to_array(img)
# img_array = np.expand_dims(img_array, axis=0)
# img_array /= 255.

# # Make a prediction
# predictions = model.predict(img_array)

# # Get the predicted class
# predicted_class = np.argmax(predictions[0])
# class_labels = ['NORMAL', 'PNEUMONIA']  # The class labels used during training
# predicted_label = class_labels[predicted_class]

# print('Prediction:', predicted_label)


# from keras.models import load_model

# model = load_model('lungs.h5')


# image_path = 'path_to_your_image.jpg'  # Replace with the path to your image
# img = image.load_img(image_path, target_size=(224, 224))
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)
# preds = model.predict(x)
# class_labels = training_set.class_indices
# predicted_class = np.argmax(preds)
# predicted_label = list(class_labels.keys())[list(class_labels.values()).index(predicted_class)]
# confidence = preds[0][predicted_class] * 100
