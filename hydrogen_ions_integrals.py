import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# ion distance value
R = np.arange(0.001, 10, 0.2)


def S_func(R):
    def func(t, p, r, R):
        # defining r_a and r_b
        r_a = r
        r_b = np.sqrt(r_a**2 + R**2 - 2 * r_a * R * np.cos(t))
        # overlap integral S and spherical coordinates functions r^2 and
        # sin(theta)
        s_func = (1 / np.pi) * r**2 * np.exp(-r_a) * np.sin(t) * np.exp(-r_b)
        return s_func

    def bounds_t(p, r, R):
        # boundaries of theta from 0 to pi
        return [0, np.pi]

    def bounds_p(r, R):
        # boundaries of phi from 0 to 2pi
        return [0, 2 * np.pi]

    def bounds_r(R):
        # boundaries of r from 0 to infinity
        return [0, 100]
    # triple integration with the scipy module nquad
    return integrate.nquad(func, [bounds_t, bounds_p, bounds_r], args=(R,))[0]


# vectorizing overlap integral S
vec_S = np.vectorize(S_func)
S = vec_S(R)


def K_func(R):
    def func(t, p, r, R):
        r_a = r
        r_b = np.sqrt(r_a**2 + R**2 - 2 * r_a * R * np.cos(t))
        s_func = (-1 / r_a) * (1 / np.pi) * r**2 * \
            np.exp(-r_a) * np.sin(t) * np.exp(-r_b)
        return s_func

    def bounds_t(p, r, R):
        return [0, np.pi]

    def bounds_p(r, R):
        return [0, 2 * np.pi]

    def bounds_r(R):
        return [0, 100]

    return integrate.nquad(func, [bounds_t, bounds_p, bounds_r], args=(R,))[0]


vec_K = np.vectorize(K_func)
K = vec_K(R)


def J_func(R):
    def func(t, p, r, R):
        r_a = r
        r_b = np.sqrt(r_a**2 + R**2 - 2 * r_a * R * np.cos(t))
        s_func = (-1 / r_b) * (1 / np.pi) * r**2 * \
            np.exp(-r_a) * np.sin(t) * np.exp(-r_a)
        return s_func

    def bounds_t(p, r, R):
        return [0, np.pi]

    def bounds_p(r, R):
        return [0, 2 * np.pi]

    def bounds_r(R):
        return [0, 100]

    return integrate.nquad(func, [bounds_t, bounds_p, bounds_r], args=(R,))[0]


vec_J = np.vectorize(J_func)
J = vec_J(R)


# to check if the integrals are giving the right values one can refer to
# solved version taken from:
# http://www.pci.tu-bs.de/aggericke/PC4e/Kap_II/H2-Ion.htm

# S = np.exp(-R) * (1 + R + 1 / 3 * R**2)
# K = np.exp(-R) * (1 / R - 2 * R / 3)
# J = np.exp(-2 * R) * (1 + 1 / R)

# coulomb potential
V = np.exp(2) / (4 * np.pi * R)

# cases
func_1 = J / (1 + S) + V  # K = 0
func_2 = V  # K = J = 0
func_3 = J / (1 + S)  # K = V = 0
func_4 = K / (1 + S)  # J = V = 0
func_5 = (K + J) / (1 + S)  # V = 0

fig, axs = plt.subplots(1, 2, figsize=(10, 3))

# plotting
axs[0].plot(R, S, label='S')
axs[0].plot(R, K, label='K')
axs[0].plot(R, J, label='J')
axs[0].set_xlabel('R')
axs[0].set_ylabel('<eV>')
axs[0].set_ylim((-0.3, 1.1))
axs[0].set_xlim((0, 10))
axs[0].legend()

# plotting cases
axs[1].plot(R, func_1, label='$J/(1+S_{ab})+V(R)$')
axs[1].plot(R, func_2, label='$V(R)$')
axs[1].plot(R, func_3, label='$J/(1+S_{ab})$')
axs[1].plot(R, func_4, label='$K/(1+S_{ab})$')
axs[1].plot(R, func_5, label='$<E_+>$')
axs[1].set_xlabel('R')
axs[1].set_ylabel('<eV>')
axs[1].set_ylim((-0.3, 1.1))
axs[1].set_xlim((0, 6))
axs[1].legend()

plt.tight_layout()
plt.savefig("graph.svg")
plt.show()
