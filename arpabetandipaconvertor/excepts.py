#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PhonemeError(Exception):
    def __init__(self, message):
        self.message = message
