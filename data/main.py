from . import prepare,tools
from .states import game, scorescreen, selectscreen

def main():
    controller = tools.Control(prepare.ORIGINAL_CAPTION)
    states = {"SELECTSCREEN": selectscreen.SelectScreen(),
                   "SPELLPOP": game.SpellPop(),
                   "SCORESCREEN": scorescreen.ScoreScreen()}
    controller.setup_states(states, "SELECTSCREEN")
    controller.main()
