import pygame as pg
from .. import tools, prepare

class ScoreScreen(tools._State):
    def __init__(self):
        super(ScoreScreen, self).__init__()
        self.num_font = pg.font.Font(prepare.FONTS["Fixedsys500c"], 128)
        self.font = pg.font.Font(prepare.FONTS["freesansbold"], 48)
        self.correct = self.font.render("Play Again", True, pg.Color("white"))
        self.wrong = self.font.render("Play Agen", True, pg.Color("white"))
        
    def startup(self, persistant):
        self.next = None
        self.screen_rect = pg.display.get_surface().get_rect()
        self.high_score = persistant["high score"]
        self.score_num = self.num_font.render("{}".format(self.high_score), True, 
                                                                  pg.Color("white"))
        self.num_rect = self.score_num.get_rect(center=self.screen_rect.center)
        self.correct_rect = self.correct.get_rect(bottomright=(self.screen_rect.centerx - 50,
                                                                                       self.screen_rect.bottom - 30))
        self.wrong_rect = self.wrong.get_rect(bottomleft=(self.screen_rect.centerx + 50,
                                                                                   self.screen_rect.bottom - 30))
    
    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.correct_rect.collidepoint(event.pos):
                self.next = "SELECTSCREEN"
                self.done = True
            elif self.wrong_rect.collidepoint(event.pos):
                self.quit = True
                self.done = True
                
    def draw(self, surface):
        surface.fill(pg.Color("black"))
        surface.blit(self.correct, self.correct_rect)
        surface.blit(self.wrong, self.wrong_rect)
        surface.blit(self.score_num, self.num_rect)
        
    def update(self, surface, keys):
        self.draw(surface)

