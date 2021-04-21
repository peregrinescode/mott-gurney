import numpy as np
import matplotlib.pyplot as plt

from scipy.constants import epsilon_0

def MG(V, mu, epsilon_r, L):
    J = (9/8) * mu * epsilon_r * epsilon_0 * V**2 * L**(-3)
    return J

# Set constants
mu = 1e-9 #m2/Vs
epsilon_r = 3
L = 100e-9

x = np.linspace(0, 10)
y = MG(x, mu, epsilon_r, L)

fig, ax = plt.subplots()

ax.loglog(x, y)
fig.savefig('/home/ross/git/mott-gurney/output.png')