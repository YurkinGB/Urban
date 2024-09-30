import numpy as np
import requests
import matplotlib.pyplot as plt

#numpy
a = np.array([[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [3, 4, 5, 6]])

b = np.array([[2, 3, 5, 6],
            [3, 2, 7, 9],
            [2, 6, 6, 7],
            [2, 5, 4, 5]])

print(f'{a + b}\n')
print(f'{a - b}\n')
print(f'{a * b}\n')
print(a.sum())

#requests
response = requests.get('https://google.com')
print(response.text)

#matplotlib
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()

