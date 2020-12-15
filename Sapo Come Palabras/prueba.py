from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from drawnow import drawnow
from scipy.integrate import odeint, quad
from scipy.optimize import brentq
import sys
from PIL import Image, ImageDraw
import glob
import io
import decimal

angle=np.pi/180
radio=5
for i in range(360):
    plt.xlim(-6,6)
    plt.ylim(-6,6)
    plt.scatter([np.cos(angle)*radio],[np.sin(angle)*radio])
    plt.draw()
    plt.pause(0.2)
    #plt.clf()
    angle=angle+np.pi/180
