import itertools
import numpy as np
from scipy import linalg
from scipy.linalg import hadamard

# Construct truth table for the Boolean function
a = []
truth_table = []
lista = [
    np.reshape(np.array(i), (1, 6))
    for i in itertools.product([0, 1], repeat=1 * 6)
]
for m in lista:
    a.append(m.tolist())
for m in a:
    truth_table = truth_table + m


# Given an input, compute the value of the Boolean function
def bool(m):
    zet1 = m[0] ^ m[4] ^ m[5] ^ (m[0] * m[3]) ^ (m[1] * m[2]) ^ (
        m[1] * m[4]) ^ (m[3] * m[4]) ^ (m[4] * m[5]) ^ (m[0] * m[2] * m[3]) ^ (
            m[0] * m[2] * m[5]) ^ (m[0] * m[3] * m[4]) ^ (m[1] * m[2] * m[5])
    zet2 = zet1 ^ (m[1] * m[3] * m[5]) ^ (m[2] * m[4] * m[5]) ^ (
        m[0] * m[1] * m[2] * m[3]) ^ (m[0] * m[1] * m[2] * m[4]) ^ (
            m[0] * m[1] * m[4] * m[5]) ^ (m[1] * m[2] * m[3] * m[5])
    res = zet2 ^ (m[0] * m[1] * m[2] * m[3] * m[4]) ^ (
        m[0] * m[2] * m[3] * m[4] * m[5])
    return (res)


# Results of boolean function of truth table
c = []
for m in truth_table:
    res = bool(m)
    c.append(res)

# Create Hadamard Matrix
had = hadamard(64)

d = np.asarray(c)
ad = np.asarray(had)
walsh = d.dot(ad)

# Print to the screen the values of Walsh Spectrum with their frequencies
print('The Walsh Spectrum is:')
values = set(walsh)
values = list(values)
values = sorted(values)
frequencies = []
walsh = walsh.tolist()
for val in values:
    frequencies.append(walsh.count(val))
for val, freq in zip(values, frequencies):
    print(val, freq)

# Compute Autocorrelation

autocorrelation = []
for m in truth_table:
    sum1 = 0
    for ma in truth_table:
        first = bool(ma)
        second = []
        for i in range(len(ma)):
            second.append(ma[i] ^ m[i])
        third = bool(second)
        sum1 += (-1)**(first + third)
    autocorrelation.append(sum1)

# Print to the screen the values of Autocorrelation Spectrum with their frequencies
print('The Autocorrelation Spectrum is:')
values = set(autocorrelation)
values = list(values)
values = sorted(values)
frequencies = []
for val in values:
    frequencies.append(autocorrelation.count(val))
for val, freq in zip(values, frequencies):
    print(val, freq)