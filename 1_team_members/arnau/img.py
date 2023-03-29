# %%
import matplotlib.pyplot as plt 
import numpy as np

# %%
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

# %%
from sklearn import datasets
digits = datasets.load_digits()

# %%
dir(digits)

# %%
print(type(digits.images))
print(type(digits.target))

# %%
digits.images.shape


# %%
print(digits.images[0])

# %%
import matplotlib.pyplot as plt
plt.imshow(digits.images[0],cmap='binary')
plt.show()

# %%
print(digits.target.shape)
print(digits.target)

# %%

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

# %%
plot_multi(0)


# %%
y = digits.target
x = digits.images.reshape((len(digits.images), -1))
x.shape

# %%
x[0]

# %%
x_train = x[:1000]
y_train = y[:1000]
x_test = x[1000:]
y_test = y[1000:]

# %%
from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(15,), activation='logistic', alpha=1e-4,
                    solver='sgd', tol=1e-4, random_state=1,
                    learning_rate_init=.1, verbose=True)

# %%
mlp.fit(x_train,y_train)

# %%
predictions = mlp.predict(x_test)
predictions[:50] 
# we just look at the 1st 50 examples in the test sample

# %%
y_test[:50] 
# true labels for the 1st 50 examples in the test sample

# %%
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)

# %%
plt.imshow(digits.images[15], cmap='binary')



