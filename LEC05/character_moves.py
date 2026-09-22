from pico2d import *

open_canvas()
character = load_image('character.png')
character.draw(400, 300)
update_canvas()
delay(10)
close_canvas()