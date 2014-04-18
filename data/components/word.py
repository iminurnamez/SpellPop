from random import choice
import pygame as pg
from .. import prepare

class Word(object):
    colors = ["lightblue", "red", "yellow", "green", "purple", "orange",
                  "darkgreen", "dodgerblue2"]
    def __init__(self, centerpoint, veracity, word):
        self.color = choice(self.colors)
        self.veracity = veracity
        self.word = word
        self.size = 16
        self.text = pg.font.Font(None, self.size).render(
                                           self.word, True, pg.Color(self.color),
                                           pg.Color("black")).convert()
        self.rect = self.text.get_rect(center=centerpoint)
        self.popped =False
        self.done = False
        self.age = 1
    
    def swell(self):
        self.size += 1
        center = self.rect.center
        self.text = pg.font.Font(None, self.size).render(self.word,
                                           True, pg.Color(self.color),
                                           pg.Color("black")).convert()
        self.rect = self.text.get_rect(center=self.rect.center)
        
    def explode(self):
        w = self.rect.w / 2
        h = self.rect.h / 2
        
        self.surfs = []
        for j in range(2):
            for i in range(2):
                r = pg.Rect((i * w), (j * h), w, h) 
                surf = self.text.subsurface(r)
                loc = (r.centerx + self.rect.left, r.centery + self.rect.top) 
                r.center = loc
                self.surfs.append((surf, r))
        self.explosion_ticks = 20
        self.popped = True
        
    def constrain(self, game):
        sr = game.screen_rect
        self.rect.left = max((self.rect.left, sr.left))
        self.rect.right = min((self.rect.right, sr.right))
        self.rect.top = max((self.rect.top, sr.top))
        self.rect.bottom = min((self.rect.bottom, sr.bottom))
        
    def update(self, game):
        if not self.popped:
            if not self.age % 30:
                self.swell()
                self.constrain(game)
            if self.size > 48:
                if self.veracity == "Correct":
                    game.score += 1
                    prepare.SFX["goodpop"].play()
                else:
                    game.score -= 1
                    prepare.SFX["badpop"].play()
                self.explode()
        else:
            if self.explosion_ticks:
                for surf in self.surfs:
                    dx = surf[1].centerx - self.rect.centerx
                    dy = surf[1].centery - self.rect.centery
                    surf[1].move_ip(cmp(dx, 0) * 2, cmp(dy, 0) * 2)
                self.explosion_ticks -= 1
            else:
                self.done = True
        self.age += 1
    
    def draw(self, surface):
        if not self.popped:
            surface.blit(self.text, self.rect)
        
        else:
            for surf in self.surfs:
                surface.blit(surf[0], surf[1])            
            
            