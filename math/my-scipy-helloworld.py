#This is the scipy Hello World
from numpy import *
import pylab

x = [0, 0];

A = [ [.5, 0], [0, .5] ];
b1 = [0, 0];
b2 = [.5, 0];
b3 = [.25, sqrt(3)/4];

for i in range(3000): # 3000 points will be generated
 r = fix(random.rand()*3)
 if r==0:
  x = dot(A,x)+b1
 if r==1:
  x = dot(A,x)+b2
 if r==2:
  x = dot(A,x)+b3
 pylab.plot(x[0],x[1],'m.',markersize=2)

pylab.show()