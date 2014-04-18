import pygame as pg
from .. import tools, prepare

class SelectScreen(tools._State):
    def __init__(self):
        super(SelectScreen, self).__init__()
        self.next = "SPELLPOP"
        screen_rect = pg.display.get_surface().get_rect()
        self.font = pg.font.Font(prepare.FONTS["freesansbold"], 48)
        title_font = pg.font.Font(prepare.FONTS["freesansbold"], 96)
        title = title_font.render("Boring Spelling Game", True, pg.Color("white"))
        self.title = (title, title.get_rect(midtop=(screen_rect.centerx, 10)))
        
        levels = ("Easy", "Normal", "Hard", "Even Harder") 
        x = screen_rect.centerx
        y = self.title[1].bottom + 140
        space = 50
        self.buttons = []
        for level in levels:
            text = self.font.render(level, True, pg.Color("white"))
            rect = text.get_rect(midtop=(x, y))
            self.buttons.append((text, rect, level))
            y += rect.height + space
            
    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button[1].collidepoint(event.pos):
                    self.persist["level"] = button[2]
                    self.done = True
                    
    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.title[0], self.title[1])
        for button in self.buttons:
            surface.blit(button[0], button[1])
              
    def update(self, surface, keys):
        self.draw(surface)    