import random
import numpy

def split_into_training_and_testing_sets(array):
  if len(array)<2:
    raise ValueError("Argument data_array must have at least 2 rows, it actually has just {}".format(len(array)))
  training_group= random.sample(range(len(array)), int(0.75*len(array)))
  training=[]
  test=[]
  for i in range(len(array)):
    if i in training_group:
      training.append(array[i])
    else:
      test.append(array[i])
  return [numpy.array(training), numpy.array(test)]

# print(split_into_training_and_testing_sets([[1,2,3,4]]))