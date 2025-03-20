import matplotlib.pyplot as plt

# data
X = [1, 2, 3, 4, 5, 6]
Y = [2, 4, 6, 8, 10, 12]

plt.plot(X, Y, marker="o")

plt.show()

""" 
When we run this script; the plot will be rendered in a different window instead of terminal
because stdout (terminal) can mainly handle textual data. 
"""
