# -*- coding: utf-8 -*-

class StatGenBase(object):
    """
    Rreturns a dictionary mapping ability scores to
    values drawn from _roll_stat()
    """

    def generate(self):
        return dict((score, self._roll_stat()) for score in self.ABILITY_SCORES)
