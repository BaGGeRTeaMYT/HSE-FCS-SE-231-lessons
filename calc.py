import numpy as np
p = [275, 150, 50, 25]
e = np.e
p_0 = [1/e, 1/e, 1/(2*e), 1 - 5/(2*e)]
n = 500
for i in range(len(p)):
  p[i] /= n
chi = 0
for i in range(len(p)):
  print(p[i], p_0[i])
  chi += 500/p_0[i] * (p[i] - p_0[i])**2
  print(chi)
