# 论文所输入数据集合NPZ在src/data_preprocess中，由于是图神经，有两个数据集合
# 输出手动放在log中

运行main_scomGNN_simple.py可以根据原论文所提到的图网络分割技术运行代码文件，注意这里的数据为data_preprocess文件夹，包含，所需的图网络数据，以及train test val数据集
Epoch:198 Loss:0.08989260
    Epoch:198 Val HR@5:0.5010, HR@10:0.7505 NDCG:0.4387
    Epoch:199 Loss:0.09010618
    Epoch:199 Val HR@5:0.5089, HR@10:0.7624 NDCG:0.4429
    Loading 180th epoch
    Testing AUC!
    Testing HR@5:0.4772, HR@10:0.7406, NDCG:0.4346
    --------------------final results--------------------
    Test HR@5: mean0.4818, std0.0179, max0.5089, min0.4436
    Test NDCG: mean0.4341, std0.0096, max0.4486, min0.4224

运行main_scomGNN.py为根据论文中的思想仿造rechorus思路，这里有几个额外文件，如src/models/model_utils.py  src/helpers/SCOMGNNRunner.py  src/models/sequential/ScomGNN_rechorus.py 模型名为  ScomGNN_rechorus
因为这里源数据只有data/Grocery_and_Gourmet_Food，故需要下载dgl，是一个基于Python的深度学习框架，专为图神经网络（GNN）的研发设计。故我们不需要额外进行其他数据处理步骤。
