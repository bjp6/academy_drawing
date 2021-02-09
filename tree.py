from p5 import *
#recursive programming: always include some elements which stops execution to avoid overflow
#expand tree with three branches
# investigate fractals
# include movement
# lindenmayer system of plants

window_height = 1000
window_width = 1000
branch_angle = 40
rot_left = -radians(branch_angle)
rot_middle = 0
rot_right = radians(branch_angle)
thickness = 13
depth = 7
length = 200
#t = 0.02 #introduce rotation

def my_setup():
    size(window_width, window_height)
    stroke(101,67,63)
    
def my_draw():
    background(100,100,100)
    translate(window_width*0.5,window_height-200)
    tree(depth, thickness, length)
    
def tree(levels, trunk_thickness, branch_len):
    #global t
    if levels == 0:
        fill(50,200,0)
        ellipse(0, 0, 6, 20)
        return
    
    stroke_weight(trunk_thickness)
    line((0, 0), (0, -branch_len))
    
    translate(0, -branch_len)
    #rotate(sin(t))
    #t = t + 0.002
    push_matrix()
    rotate_z(rot_left)
    tree(levels-1, int(trunk_thickness*0.7), int(branch_len*0.75))
    pop_matrix()

    push_matrix()
    rotate_z(-rot_middle)
    tree(levels - 1, int(trunk_thickness*0.7), int(branch_len*0.75))
    pop_matrix()

    push_matrix()
    rotate_z(rot_right)
    tree(levels - 1, int(trunk_thickness*0.7), int(branch_len*0.75))
    pop_matrix()

if __name__ == '__main__':
    run(sketch_setup=my_setup, sketch_draw=my_draw)