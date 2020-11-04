from numpy import array as ary; from numpy import log as ln
from numpy import cos, sin, pi, sqrt, exp, arccos;
tau = 2*pi
import numpy as np;
from matplotlib import pyplot as plt

def transform(pt):
    """
    Define your own self-map here.
    The self-map must take a point (x_in, y_in) and produce another point (x_out, y_out).
    The distance between any two input points must decrease after the transformation in order for the contraction mapping theorem to work.
    The default self-map used here has attractive fixed point: -0.5, 0
    """
    x, y = pt.T[0], pt.T[1]
    x0, y0 = -0.5, 0.0
    trans_pt = ary([-(0.6*(x-x0)+x0), 0.6*(y-y0)+y0]).T
    return trans_pt

if __name__=='__main__':
    x_ticks, y_ticks = np.linspace(-1,1), np.linspace(-1,1)
    x_pts, y_pts = [l.flatten() for l in np.meshgrid(x_ticks, y_ticks)]
    meshgrid = ary([x_pts, y_pts]).T
    plt.scatter(*meshgrid.T, marker='x')
    meshgrid = transform(meshgrid)
    plt.scatter(*meshgrid.T)
    meshgrid = transform(meshgrid)
    plt.scatter(*meshgrid.T)
    plt.show()