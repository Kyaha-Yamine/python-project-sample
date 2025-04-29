import numpy as np
import matplotlib.pyplot as plt
import math
x = np.linspace(0,2 * math.pi,100)
y = []
for i in x:
    y.append(np.sin(i))
plt.plot(x, y)

plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()