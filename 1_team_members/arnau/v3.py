import matplotlib.pyplot as plt 
import numpy as np
from sklearn import datasets
from sklearn.neural_network import MLPClassifier

# Load the digits dataset from scikit learn
digits = datasets.load_digits()

# Preprocess the data: Scale pixel values to a range between 0 and 1
x = digits.images / 16.0
x = x.reshape((len(digits.images), -1))

# Split the data into training and testing sets
x_train = x[:1000]
y_train = digits.target[:1000]
x_test = x[1000:]
y_test = digits.target[1000:]

# Initialize a multi-layer perceptron classifier with 2 hidden layers of 50 neurons each
mlp = MLPClassifier(hidden_layer_sizes=(50, 50), activation='relu', alpha=0.0001,
                    solver='adam', tol=1e-4, random_state=1,
                    learning_rate_init=0.01, verbose=True)

# Fit the model to the training data
mlp.fit(x_train, y_train)

# Make a prediction on a test image
image_index = 18
prediction = mlp.predict(x_test[image_index].reshape(1,-1))
print("Prediction:", prediction[0])
plt.imshow(digits.images[image_index], cmap='binary')
plt.show()