#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = """Generator for "global-warming".

Parameters:
* type (spec/rand)
* S (seed)
"""



def run(type):
    assert type in ['spec','rand']

    if type=='rand':
        SH=SM=EM=EH=0
        while EH*60+EM-SH*60-SM<=0:
            SH = randint(0,23)
            EH = randint(0,23)
            SM = randint(0,59)
            EM = randint(0,59)
    else:
        SH=SM=EM=EH=0
        while EH*60+EM-SH*60-SM<=0 or SM<EM:
            SH = randint(0,23)
            EH = randint(0,23)
            SM = randint(0,59)
            EM = randint(0,59)
    print(SH)
    print(SM)
    print(EH)
    print(EM)


if __name__ == "__main__":
    num_args = len(signature(run).parameters) + 2
    if len(argv) != num_args:
        print("Got %d parameters, expecting %d" % (len(argv), num_args), file=stderr)
        print(usage, file=stderr)
        exit(1)

    def tryconv(x):
        for t in [int, float, str]:
            try:
                return t(x)
            except:
                pass

    *args, S = map(tryconv, argv[1:])
    seed(S)
    run(*args)
