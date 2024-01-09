import torch

#Description too long
torch.manual_seed(7)

tensor = torch.rand(size = (1,1,1,10))
print(tensor)
print(tensor.size())

tensornew = tensor.squeeze()
print(tensor)
print(tensornew.size())

