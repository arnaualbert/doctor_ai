import matplotlib.pyplot as plt 
import numpy as np
from sklearn import datasets
from sklearn.neural_network import MLPClassifier

digits = datasets.load_digits()

x = np.arange(0, 3, 0.2)
y = x**2

plt.plot(x, y)

x = digits.images.reshape((len(digits.images), -1))
x_train = x[:1000]
y_train = digits.target[:1000]
x_test = x[1000:]
y_test = digits.target[1000:]

mlp = MLPClassifier(hidden_layer_sizes=(15,), activation='logistic', alpha=1e-4,
                    solver='sgd', tol=1e-4, random_state=1,
                    learning_rate_init=.1, verbose=True)

mlp.fit(x_train,y_train)

image_index = 5
prediction = mlp.predict(x_test[image_index].reshape(1,-1))
print("Prediction:", prediction[0])
plt.imshow(digits.images[image_index], cmap='binary')
plt.show()