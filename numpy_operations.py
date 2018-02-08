import numpy as np

t0 = np.array(['x0', 'y0', 'z0'])
t1 = np.array(['x1', 'y1', 'z1'])
t2 = np.array(['x2', 'y2', 'z2'])

total_result = t0
total_result = np.vstack((total_result, t1))
total_result = np.vstack((total_result, t2))

with open('output.txt', 'w') as outfile:
    for slice_2d in total_result:
        outfile.write(" ".join(map(str, slice_2d)))
        outfile.write("\n")

"""
output.txt looks like this
x0 y0 z0
x1 y1 z1
x2 y2 z2
"""
