import matplotlib.pyplot as plt 
import numpy as np
from sklearn import datasets
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

digits = datasets.load_digits()

# create a numpy 1-D array with 16 evenly spaced values, from 0 to 3.
x = np.linspace(0, 3, 16)
print(x)
# create a new numpy array. 
# x**2 means that each element of x is squared.
y = x**2
print(y)
# plot y versus x, you should get a parabola. 
# check that for x = 1 we have y = 1, and that for x = 2, y = 4. 
plt.plot(x, y)

dir(digits)
print(type(digits.images))
print(type(digits.target))

print(digits.images.shape)

print(digits.target.shape)
print(digits.target)

def plot_multi(i):
    '''Plots 16 digits, starting with digit i'''
    nplots = 16
    fig = plt.figure(figsize=(15,15))
    for j in range(nplots):
        plt.subplot(4,4,j+1)
        plt.imshow(digits.images[i+j], cmap='binary')
        plt.title(digits.target[i+j])
        plt.axis('off')
    plt.show()

plot_multi(0)

y = digits.target
x = digits.images.reshape((len(digits.images), -1))
x.shape

x_train = x[:1000]
y_train = y[:1000]
x_test = x[1000:]
y_test = y[1000:]

mlp = MLPClassifier(hidden_layer_sizes=(15,), activation='logistic', alpha=1e-4,
                    solver='sgd', tol=1e-4, random_state=1,
                    learning_rate_init=.1, verbose=True)

mlp.fit(x_train,y_train)

# Predict digit for a given image
image_index = 5
prediction = mlp.predict(x_test[image_index].reshape(1,-1))
print("Prediction:", prediction[0])
plt.imshow(digits.images[image_index], cmap='binary')
plt.show()