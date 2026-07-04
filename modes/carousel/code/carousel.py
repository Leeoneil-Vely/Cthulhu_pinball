import random
from mpf.modes.carousel.code.carousel import Carousel as MpfCarousel
 
 
class Carousel(MpfCarousel):
 
    def mode_start(self, **kwargs):
        super().mode_start(**kwargs)
        # self._items contient uniquement les items dont les conditions
        # sont remplies (missions non complétées, boss disponibles, etc.)
        if not self._items or len(self._items) <= 1:
            return
 
        # Priorité aux videomodes s'ils sont disponibles
        videomodes = [i for i in self._items if i.startswith('missionVIDEO')]
        if videomodes:
            pool = videomodes
        else:
            # Sinon tout sauf 'exit'
            pool = [i for i in self._items if i != 'exit']
 
        # Fallback au cas où pool serait vide (ne devrait pas arriver)
        if not pool:
            pool = self._items
 
        target = random.choice(pool)
        self._highlighted_item_index = self._items.index(target)
        self._update_highlighted_item(direction=1)
