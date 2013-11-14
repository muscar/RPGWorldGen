# -*- coding: utf-8 -*-

from systems.sw.stat_gen import StatGen


stat_gen = StatGen()


def gen_stats():
    return stat_gen.generate()
