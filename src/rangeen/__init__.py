# -*- coding: utf-8 -*-
'''
Rangeen ASCII color library for terminals
------------------------------------------

Usage:

    from rangeen import emotes
    print(f"{emotes.heart} from India!")

    from rangeen import warning
    warning_text = warning("this is a warning")
    print(warning_text)

    from rangeen import colors, colorify
    yellow_text_with_white_background = colorify("THIS IS A SAMPLE", fg=colors.YELLOW, bg=colors.WHITE)

:copyright: (c) 2020 by Shanu Khera.
:license: MIT, see LICENSE for more details.
'''

__version_info__ = (0, 0, 1)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "Shanu Khera"

from ._colors import Color
from ._emotes import Emote
from ._utils import Util

colors = Color()
emotes = Emote()

def colorify(text, fg=colors.RESET, bg=colors.RESET):
    return Util._bg(Util._fg(text, fg), bg)

def info(text): return colorify(text, fg=colors.BLUE)
def warning(text): return colorify(text, fg=colors.YELLOW)
def danger(text): return colorify(text, fg=colors.RED)

__all__ = [colors, emotes, colorify, info, warning, danger]
