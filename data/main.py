from . import prepare,tools
from .states import game

def main():
    controller = tools.Control(prepare.ORIGINAL_CAPTION)
    states = {"SPELLPOP": game.SpellPop()}
    controller.setup_states(states, "SPELLPOP")
    controller.main()
