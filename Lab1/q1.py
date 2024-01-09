import torch

#Reshaping

tensorpre = torch.tensor([[2,2],[3,3]])
print(tensorpre)

tensorpost = torch.reshape(tensorpre,(-1,))
print(tensorpost)

#Viewing

tensorpre = torch.arange(16)
print(tensorpre)

tensorpre = tensorpre.view(4,4)
print(tensorpre)

#Stacking

tensor1 = torch.arange(16)
tensor2 = torch.rand(16)

tensorstacked = torch.stack((tensor1,tensor2))
print(tensorstacked)

#Squeezing

tensorzero = torch.zeros(2,1,1,1,2)
print(f'Tensor with Dimensions (2 x 1 x 1 x 1 x 2):\n{tensorzero}')

tensorzero = torch.squeeze(tensorzero)
print(f'Post squeeze: \n {tensorzero}')

#Unsqueeze

x = torch.tensor([1, 2, 3, 4])
torch.unsqueeze(x, 1)

print(x)

