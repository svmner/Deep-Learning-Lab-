import torch

#Finding indexes of maximum and minimum values

tensor1 = torch.rand(size = (2,3))
tensor2 = torch.rand(size = (2,3))

print("Tensor 1:", tensor1)
print("Tensor 1 device:", tensor1.device)

print("Tensor 2:", tensor2)
print("Tensor 2 device:", tensor2.device)

tensor1 = tensor1.to("cuda:0")
tensor2 = tensor2.to("cuda:0")
print(tensor1)
print(tensor2)

print("Tensor 1  device:", tensor1.device)
print("Tensor 2  device:", tensor2.device)

tensor2 = torch.transpose(tensor2,0,1)

tensor3 = torch.matmul(tensor1,tensor2)
print(tensor3)

print(torch.argmax(tensor3))
print(torch.argmin(tensor3))