import torch

#Matrix Multiplication

tensor1 = torch.rand(size = (7,7))
tensor2 = torch.rand(size = (1,7))

tensor2 = torch.transpose(tensor2,0,1)

tensor3 = torch.matmul(tensor1,tensor2)
print(tensor3)