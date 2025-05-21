import torch
import torch.nn as nn
from typing import T
from mypy.typeops import false_only

class SelfAttentionV1(nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()
        self.W_query = nn.Parameter(torch.randn(d_in, d_out))
        self.W_key = nn.Parameter(torch.randn(d_in, d_out))
        self.W_value = nn.Parameter(torch.randn(d_in, d_out))

    def forward(self, x):
        keys = x @ self.W_key
        queries = x @ self.W_query
        values = x @ self.W_value
        attn_scores = queries @ keys.transpose(-2, -1)

        attn_weights = torch.softmax(
            attn_scores/keys.shape[-1] ** 0.5, dim = -1
        )
        context_vec = attn_weights @ values

        return context_vec


# Essentially the same as them, instead using Linear for optimization issues

class selfAttentionV2(nn.Module):
    def __init__(self, d_in, d_out, qkv_bias=False):
        super().__init__()
        self.W_query = nn.Linear(d_in, d_out, bias = qkv_bias)
        self.W_key = nn.Linear(d_in, d_out, bias = qkv_bias)
        self.W_value = nn.Linear(d_in, d_out, bias = qkv_bias)

    def forward(self, x):
        keys = x @ self.W_key
        queries = x @ self.W_query
        values = x @ self.W_value

        attn_scores = queries @ keys.transpose(-2, -1)

        attn_weights = torch.softmax(
            attn_scores/keys.shape[-1] ** 0.5, dim = -1
        )
        context_vec = attn_weights @ values

        return context_vec
