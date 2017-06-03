
# coding: utf-8

import scipy
from scipy import misc
import os



# dataset ../dataset/apple/train
# valid   ../dataset/apple/valid

def image_resize(filepath,height,width):
    #filepath = "../Downloads/apple/"
    for filename in os.listdir(filepath):
        if filename.endswith(".jpeg"): 
            print(filename)
            image = scipy.misc.imread(filepath+"/"+filename)
            resized_image_image = scipy.misc.imresize(image,[height,width])
            scipy.misc.imsave(filepath+"/"+filename+"_resized.jpeg",resized_image)
    return 0

# filepath = "../Directory_name"
# example
# image_resize("../Downloads/apple",25,25)
