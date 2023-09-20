from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('circle')
    
    cx = 800 / 2
    cy = 600 / 2
    r = 200
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(deg /360 * 2 * math.pi)
        y = cy + r * math.sin(deg /360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)
        delay(0.1)


def run_rectangle():
    print('rectangle')
    #bottom line
    for x in range(50,750+1,10):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,90)
        delay(0.01)

    pass

while (True):
    run_rectangle()
    #run_circle()
    break


close_canvas()
