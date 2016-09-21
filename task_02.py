#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

TEXT = inquisition.SPANISH

MY_VAR = len('Spanish')


POSITION = TEXT.index('Spanish')


FLEMISH = TEXT[:POSITION] + "Flemish" + TEXT[POSITION + MY_VAR:]


print FLEMISH
