import torch

#Indexing

tensor = torch.rand(20)

print(tensor)

print(tensor[0])
print(tensor[5])
print(tensor[0:3])
print(tensor[5:])
print(tensor[:4])

tensor1 = torch.tensor([[1, 2, 1], [3, 8, 4]])

print(tensor1[1])
print(tensor1[0][2])

tensor[0] = 8

print(tensor)

tensor1[0][2] = 9
print(tensor1)