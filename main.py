# imports for array-handling and plotting
import numpy as np
import matplotlib
matplotlib.use( 'tkagg' )
import matplotlib.pyplot as plt

# let's keep our keras backend tensorflow quiet
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
# for testing on CPU
os.environ['CUDA_VISIBLE_DEVICES'] = ''
# keras imports for the dataset and building our neural network
from keras.datasets import mnist
from keras.models import Sequential, load_model
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


def train_model(epochs=20, filename="keras_mnist.h5"):
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    fig = plt.figure()

    for i in range(16):
      plt.subplot(4,4,i+1)
      plt.tight_layout()
      plt.imshow(X_train[i], cmap='gray', interpolation='none')
      plt.title("Digit: {}".format(y_train[i]))
      plt.xticks([])
      plt.yticks([])

    fig.savefig("image.png")


    plt.subplot(2,1,1)
    plt.imshow(X_train[0], cmap='gray', interpolation='none')
    plt.title("Digit: {}".format(y_train[0]))
    plt.xticks([])
    plt.yticks([])
    plt.subplot(2,1,2)
    plt.hist(X_train[0].reshape(784))
    plt.title("Pixel Value Distribution")

    # let's print the shape before we reshape and normalize
    print("X_train shape", X_train.shape)
    print("y_train shape", y_train.shape)
    print("X_test shape", X_test.shape)
    print("y_test shape", y_test.shape)

    # building the input vector from the 28x28 pixels
    X_train = X_train.reshape(60000, 784)
    X_test = X_test.reshape(10000, 784)
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')

    # normalizing the data to help with the training
    X_train /= 255
    X_test /= 255

    # print the final input shape ready for training
    print("Train matrix shape", X_train.shape)
    print("Test matrix shape", X_test.shape)

    print(np.unique(y_train, return_counts=True))

    # one-hot encoding using keras' numpy-related utilities
    n_classes = 10
    print("Shape before one-hot encoding: ", y_train.shape)
    Y_train = np_utils.to_categorical(y_train, n_classes)
    Y_test = np_utils.to_categorical(y_test, n_classes)
    print("Shape after one-hot encoding: ", Y_train.shape)

    # building a linear stack of layers with the sequential model
    model = Sequential()
    model.add(Dense(512, input_shape=(784,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))

    model.add(Dense(10))
    model.add(Activation('softmax'))

    # compiling the sequential model
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

    # training the model and saving metrics in history
    history = model.fit(X_train, Y_train,
              batch_size=128, epochs=epochs,
              verbose=2,
              validation_data=(X_test, Y_test))

    # saving the model
    save_dir = "save/"
    model_name = filename
    model_path = os.path.join(save_dir, model_name)
    model.save(model_path)
    print('Saved trained model at %s ' % model_path)



    # evalutating model performance
    mnist_model = load_model(filepath=model_path)
    loss_and_metrics = mnist_model.evaluate(X_test, Y_test, verbose=2)

    print("Test Loss", loss_and_metrics[0])
    print("Test Accuracy", loss_and_metrics[1])

    # load the model and create predictions on the test set
    mnist_model = load_model(filepath=model_path)
    predicted_classes = mnist_model.predict_classes(X_test)

    # see which we predicted correctly and which not
    correct_indices = np.nonzero(predicted_classes == y_test)[0]
    incorrect_indices = np.nonzero(predicted_classes != y_test)[0]
    print()
    print(len(correct_indices)," classified correctly")
    print(len(incorrect_indices)," classified incorrectly")

    # adapt figure size to accomodate 18 subplots
    plt.rcParams['figure.figsize'] = (7,14)

    figure_evaluation = plt.figure()

    # plot 9 correct predictions
    for i, correct in enumerate(correct_indices[:9]):
        plt.subplot(3,3,i+1)
        plt.imshow(X_test[correct].reshape(28,28), cmap='gray', interpolation='none')
        plt.title(
          "Predicted: {}, Truth: {}".format(predicted_classes[correct],
                                            y_test[correct]))
        plt.xticks([])
        plt.yticks([])

    plt.show()
    fig.savefig("evaluation.png")


# trying trained model on input file
def load_image(filename):
	img = load_img(filename, grayscale=True, target_size=(28, 28))
	img = img_to_array(img)
	img = img.reshape((1, 784))
	img = img.astype('float32')
	img = img / 255.0
	return img

def predict_input_image(filename):
    model = load_model('save/keras_mnist.h5')
    img = load_image(filename)
    digit = model.predict_classes(img, 0)
    print("Predicted number: ", digit[0])



#train_model(epochs=10, filename="keras_mnist.h5")
predict_input_image("input_image.png")
