# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sTZoq7hy0BTwsBnZTej4d9XDflVc204O
"""

from PIL import Image

def ReLU(Z):
  if Z < 0:
    return 0
  else:
    return Z

import numpy as np
import random as r

weights = np.random.randint(0, 5, (1, 900))
biasess = np.random.randint(0, 10, (1, 5))
weights2 = np.random.randint(0, 5, (1, 5))
biasess2 = np.random.randint(0, 10, (1, 2))
labeling = ["CompressedCats", "DowngradedDogs"]

def cost_function(pred_list, true_list):
	val = []
	for i in range(len(true_list)):
		val.append(true_list[i] - pred_list[i])
	return sum(val) ** 2, val

for re in range(100):
  while True:
    ran = r.randint(0, 20)
    c = r.choice(labeling)
    if c == "CompressedCats":
      true_list = [10000000, 0]
    elif c == "DowngradedDogs":
      true_list = [0, 10000000]

    try:
      im = Image.open(c + '/result' + str(ran) + '.jpg')
      pix_val = list(im.getdata())
      rgb_values = np.array(pix_val)
      pixie_dust = []
      for x in rgb_values: pixie_dust.append(sum(x))
      pixels = np.array(pixie_dust)
      break
    except:
      pass
  for rf in range(3):
    hidden_layer = []
    for x in range(5):
      a = []
      for y in range(len(pixels)):
        a.append(pixels[y] * weights[0, y])
      hidden_layer.append(ReLU(sum(a) + biasess[0, x]))
    output = []
    for x in range(2):
      a = []
      for y in range(len(hidden_layer)):
        a.append(hidden_layer[y] * weights2[0, y])
      output.append(ReLU(sum(a) + biasess2[0, x]))
    per, arr = cost_function(output, true_list)
    for i in range(len(arr)):
      if arr[i] > 0.0:
       weights[0, i] += 1
       weights2[0, i] += 1
       biasess[0, i] += 1
       biasess2[0, i] += 1
      if arr[i] < 0.0:
       weights[0, i] -= 1
       weights2[0, i] -= 1
       biasess[0, i] -= 1
       biasess2[0, i] -= 1

true_list = [10000000, 0]
im = Image.open(c + '/result' + str(ran) + '.jpg')
pix_val = list(im.getdata())
rgb_values = np.array(pix_val)
pixie_dust = []
for x in rgb_values: pixie_dust.append(sum(x))
pixels = np.array(pixie_dust)

hidden_layer = []
for x in range(5):
  a = []
  for y in range(len(pixels)):
      a.append(pixels[y] * weights[0, y])
  hidden_layer.append(ReLU(sum(a) + biasess[0, x]))
output = []
for x in range(2):
  a = []
  for y in range(len(hidden_layer)):
      a.append(hidden_layer[y] * weights2[0, y])
  output.append(ReLU(sum(a) + biasess2[0, x]))
per, arr = cost_function(output, true_list)

print(true_list)
print(output)
high = max(output)
if high == output[0]:
  print("Cat")
elif high == output[1]:
  print("Dog")
im.show()
