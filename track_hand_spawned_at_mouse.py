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
    def __init__(self, x, y):
        self.img = load_image('hand_arrow.png')
        self.pos = (x, y)
    
    def draw(self):
        x, y = 0, 1
        self.img.draw(self.pos[x], self.pos[y])


class GameManager:
    def __init__(self):
        open_canvas(1024,720)
        self.backGround = load_image('TUK_GROUND_FULL.png')
        self.hands = []
        self.w, self.h = 1024, 720
        self.player = Player()
        resize_canvas(self.w, self.h)
    
    def render(self):
        clear_canvas()
        self.backGround.draw(self.w // 2, self.h // 2)
        for hand in self.hands:
            hand.draw()
        self.player.draw()
        update_canvas()
        delay(0.1)

    def handle_events(self):
        events = get_events()
        for event in events:
            if(event.type == SDL_MOUSEBUTTONDOWN):
                x, y = event.x, self.h - 1 - event.y
                self.hands += [Hand(x, y)]
    
    def isCollide(self, p1, p2, gap):
        return abs(p1[0] - p2[0]) < gap and abs(p1[1] -p2[1]) < gap
    
    def logic(self):
        if(len(self.hands) != 0):
            self.player.track(self.hands[0].pos, 0.2)
            if( self.isCollide(self.hands[0].pos, self.player.pos, self.hands[0].img.w // 4)):
                self.hands.pop(0)

GM = GameManager()

while True:
    GM.handle_events()
    GM.render()
    GM.logic()
delay(1)

close_canvas()