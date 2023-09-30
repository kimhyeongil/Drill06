from pico2d import *
import random

class Player:
    def __init__(self):
        self.sprite = load_image('animation_sheet.png')
        self.pos = [get_canvas_width() // 2, get_canvas_height() // 2]
        self.nFrame, self.frame = 8, 0
        self.dir = 'right'
    def draw(self):
        x, y = 0, 1
        if(self.dir == 'left'):
            self.sprite.clip_draw(self.frame * 100, 0, 100, 100, self.pos[x], self.pos[y])
        elif(self.dir == 'right'):
            self.sprite.clip_composite_draw(self.frame * 100, 0, 100, 100, 0, 'h', self.pos[x], self.pos[y], 100, 100)
        self.frame = (self.frame + 1) % self.nFrame

    def track(self, target, t):
        x, y = 0,1
        if(target[x] > self.pos[x]):
            self.dir = 'right'
        else :
            self.dir = 'left'
        self.pos[x] = (1 - t) * self.pos[x] + t * target[x]
        self.pos[y] = (1 - t) * self.pos[y] + t * target[y]

class Hand:
    def __init__(self):
        self.img = load_image('hand_arrow.png')
        self.set_random_pos()
    
    def set_random_pos(self):
        self.pos = [random.randint(0 + self.img.w, get_canvas_width() - self.img.w), random.randint(0 + self.img.h, get_canvas_height() - self.img.h)]   

    def draw(self):
        x, y = 0, 1
        self.img.draw(self.pos[x], self.pos[y])


class GameManager:
    def __init__(self):
        open_canvas(1024,720)
        self.backGround = load_image('TUK_GROUND_FULL.png')
        self.hand = Hand()
        self.w, self.h = 1024, 720
        self.player = Player()
        resize_canvas(self.w, self.h)
    
    def render(self):
        clear_canvas()
        self.backGround.draw(self.w // 2, self.h // 2)
        self.player.draw()
        self.hand.draw()
        update_canvas()
        delay(0.1)

    def isCollide(self, p1, p2, gap):
        return abs(p1[0] - p2[0]) < gap and abs(p1[1] -p2[1]) < gap
    
    def logic(self):
        self.player.track(self.hand.pos, 0.2)
        if( self.isCollide(self.hand.pos, self.player.pos, self.hand.img.w // 2)):
            self.hand.set_random_pos()

GM = GameManager()

while True:
    GM.render()
    GM.logic()
delay(1)

close_canvas()