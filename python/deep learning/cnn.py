import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from keras.layers import Dense
from keras.models import Sequential
model=Sequential()

print(model)
print("done")



