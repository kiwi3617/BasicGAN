import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import tensorflow as tf

_FILENAME1 = "BTC_EUR_2week(1)fixed.csv"
#_FILENAME2 = "minute_CryptoCompare_Index_BTC_EUR_289_51512368368118.csv"

data = np.loadtxt(fname=_FILENAME1,dtype=np.float32,delimiter=",")

#close(p1) open(p2) volumefrom(p3)	p1-p2(p4) , p3*p4(p5) , phase(p6)
#0 - stelth , 1 - Aware , 2 - mania , 3-blow off

x = data[0:1,0:-1]    # from 1st to (n-1)th column, when data has n columns
y = data[0:1,[-1]]    # nth column, class

# print variable type
print(type(x))
# print variable shape
print("x is", x.shape, "and y is", y.shape)
print("x is", x, "and y is", y)

