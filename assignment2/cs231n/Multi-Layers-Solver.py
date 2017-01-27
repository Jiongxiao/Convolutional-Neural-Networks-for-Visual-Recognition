
# As usual, a bit of setup

import numpy as np
import matplotlib.pyplot as plt
from cs231n.classifiers.cnn import *
from cs231n.classifiers.convnet import *
from cs231n.data_utils import *
from cs231n.gradient_check import eval_numerical_gradient_array, eval_numerical_gradient
from cs231n.layers import *
from cs231n.fast_layers import *
from cs231n.solver import Solver


plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

# for auto-reloading external modules
# see http://stackoverflow.com/questions/1907993/autoreload-of-modules-in-ipython
%load_ext autoreload
%autoreload 2

def rel_error(x, y):
  """ returns relative error """
  return np.max(np.abs(x - y) / (np.maximum(1e-8, np.abs(x) + np.abs(y))))


data = get_added_CIFAR10_data()
for k, v in data.iteritems():
  print '%s: ' % k, v.shape

num_train = 100
small_data = {
  'X_train': data['X_train'][-num_train:],
  'y_train': data['y_train'][-num_train:],
  'X_val': data['X_val'],
  'y_val': data['y_val'],
}

model = ThreeLayerConvNet(weight_scale=1e-2)

solver = Solver(model, small_data,
                num_epochs=20, batch_size=50,
                update_rule='adam',
                optim_config={
                  'learning_rate': 1e-3,
                },
                verbose=True, print_every=1)
solver.train()




model = MultiLayerConvNet(weight_scale=0.0001,num_filters=32, hidden_dim=500, reg=0.05,use_affine_batchnorm=True,
                         num_conv_relu=3,num_con_relu_p=2,num_fc_relu=2)

solver = Solver(model, data,
                num_epochs=50, batch_size=100,
                update_rule='adam',
                optim_config={
                  'learning_rate': 1e-4,
                },
                verbose=True, print_every=20)
solver.train()