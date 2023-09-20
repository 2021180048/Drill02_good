from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

while(True):
    x=400
    y=90
    while(x < 750):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
        x=x+5
    while(y < 550):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
        y=y+5
    while(x > 50):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
        x=x-5
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
        y=y-5
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)
        x=x+5
    degree=270
    r=210
    while(degree>-90):
        clear_canvas_now()
        grass.draw_now(400,30)
        x=r*math.cos(degree*math.pi/180)
        y=r*math.sin(degree*math.pi/180)
        character.draw_now(x+400,y+300)
        delay(0.01)
        degree = degree - 1
