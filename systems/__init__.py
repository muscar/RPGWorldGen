# -*- coding: utf-8 -*-

import importlib
import os


def list_systems():
    return [e for e in os.listdir('systems')
            if os.path.isdir(os.path.join('systems', e))]


def load_system(name):
    try:
        return importlib.import_module('.'.join(['systems', name]))
    except ImportError as e:
        raise ValueError("System {0} is not defined".format(name))
