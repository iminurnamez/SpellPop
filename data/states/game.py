import sys
from random import randint, choice 
import pygame as pg
from .. import tools, prepare
from ..components.word import Word


class SpellPop(tools._State):
    def __init__(self):
        super(SpellPop, self).__init__()
        self.font = pg.font.Font(prepare.FONTS["Fixedsys500c"], 64)
        self.screen_rect = pg.display.get_surface().get_rect()
        self.next = "SCORESCREEN"
        self.words = []
        self.score = 0
        self.ticks = 1
        self.word_freq = 100
        
    def startup(self, persistant):
        self.screen_rect = pg.display.get_surface().get_rect()
        self.word_freq = 100
        self.words = []
        self.score = 0
        self.ticks = 1
        
    def get_event(self, event):
        if event.type == pg.QUIT:
            self.done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            for word in self.words:
                if word.rect.collidepoint(event.pos):
                    self.pop_word(word)
                    break
        
    def pop_word(self, word):
        if word.veracity == "Wrong":
            self.score += 1
            prepare.SFX["goodpop"].play()
        else:
            self.score -= 1
            prepare.SFX["badpop"].play()
        word.explode()
        
    def add_word(self):
        veracity = choice(("Correct", "Wrong", "Wrong", "Wrong")) 
        w, h = self.screen_rect.size
        margin = 20
        center_point = (randint(margin, w - margin), randint(margin, h - margin))
        
        new_word = Word(center_point, veracity, choice(prepare.WORDS[veracity]))
        while True:
            if not new_word.rect.collidelist([x.rect for x in self.words]) == -1:
                new_word.rect.center = (randint(margin, w - margin),
                                                     randint(margin, h - margin))
            else:
                break
            
        self.words.append(new_word)
        
    def update(self, surface, keys):
        for word in self.words:
            word.update(self)
        
        collided = set()
        for word in [x for x in self.words if not x.popped]:
            others = [x for x in self.words if x != word and x not in collided]
            for other in others:
                if word.rect.colliderect(other.rect):
                    if word.veracity == "Correct" and other.veracity == "Correct":
                        self.score += 2
                        prepare.SFX["goodpop"].play
                    else:
                        self.score -= 2
                        prepare.SFX["badpop"].play()                        
                    word.explode()
                    other.explode()
                    collided.add(word)
                    collided.add(other)
                    
        self.words = [x for x in self.words if not x.done] 
        if not self.ticks % self.word_freq:
            self.add_word()
                 
                
        self.score = max((self.score, 0))
        
        
        self.draw(surface)
        self.ticks += 1
            
    def draw(self, surface):    
        surface.fill(pg.Color("black"))
        for word in self.words:
            word.draw(surface)
        score_text = self.font.render("{}".format(self.score), True,
                                                   pg.Color("white"), pg.Color("black"))
        score_rect = score_text.get_rect(topright=self.screen_rect.topright)
        surface.blit(score_text, score_rect)
        
        
if __name__ == "__main__":
    main(800, 800, 60)