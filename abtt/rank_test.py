import numpy as np
from scipy.stats import norm

alpha = 0.05
beta = 0.8
z_alpha = norm.ppf(1-alpha)
z_beta = norm.ppf(beta)

def mean(n, frac):
  n1 = n*frac
  n2 = n*(1-frac)
  return n1 * n2/2

def std(n, frac):
  n1 = n*frac
  n2 = n*(1-frac)
  return np.sqrt(n1*n2 * (n1+n2+1)/12)

def mde(n, frac):
  return (z_alpha + z_beta) * std(n, frac)

def mde_auc(n, frac):
  n1 = n*frac
  n2 = n*(1-frac)
  return mde(n, frac) / n1 / n2

n, frac = 0.1 * 10.8e6, 0.5
print(mean(n, frac))    # 145800000000.0
print(std(n, frac))     # 162000074.99998263
print(mde(n, frac))     # 402809113.8905219
print(mde_auc(n, frac)) # 0.0013813755620388267
