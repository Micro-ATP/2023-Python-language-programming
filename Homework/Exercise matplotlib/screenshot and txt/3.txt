from mayavi import mlab
import numpy as np
fig = mlab.figure()
x, y, z = np.mgrid[-10:10:50j, -10:10:50j, -10:10:50j]
s = np.sqrt(x**2+y**2+z**2)
mlab.contour3d(s,contours=[5],transparent=True)
mlab.show()