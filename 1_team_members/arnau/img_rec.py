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

IMAGE_SIZE = [224, 224]

train_path = 'archive/BoneFractureDataset/training'
valid_path = 'archive/BoneFractureDataset/testing'

vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

for layer in vgg.layers:
    layer.trainable = False

folders = glob('archive/BoneFractureDataset/training/*')
x = Flatten()(vgg.output)


prediction = Dense(len(folders), activation='softmax')(x)
# create a model object
model = Model(inputs=vgg.input, outputs=prediction)
# view the structure of the model
model.summary()

model.compile(
  loss='categorical_crossentropy',
  optimizer='adam',
  metrics=['accuracy']
)

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

# Make sure you provide the same target size as initialied for the image size
training_set = train_datagen.flow_from_directory('archive/BoneFractureDataset/training',
                                                 target_size = (224, 224),
                                                 batch_size = 10,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('archive/BoneFractureDataset/testing',
                                            target_size = (224, 224),
                                            batch_size = 10,
                                            class_mode = 'categorical')



r = model.fit(
  training_set,
  validation_data=test_set,
  epochs=20,#epochs=1,
  steps_per_epoch=len(training_set),
  validation_steps=len(test_set)
)



import tensorflow as tf
from keras.models import load_model

model.save('bones.h5') # chest_xray

from keras.models import load_model

from keras.preprocessing import image

from keras.applications.vgg16 import preprocess_input

import numpy as np

model=load_model('bones.h5')



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
