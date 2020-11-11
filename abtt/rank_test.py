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

n, frac = 4*400e3, 0.5
print(mean(n, frac))    # 320000000000.0
print(std(n, frac))     # 292118788.6231673
print(mde(n, frac))     # 726346024.1983426
print(mde_auc(n, frac)) # 0.0011349156628099103
