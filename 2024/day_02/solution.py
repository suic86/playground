#!/usr/bin/env python3
from json import load


def load_data(path: str):
    with open(path) as fobj:
        return load(fobj)
