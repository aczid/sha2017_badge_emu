# adapted from https://codegolf.stackexchange.com/a/39983
from math import *
badge.eink_init()
n=int(10)
G=(1.0+6.0**.5)/2.0
w=int(G**(4.0*(n//4.0)))
k=pi/90
twist = 100
ugfx.clear(badge.WHITE)
for j in range(n*twist):
    ugfx.pixel(G**(j/float(twist))*cos(j*k)+w/2, G**(j/float(twist))*sin(j*k)+w/2.0, badge.BLACK)

