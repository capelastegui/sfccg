""" Module description
.. moduleauthor:: Pedro Capelastegui <pcapelastegui@gmail.com>
"""
# Imports
import logging
from enum import Enum
import pandas as pd
import numpy as np

# Globals

logger = logging.getLogger(__name__)

CardColor = Enum('CardColor', 'White Green Red Black Blue Colorless')

class CardBase:
    def __init__(self, name, cost='1',colors=None,types=None,traits=None, tags=None,
                 rules='', power=None,toughness=None,is_token=False):
        self.name=name
        self.cost=cost
        self.colors=colors
        self.types=types
        self.traits=traits
        self.tags=tags
        self.rules=rules
        self.power=power
        self.toughness=toughness
        self.is_token=is_token

    def __str__(self):
        result = (
            """Card: {name}"""
        ).format(name=self.name)


"""
TODO:
- Collector info: class, take cardBase, add set, rarity
- CardInPlay: class, take cardBase, add modifiers, counters, token, is_tapped...
- GameCardList: Ordered List of cards in the game - represents library, graveyard, exile, hand
- Each player's permanents is a GameCardList
- Visual representation is described elsewhere, including a player's card arrangements.

"""

