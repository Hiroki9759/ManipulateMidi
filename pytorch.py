import torch
print(torch.__version__)

#テンソルの作成
x = torch.Tensor(2,2)
list = [[1,2,3],[4,5,6]]
x2 = torch.Tensor(list)
print(x)
print(x2)
#テンソルのサイズ確認
print(x2.size())
#乱数（一様分布）
print(torch.rand(2,2))
#乱数（正規分布）
print(torch.randn(2,2))
#単位行列
print(torch.eye(3,3))
#空のテンソル
print(torch.empty(4,1))
#等間隔の数列
print(torch.linspace(0,100,steps=11))
# テンソルの作成
x = torch.Tensor([[2, 2], [1, 1]])
y = torch.Tensor([[3, 2], [1, 2]])
 
# 表示
print(x)
print(y)

# テンソルの足し算
print(x + y)
print(torch.add(x, y))

# テンソルのアダマール積（要素の乗法）
print(x * y)
print(torch.mul(x, y))

# テンソルの積（ドットプロダクト）
print(torch.mm(x, y))

# テンソルの要素の和
print(torch.sum(x))

# テンソルの要素の標準偏差
print(torch.std(x))

# テンソルの要素の算術平均
print(torch.mean(x))
