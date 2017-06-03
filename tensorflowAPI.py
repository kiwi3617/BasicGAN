import os

from app import TransferAPI


class TensorflowAPI(TransferAPI):
    def transfer(self, image):
        pass


class Model:
    def __init__(self):
        pass

    def train(self):
        pass


class Preprocessor:

    def preprocess(self):
        pass

    def image_resize(filepath, height, width):
        # filepath = "../Downloads/apple/"
        for filename in os.listdir(filepath):
            if filename.endswith(".jpeg"):
                print(filename)
                image = scipy.misc.imread(filepath + "/" + filename)
                resized_image_image = scipy.misc.imresize(image, [height, width])
                scipy.misc.imsave(filepath + "/" + filename + "_resized.jpeg", resized_image)
        return 0