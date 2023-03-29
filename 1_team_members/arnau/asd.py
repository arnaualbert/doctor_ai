import matplotlib.pyplot as plt 
import numpy as np
from sklearn import datasets
from sklearn.neural_network import MLPClassifier

digits = datasets.load_digits()

# Preprocess the data: Scale pixel values to a range between 0 and 1
x = digits.images / 16.0
x = x.reshape((len(digits.images), -1))

# Split the data into training and testing sets
x_train = x[:1000]
y_train = digits.target[:1000]
x_test = x[1000:]
y_test = digits.target[1000:]

# Find all instances of the number 5 in the training set
fives_train = x_train[np.where(y_train == 5)]

# Initialize a multi-layer perceptron classifier with 2 hidden layers of 50 neurons each
mlp = MLPClassifier(hidden_layer_sizes=(50, 50), activation='relu', alpha=0.0001,
                    solver='adam', tol=1e-4, random_state=1,
                    learning_rate_init=0.01, verbose=True)
# Fit the model to the 5 training data
mlp.fit(fives_train, np.ones(len(fives_train)))

# Find all instances of the number 5 in the test set
fives_test = x_test[np.where(y_test == 5)]

# Use the model to predict whether each instance of the 5 is actually a 5
predictions = mlp.predict(fives_test)

# Count the number of correct predictions
num_correct = np.sum(predictions == 1)

print("Number of correct predictions for the digit 5:", num_correct)
# num_images = 10
num_images = num_correct
fig, axes = plt.subplots(1, num_images, figsize=(6, 6))
fives_indices = np.where(y_train == 5)[0]
for i in range(num_images):
    axes[i].imshow(x_train[fives_indices[i]].reshape(8, 8), cmap=plt.cm.gray_r, interpolation='nearest')
    axes[i].axis('off')
    axes[i].set_title('Label: {}'.format(y_train[fives_indices[i]]))
plt.show()