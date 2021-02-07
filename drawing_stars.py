from p5 import *
import time

window_height = 1000
window_width = 1000
a = 50
up_x1 = 20
up_y1 = 20
up_x2 = up_x1 + a
up_y2 = up_y1
up_x3 = up_x1 + a/2
up_y3 = up_y1 + a*sqrt(3)/2
lo_x1 = up_x1
lo_y1 = up_y1+(a*sqrt(3)/3)
lo_x2 = up_x3
lo_y2 = lo_y1-a*sqrt(3)/2
lo_x3 = up_x2
lo_y3 = lo_y1

def my_setup():
    size(window_width, window_height)
    stroke(255)
       
def my_draw():
    background(100)
    dwn = 0
    while dwn < 950:
        for i in range(1,940,a+6):
            fill(10+i/5,10+i/5,0)
            no_stroke()
            triangle(up_x1+i,up_y1+dwn,up_x2+i,up_y2+dwn,up_x3+i,up_y3+dwn)
            triangle(lo_x1+i,lo_y1+dwn,lo_x2+i,lo_y2+dwn,lo_x3+i,lo_y3+dwn)
        dwn = dwn + 60

if __name__ == '__main__':
    run(sketch_setup=my_setup, sketch_draw=my_draw)