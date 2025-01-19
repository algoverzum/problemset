#!/usr/bin/env python3

from limits import *
from sys import argv, exit, stderr
import os
from random import random, randint, choice, sample, shuffle, seed
from inspect import signature

usage = (
    """Generator for "count-recursive".

Parameters:
* S (seed)

Constraint:
"""
    % ()
)


def run():
    for row in reversed(usage.split("\n")[:-1]):
        if row[0] != "*":
            break
        assert eval(row[2:]), row[2:]

    words = [
        "achievement",
        "acknowledge",
        "administration",
        "administrator",
        "advertising",
        "agricultural",
        "alternative",
        "anniversary",
        "application",
        "appointment",
        "appropriate",
        "approximately",
        "arrangement",
        "association",
        "celebration",
        "championship",
        "characteristic",
        "characterize",
        "cholesterol",
        "circumstance",
        "combination",
        "comfortable",
        "communicate",
        "communication",
        "competition",
        "competitive",
        "complicated",
        "composition",
        "comprehensive",
        "concentrate",
        "concentration",
        "congressional",
        "consciousness",
        "consequence",
        "conservative",
        "considerable",
        "consideration",
        "constitutional",
        "construction",
        "consumption",
        "contemporary",
        "contribution",
        "controversial",
        "controversy",
        "conventional",
        "conversation",
        "cooperation",
        "corporation",
        "correspondent",
        "demonstrate",
        "demonstration",
        "description",
        "destruction",
        "development",
        "differently",
        "discrimination",
        "distinction",
        "distinguish",
        "distribution",
        "dramatically",
        "educational",
        "effectively",
        "electricity",
        "enforcement",
        "engineering",
        "entertainment",
        "environment",
        "environmental",
        "essentially",
        "establishment",
        "examination",
        "expectation",
        "explanation",
        "extraordinary",
        "frustration",
        "fundamental",
        "furthermore",
        "grandfather",
        "grandmother",
        "headquarters",
        "identification",
        "imagination",
        "immediately",
        "immigration",
        "implication",
        "improvement",
        "incorporate",
        "increasingly",
        "independence",
        "independent",
        "information",
        "institution",
        "institutional",
        "instruction",
        "intellectual",
        "intelligence",
        "interaction",
        "interesting",
        "international",
        "interpretation",
        "intervention",
        "introduction",
        "investigate",
        "investigation",
        "investigator",
        "involvement",
        "legislation",
        "maintenance",
        "manufacturer",
        "manufacturing",
        "measurement",
        "necessarily",
        "negotiation",
        "neighborhood",
        "nevertheless",
        "nonetheless",
        "observation",
        "occasionally",
        "opportunity",
        "organization",
        "orientation",
        "participant",
        "participate",
        "participation",
        "particularly",
        "partnership",
        "performance",
        "personality",
        "perspective",
        "photographer",
        "politically",
        "possibility",
        "potentially",
        "preparation",
        "prescription",
        "presentation",
        "presidential",
        "professional",
        "psychological",
        "psychologist",
        "publication",
        "quarterback",
        "recognition",
        "recommendation",
        "relationship",
        "representation",
        "representative",
        "requirement",
        "reservation",
        "responsibility",
        "responsible",
        "restriction",
        "satisfaction",
        "scholarship",
        "significance",
        "significant",
        "significantly",
        "sophisticated",
        "specifically",
        "substantial",
        "successfully",
        "surprisingly",
        "temperature",
        "traditional",
        "transformation",
        "transportation",
        "understanding",
        "unfortunately",
    ]

    abc = list(map(chr, range(ord("a"), ord("z") + 1)))
    x = randint(1, 5)
    i = randint(0, len(words) - 1)
    S = words[i]
    c = choice(abc)
    if x == 1:
        while c in S:
            c = choice(abc)
    else:
        while c not in S:
            c = choice(abc)
    print(S)
    print(c)


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

    *x, S = map(tryconv, argv[1:])
    seed(S)
    run()
