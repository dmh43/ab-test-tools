import numpy as np
from scipy.stats import norm

alpha = 0.05
beta = 0.8
z_alpha = norm.ppf(1-alpha)
z_beta = norm.ppf(beta)

def mean(n, frac):
  return n*frac*n*(1-frac)/2

def std(n, frac):
  n1 = n*frac
  n2 = n*(1-frac)
  return np.sqrt(n1*n2*(n1+n2+1)/12)

def mde(n, frac):
  return (z_alpha + z_beta) * std(n, frac)

def mde_auc(n, frac):
  n1 = n*frac
  n2 = n*(1-frac)
  return mde(n, frac) / n1 / n2

n, frac = 600000, 0.1
print(mean(n, frac)) # 16200000000.0
print(std(n, frac)) # 40249257.1360019
print(mde(n, frac)) # 100078766.02345048
print(mde_auc(n, frac)) # 0.003088850803192916
