#!/usr/bin/env python
# -*- coding: utf-8 -*-

class KeyError(Exception):
    def __init__(self, message):
        self.message = message
