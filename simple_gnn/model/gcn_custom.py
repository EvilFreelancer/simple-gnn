import torch
import torch.nn as nn


class GraphConvolution(nn.Module):
    def __init__(self, input_dim, output_dim, support, act_func=None, featureless=False, dropout_rate=0., bias=False):
        super(GraphConvolution, self).__init__()
        self.embedding = None
        self.support = support
        self.featureless = featureless
        # self.linear = nn.Linear(input_dim,output_dim)
        for i in range(len(self.support)):
            setattr(self, 'W{}'.format(i), nn.Parameter(torch.randn(input_dim, output_dim)))

        if bias:
            self.b = nn.Parameter(torch.zeros(1, output_dim))

        self.act_func = act_func
        self.dropout = nn.Dropout(dropout_rate)

    def forward(self, x):
        x = self.dropout(x)
        out = 0

        for i in range(len(self.support)):
            if self.featureless:
                pre_sup = getattr(self, 'W{}'.format(i))
            else:
                pre_sup = x.mm(getattr(self, 'W{}'.format(i)))

            if i == 0:
                out = self.support[i].mm(pre_sup)
            else:
                out += self.support[i].mm(pre_sup)

        if self.act_func is not None:
            out = self.act_func(out)

        self.embedding = out
        return out


class GCNCustom(nn.Module):
    def __init__(self, input_dim, hidden_dim, support, dropout_rate=0., num_classes=10):
        super(GCNCustom, self).__init__()

        # GraphConvolution
        self.layer1 = GraphConvolution(
            input_dim, hidden_dim, support, act_func=nn.ReLU(),
            featureless=True, dropout_rate=dropout_rate
        )
        self.layer2 = GraphConvolution(
            hidden_dim, num_classes, support, dropout_rate=dropout_rate
        )

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        return out