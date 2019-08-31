#!/home/ocean/anaconda3/bin/python3
from numpy import cos, arccos, sin, arctan, tan, pi, sqrt; from numpy import array as ary; import numpy as np; tau = 2*pi
from matplotlib import pyplot as plt
from autograd import grad

# EPSILON=1E-12
OMEGA=1.1
INITIAL_X = 1.0

f = lambda x : 8/x -1
df_dx = grad(f)

def get_line(x0):
    #x0 is a scalar
    '''
    Return the list of y_coordinates of the line
    which starts from f(x0), follow the gradient f'(x0),
    and reaches 0.
    '''
    assert ary([x0]).shape==(1,), "Can only input a single scalar into the get_line program"
    start_x = ary(x0)
    start_y = f(x0)
    
    slope = df_dx(x0)
    first_order = lambda x : start_y+slope*(x-start_x)

    dy = OMEGA*start_y
    
    end_x = x0+(-dy)/slope
    x = np.linspace(start_x,end_x)
    return x,first_order(x)

if __name__=="__main__":
    
    x0=INITIAL_X
    for i in range(9):
        x,y=get_line(x0)
        plt.plot(x,y, color="C"+str(i), label = "iteration "+str(i+1))
        x0 = x[-1]
        plt.plot([x0,x0],[y[-1],f(x0)], color="C"+str(i+1), linestyle="--")

    x = np.linspace(INITIAL_X,x0)
    y = f(x)
    plt.plot(x,y,color="black", label="original function")
    plt.axhline(color="black")
    plt.show()