import torch
import numpy

#Numpy to Tensor and Vice Versa

a = numpy.array([1,2,3,4])
t = torch.from_numpy(a)
print(t)

t1 = torch.tensor([1,2,3,4])
a1 = t1.numpy()
print(a1)