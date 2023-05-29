#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as a:
        sys.stderr.write(f"Exception: {a}\n")
        return None
