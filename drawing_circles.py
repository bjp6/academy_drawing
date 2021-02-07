from p5 import *

window_height = 1000
window_width = 1000

def my_setup():
    size(window_width, window_height)
    stroke(255)
       
def my_draw():
    background(100)
    y = window_height * 0.5
    line((0, y), (window_width, y))
    line((0,0),(1000,1000))

    for i in range(1,2500,4):
        fill(255,0,0)
        stroke(255)
        circle(i/2*sin(i*45), i/2*cos(i*45), 100)
        color = int(i/10)
        fill(color,0,0)
        no_stroke()
        circle(900+i/100,920+i/100,10)

if __name__ == '__main__':
    run(sketch_setup=my_setup, sketch_draw=my_draw)