from p5 import *
import time

window_height = 1000
window_width = 1000
a = 50
xys_1 = [20,20,20+a,20,20+a/2,20+a*sqrt(3)/2]
#up_x1 = 20
#up_y1 = 20
#up_x2 = up_x1 + a
#up_y2 = up_y1
#up_x3 = up_x1 + a/2
#up_y3 = up_y1 + a*sqrt(3)/2
xys_2 = [xys_1[0],xys_1[1]+(a*sqrt(3)/3),xys_1[4],xys_1[1]+a*sqrt(3)/3-a*sqrt(3)/2,xys_1[2],xys_1[1]+(a*sqrt(3)/3)]
#lo_x1 = up_x1
#lo_y1 = up_y1+(a*sqrt(3)/3)
#lo_x2 = up_x3
#lo_y2 = lo_y1-a*sqrt(3)/2
#lo_x3 = up_x2
#lo_y3 = lo_y1

def my_setup():
    size(window_width, window_height)
    stroke(255)
       
def my_draw():
    background(0,0,180)
    dwn = 0
    while dwn < 950:
        for i in range(1,940,a+6):
            fill(10+i/5,10+i/5,0)
            no_stroke()
            triangle(xys_1[0]+i,xys_1[1]+dwn,xys_1[2]+i,xys_1[3]+dwn,xys_1[4]+i,xys_1[5]+dwn)
            triangle(xys_2[0]+i,xys_2[1]+dwn,xys_2[2]+i,xys_2[3]+dwn,xys_2[4]+i,xys_2[5]+dwn)
        dwn = dwn + 61

if __name__ == '__main__':
    run(sketch_setup=my_setup, sketch_draw=my_draw)