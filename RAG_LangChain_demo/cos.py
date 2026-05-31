"""
  计算向量间的cos值相似度
"""
import numpy as np
def get_d_dot(vec_a,vec_b):
  """计算两个向量的点乘"""
  if len(vec_a)!=len(vec_b):
    raise ValueError("2个向量的维度必须相等")
  sum = 0
  for x,y in zip(vec_a,vec_b):
    sum += x*y
  return sum

def get_norm(vcm):
  """
    计算单个向量的向量模
  """
  norm_sum = 0
  for v in vcm:
    norm_sum += v*v
  return np.sqrt(norm_sum) 

def cosine_similarity(vec_a,vec_b):
  """计算余弦相似度"""
  return get_d_dot(vec_a, vec_b) / (get_norm(vec_a) * get_norm(vec_b))

print(cosine_similarity([0.5], [0.5]))
print(cosine_similarity([-0.5], [0.5]))